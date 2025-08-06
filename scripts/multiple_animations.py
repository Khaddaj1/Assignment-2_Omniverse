from pxr import Usd, UsdGeom, Sdf, Gf

def create_multiple(output_path: str = "multiple_animations.usda"):
    stage = Usd.Stage.CreateNew(output_path)
    stage.SetStartTimeCode(1)
    stage.SetEndTimeCode(192)
    orig = UsdGeom.Xform.Define(stage, "/Original")
    orig.GetPrim().GetReferences().AddReference("animated_robot.usda", "/Robot")
    orig.AddTranslateOp().Set(Gf.Vec3d(0, 0, 0))
    shifted = UsdGeom.Xform.Define(stage, "/Shifted")
    shifted.GetPrim().GetReferences().AddReference(
        "animated_robot.usda",
        "/Robot",
        Sdf.LayerOffset(offset=48)
    )
    shifted.AddTranslateOp().Set(Gf.Vec3d(5, 0, 0))
    half = UsdGeom.Xform.Define(stage, "/HalfSpeed")
    half.GetPrim().GetReferences().AddReference(
        "animated_robot.usda",
        "/Robot",
        Sdf.LayerOffset(scale=0.5)
    )
    half.AddTranslateOp().Set(Gf.Vec3d(10, 0, 0))
    stage.GetRootLayer().Save()
    print(f"Created {output_path}")

if __name__ == "__main__":
    create_multiple()