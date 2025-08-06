from pxr import Usd, UsdGeom, Gf, UsdPhysics

def create_physics(output_path: str = "physics_robot.usda"):
    stage = Usd.Stage.CreateNew(output_path)
    stage.SetStartTimeCode(1)
    stage.SetEndTimeCode(192)
    root = UsdGeom.Xform.Define(stage, "/Robot")
    root.AddTranslateOp().Set(Gf.Vec3d(0, 0, 5))
    root.GetPrim().GetReferences().AddReference("animated_robot.usda", "/Robot")
    UsdPhysics.RigidBodyAPI.Apply(root.GetPrim())
    UsdPhysics.CollisionAPI.Apply(root.GetPrim())
    mat = UsdPhysics.Material.Define(stage, "/PhysMaterial")
    mat.CreateStaticFrictionAttr(1.0)
    mat.CreateDynamicFrictionAttr(0.7)
    mat.CreateRestitutionAttr(0.9)
    UsdPhysics.MaterialBindingAPI.Apply(root.GetPrim()).Bind(mat.GetPrim())
    ground = UsdGeom.Cube.Define(stage, "/Ground")
    ground.AddScaleOp().Set(Gf.Vec3d(10, 0.1, 10))
    UsdPhysics.CollisionAPI.Apply(ground.GetPrim())
    stage.GetRootLayer().Save()
    print(f"Created {output_path}")

if __name__ == "__main__":
    create_physics()
