import ansys.mechanical.core as mech
from ansys.mechanical.core.examples import delete_downloads, download_file
import pytest


@pytest.mark.embedding
def test_embedding_simple():
    # Embed Mechanical and set global variables
    app = mech.App(version=232)
    globals().update(mech.global_variables(app))
    print(app)

    # Import geometry
    geometry_path = download_file("Valve.pmdb", "pymechanical", "embedding")
    geometry_file = geometry_path
    geometry_import = Model.GeometryImportGroup.AddGeometryImport()
    geometry_import_format = (
        Ansys.Mechanical.DataModel.Enums.GeometryImportPreference.Format.Automatic
    )
    geometry_import_preferences = Ansys.ACT.Mechanical.Utilities.GeometryImportPreferences()
    geometry_import_preferences.ProcessNamedSelections = True
    geometry_import.Import(geometry_file, geometry_import_format, geometry_import_preferences)
    # Settinng up Analsys
    analysis = Model.AddStaticStructuralAnalysis()
    material_assignment = Model.Materials.AddMaterialAssignment()
    material_assignment.Material = "Structural Steel"
    sel = ExtAPI.SelectionManager.CreateSelectionInfo(
        Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities
    )
    sel.Ids = [
        body.GetGeoBody().Id
        for body in Model.Geometry.GetChildren(
            Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory.Body, True
        )
    ]
    material_assignment.Location = sel

    # Define mesh settings,  generate mesh
    mesh = Model.Mesh
    mesh.ElementSize = Quantity(25, "mm")
    mesh.GenerateMesh()

    fixed_support = analysis.AddFixedSupport()
    fixed_support.Location = ExtAPI.DataModel.GetObjectsByName("NSFixedSupportFaces")[0]

    frictionless_support = analysis.AddFrictionlessSupport()
    frictionless_support.Location = ExtAPI.DataModel.GetObjectsByName("NSFrictionlessSupportFaces")[
        0
    ]

    pressure = analysis.AddPressure()
    pressure.Location = ExtAPI.DataModel.GetObjectsByName("NSInsideFaces")[0]

    pressure.Magnitude.Inputs[0].DiscreteValues = [Quantity("0 [s]"), Quantity("1 [s]")]
    pressure.Magnitude.Output.DiscreteValues = [Quantity("0 [Pa]"), Quantity("15 [MPa]")]

    # Solve model
    config = ExtAPI.Application.SolveConfigurations["My Computer"]
    config.SolveProcessSettings.MaxNumberOfCores = 1
    config.SolveProcessSettings.DistributeSolution = False
    Model.Solve()

    ###################################################################################
    # Postprocessing
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Evaluate results, export screenshots
    solution = analysis.Solution
    deformation = solution.AddTotalDeformation()
    stress = solution.AddEquivalentStress()
    solution.EvaluateAllResults()
    assert str(solution.Status) == "Done", "Solution status is not 'Done'"
    app.new()
    delete_downloads()
