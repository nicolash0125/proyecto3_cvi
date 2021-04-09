import bpy

class SunUp(bpy.types.Operator):
    bl_idname = "wm.sun_up"
    bl_label = "Adelanta"

    def execute(self, context):
        print("Subiendo sol")
        bpy.data.objects["Point"].location.z = bpy.data.objects["Point"].location.z+5
        return {'FINISHED'}

bpy.utils.register_class(SunUp)

class SunDown(bpy.types.Operator):
    bl_idname = "wm.sun_down"
    bl_label = "Atrasa"

    def execute(self, context):
        print("Subiendo sol")
        bpy.data.objects["Point"].location.z = bpy.data.objects["Point"].location.z-5
        return {'FINISHED'}

bpy.utils.register_class(SunDown)


class SetCam1(bpy.types.Operator):
    bl_idname = "wm.set_cam1"
    bl_label = "Camara 1"

    def execute(self, context):
        print("Cambiando camara")
        bpy.context.scene.camera = bpy.data.objects["Camera_1"]
        return {'FINISHED'}

bpy.utils.register_class(SetCam1)

class SetCam2(bpy.types.Operator):
    bl_idname = "wm.set_cam2"
    bl_label = "Camara 2"

    def execute(self, context):
        print("Cambiando camara")
        bpy.context.scene.camera = bpy.data.objects["Camera_2"]
        return {'FINISHED'}

bpy.utils.register_class(SetCam2)

class SetCam3(bpy.types.Operator):
    bl_idname = "wm.set_cam3"
    bl_label = "Camara 3"

    def execute(self, context):
        print("Cambiando camara")
        bpy.context.scene.camera = bpy.data.objects["Camera_3"]
        return {'FINISHED'}

bpy.utils.register_class(SetCam3)

class ControlPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_controles"
    bl_label = "Controles"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    #bl_category = "Tab"

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="Control de la escena")

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.label(text="Control de la hora del dia")
        row = box.row()
        row.operator("wm.sun_down")
        row.operator("wm.sun_up")

        box = layout.box()
        box.label(text="Control de las camaras")
        row = box.row()
        row.operator("wm.set_cam1")
        row = box.row()
        row.operator("wm.set_cam2")
        row = box.row()
        row.operator("wm.set_cam3")

bpy.utils.register_class(ControlPanel)
