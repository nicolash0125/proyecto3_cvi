import bpy
from random import random,randrange

for obj in bpy.data.collections['Objects'].all_objects:
    obj.select_set(True)

bpy.ops.object.delete()

#Texturas

#Textura hojas
textura_hojas = bpy.data.materials.new(name="Textura_Hojas")
textura_hojas.use_nodes = True
bsdf = textura_hojas.node_tree.nodes["Principled BSDF"]
texImage = textura_hojas.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Downloads/hojas.jpg")
textura_hojas.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])



#Textura tronco
textura_tronco = bpy.data.materials.new(name="Textura_Tronco")
textura_tronco.use_nodes = True
bsdf = textura_tronco.node_tree.nodes["Principled BSDF"]
texImage = textura_tronco.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Downloads/tronco.jpg")
textura_tronco.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

#Textura tela
textura_tela = bpy.data.materials.new(name="Textura_Tela")
textura_tela.use_nodes = True
bsdf = textura_tela.node_tree.nodes["Principled BSDF"]
texImage = textura_tela.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Downloads/tela.jpg")
textura_tela.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

#Textura metal
textura_metal = bpy.data.materials.new(name="Textura_Metal")
textura_metal.use_nodes = True
bsdf = textura_metal.node_tree.nodes["Principled BSDF"]
texImage = textura_metal.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Downloads/acero1.jpg")
textura_metal.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])




#Arboles

numArboles=10
posArboles=[(1,1),(2,0),(-3,2),(2,-2),(4,2),(1,-3),(1,-4.5),(1,-5.5),(3,-5),(2,-6),(-2.5,-7),(-3,8),(1,3),(-2,4),(-1,5),(-3,4),(-4,3),(-4,2.5),(-5,1.5),(-4,0)]
for i in posArboles:
    numHojas=30
    (pos_x,pos_y)=i
    pos_z=1
    bpy.ops.mesh.primitive_cylinder_add(location=(0, 0, 1))
    bpy.ops.transform.resize(value=(0.25, 0.25, 1), orient_type='LOCAL')
    ob = bpy.context.active_object
    ob.data.materials.append(textura_tronco)
    ob =  bpy.data.objects['Cylinder']
    ob.name = "Tree."+str(i)
    ob.data.name = "Tree."+str(i)

    for n in range(numHojas):
        bpy.ops.mesh.primitive_ico_sphere_add(location=(random()-0.5, random()-0.5, 1+3*random()/2))
        bpy.ops.transform.resize(value=(0.3, 0.3, 0.3), orient_type='LOCAL')
        ob = bpy.context.active_object
        ob.data.materials.append(textura_hojas)

        obs=[bpy.data.objects['Icosphere'], bpy.data.objects["Tree."+str(i)] ]
        c = {}
        c["object"] = c["active_object"] = bpy.data.objects["Tree."+str(i)]
        c["selected_objects"] = c["selected_editable_objects"] = obs
        bpy.ops.object.join(c)
        ob =  bpy.data.objects["Tree."+str(i)]
        ob.name = "Tree."+str(i)
        ob.data.name = "Tree."+str(i)
    bpy.data.objects["Tree."+str(i)].location.x = pos_x
    bpy.data.objects["Tree."+str(i)].location.y = pos_y
    bpy.data.objects["Tree."+str(i)].location.z = pos_z
    
#Carpas

posCarpas=[(0,0,0.5),(-1,1,0.5),(-2,1,0.5),(0,-1,0.5),(-2,-2,0.5),(-1,-2,0.5),(-3,0,0.5),(-3,-1,0.5)]

for i in posCarpas:
    bpy.ops.mesh.primitive_cone_add(location=i)
    bpy.ops.transform.resize(value=(0.5, 0.5, 0.5), orient_type='LOCAL')
    ob = bpy.context.active_object
    ob.data.materials.append(textura_tela)
    ob =  bpy.data.objects['Cone']
    ob.name = "Carpa."+str(i)

#Fogata

bpy.ops.mesh.primitive_cylinder_add(location=(-1.5, -0.5, 0.25))

bpy.ops.transform.resize(value=(0.08, 0.08, 0.3), orient_type='LOCAL')
bpy.ops.transform.rotate(value=3.14*0.2, orient_axis='X')
bpy.ops.transform.rotate(value=3.14*0.8, orient_axis='Y')
bpy.ops.rigidbody.object_add()
ob = bpy.context.active_object
ob.data.materials.append(textura_tronco)



bpy.ops.mesh.primitive_cylinder_add(location=(-1.5, -0.5, 0.25))
bpy.ops.transform.resize(value=(0.08, 0.08, 0.3), orient_type='LOCAL')
bpy.ops.transform.rotate(value=3.14*0.6, orient_axis='X')
bpy.ops.transform.rotate(value=3.14*0.2, orient_axis='Y')
bpy.ops.rigidbody.object_add()
ob = bpy.context.active_object
ob.data.materials.append(textura_tronco)

bpy.ops.mesh.primitive_cylinder_add(location=(-1.5, -0.5, 0.25))
bpy.ops.transform.resize(value=(0.08, 0.08, 0.3), orient_type='LOCAL')
bpy.ops.transform.rotate(value=3.14*1.2, orient_axis='X')
bpy.ops.transform.rotate(value=3.14*0.2, orient_axis='Y')
bpy.ops.rigidbody.object_add()
ob = bpy.context.active_object
ob.data.materials.append(textura_tronco)

bpy.ops.mesh.primitive_cylinder_add(location=(-1.5, -0.5, 0.25))
bpy.ops.transform.resize(value=(0.08, 0.08, 0.3), orient_type='LOCAL')
bpy.ops.transform.rotate(value=3.14*0.2, orient_axis='X')
bpy.ops.transform.rotate(value=3.14*1.2, orient_axis='Y')
bpy.ops.rigidbody.object_add()
ob = bpy.context.active_object
ob.data.materials.append(textura_tronco)




#Carro

bpy.ops.mesh.primitive_cube_add(location=(-4, -5, 0.5))
bpy.ops.transform.resize(value=(1, 0.5, 0.5), orient_type='LOCAL')
ob = bpy.context.active_object
ob.data.materials.append(textura_metal)
 
bpy.ops.mesh.primitive_cube_add(location=(-4, -5, 0.25))
bpy.ops.transform.resize(value=(2, 0.5, 0.25), orient_type='LOCAL')
ob = bpy.context.active_object
ob.data.materials.append(textura_metal)






