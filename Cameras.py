import bpy

# Elimina todos los objetos

for obj in bpy.data.collections['Cameras'].all_objects:
    obj.select_set(True)

bpy.ops.object.delete()


cam1 = bpy.data.cameras.new(name='Camera_1')
cam1.lens = 15
cam_ob_1 = bpy.data.objects.new('Camera_1', cam1)
cam_ob_1.location=(-3.5,-3.5,1)
cam_ob_1.rotation_euler = (3.14/2, 0, 5.2*3.14/3)
bpy.data.collections['Cameras'].objects.link(cam_ob_1)


cam2 = bpy.data.cameras.new(name='Camera_2')
cam2.lens = 25
cam_ob_2 = bpy.data.objects.new('Camera_2', cam2)
cam_ob_2.location=(-7,-2.5,2)
cam_ob_2.rotation_euler = (2.84/2, 0, -2*3.14/3)
bpy.data.collections['Cameras'].objects.link(cam_ob_2)

cam3 = bpy.data.cameras.new(name='Camera_3')
cam3.lens = 55
cam_ob_3 = bpy.data.objects.new('Camera_3', cam3)
cam_ob_3.location=(10,25,20)
cam_ob_3.rotation_euler = (1.84/2, 0, 2.5*3.14/3)
bpy.data.collections['Cameras'].objects.link(cam_ob_3)
