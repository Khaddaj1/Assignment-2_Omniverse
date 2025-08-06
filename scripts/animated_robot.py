from pxr import Usd, UsdGeom, Gf

def create_animated_robot(output_path: str = "animated_robot.usda"):
    stage = Usd.Stage.CreateNew(output_path)
    stage.SetStartTimeCode(1)
    stage.SetEndTimeCode(192)
    root = UsdGeom.Xform.Define(stage, "/Robot")
    root.GetPrim().GetReferences().AddReference("robot.usda", "/Robot")
    base_op = UsdGeom.Xformable(stage.GetPrimAtPath("/Robot/Base")).AddRotateZOp(opSuffix="anim:baseSpin")
    base_op.Set(0.0, time=1)
    base_op.Set(360.0, time=192)
    upper_op = UsdGeom.Xformable(
        stage.GetPrimAtPath(
            "/Robot/Base/LowerArm_xf/LowerArm/"
            "UpperArm_base_xf/UpperArm_rot_xf"
        )
    ).AddRotateZOp(opSuffix="anim:twist")
    upper_op.Set(0.0, time=1)
    upper_op.Set(30.0, time=96)
    grip_op = UsdGeom.Xformable(
        stage.GetPrimAtPath(
            "/Robot/Base/LowerArm_xf/LowerArm/"
            "UpperArm_base_xf/UpperArm_rot_xf/"
            "UpperArm/Gripper_xf"
        )
    ).AddScaleOp(opSuffix="anim:gripScale")
    grip_op.Set(Gf.Vec3f(1.0), time=1)
    grip_op.Set(Gf.Vec3f(2.0), time=96)
    grip_op.Set(Gf.Vec3f(1.0), time=192)
    stage.GetRootLayer().Save()
    print(f"Created {output_path}")

if __name__ == "__main__":
    create_animated_robot()
