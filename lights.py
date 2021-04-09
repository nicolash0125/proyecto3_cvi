#Agrega luces

import bpy
from random import randint

for obj in bpy.data.collections['Lights'].all_objects:
    obj.select_set(True)
    
bpy.ops.object.delete()

bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(26.77, 0, 0), scale=(1, 1, 1))
bpy.context.object.data.color = (1, 0.9, 0.4288181)
bpy.context.object.data.energy = 100774

bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(-1.5, -0.5, 0.3), scale=(1, 1, 1))
bpy.context.object.data.color = (1, 0.482994, 0.0892071)
bpy.context.object.data.energy = 50

bpy.ops.object.light_add(type='SPOT', align='WORLD', location=(-1.9, -5.25, 0.25), scale=(1, 1, 1))
bpy.ops.transform.rotate(value=-3.14*0.45, orient_axis='Y')
bpy.context.object.data.energy = 200
bpy.ops.object.light_add(type='SPOT', align='WORLD', location=(-1.9, -4.75, 0.25), scale=(1, 1, 1))
bpy.ops.transform.rotate(value=-3.14*0.45, orient_axis='Y')
bpy.context.object.data.energy = 200


