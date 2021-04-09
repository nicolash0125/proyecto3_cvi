
#Loads WangTiles
import bpy
from random import randint

for obj in bpy.data.collections['Ground'].all_objects:
    obj.select_set(True)

bpy.ops.object.delete()

# Elimina materials

for material in bpy.data.materials:
    material.user_clear()
    bpy.data.materials.remove(material)
    

#definicion texturas

#Textura 0
mat_0 = bpy.data.materials.new(name="Textura_0")
mat_0.use_nodes = True
bsdf = mat_0.node_tree.nodes["Principled BSDF"]
texImage = mat_0.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/0.jpg")
mat_0.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

#Textura 1
mat_1 = bpy.data.materials.new(name="Textura_1")
mat_1.use_nodes = True
bsdf = mat_1.node_tree.nodes["Principled BSDF"]
texImage = mat_1.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/1.jpg")
mat_1.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

#Textura 2
mat_2 = bpy.data.materials.new(name="Textura_2")
mat_2.use_nodes = True
bsdf = mat_2.node_tree.nodes["Principled BSDF"]
texImage = mat_2.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/2.jpg")
mat_2.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

#Textura 3
mat_3 = bpy.data.materials.new(name="Textura_3")
mat_3.use_nodes = True
bsdf = mat_3.node_tree.nodes["Principled BSDF"]
texImage = mat_3.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/3.jpg")
mat_3.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

#Textura 4
mat_4 = bpy.data.materials.new(name="Textura_4")
mat_4.use_nodes = True
bsdf = mat_4.node_tree.nodes["Principled BSDF"]
texImage = mat_4.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/4.jpg")
mat_4.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

#Textura 5
mat_5 = bpy.data.materials.new(name="Textura_5")
mat_5.use_nodes = True
bsdf = mat_5.node_tree.nodes["Principled BSDF"]
texImage = mat_5.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/5.jpg")
mat_5.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

#Textura 6
mat_6 = bpy.data.materials.new(name="Textura_6")
mat_6.use_nodes = True
bsdf = mat_6.node_tree.nodes["Principled BSDF"]
texImage = mat_6.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/6.jpg")
mat_6.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

#Textura 7
mat_7 = bpy.data.materials.new(name="Textura_7")
mat_7.use_nodes = True
bsdf = mat_7.node_tree.nodes["Principled BSDF"]
texImage = mat_7.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/7.jpg")
mat_7.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

#Textura 8
mat_8 = bpy.data.materials.new(name="Textura_8")
mat_8.use_nodes = True
bsdf = mat_8.node_tree.nodes["Principled BSDF"]
texImage = mat_8.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/8.jpg")
mat_8.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

#Textura 9
mat_9 = bpy.data.materials.new(name="Textura_9")
mat_9.use_nodes = True
bsdf = mat_9.node_tree.nodes["Principled BSDF"]
texImage = mat_9.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/9.jpg")
mat_9.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

#Textura 10
mat_10 = bpy.data.materials.new(name="Textura_10")
mat_10.use_nodes = True
bsdf = mat_10.node_tree.nodes["Principled BSDF"]
texImage = mat_10.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/10.jpg")
mat_10.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

#Textura 11
mat_11 = bpy.data.materials.new(name="Textura_11")
mat_11.use_nodes = True
bsdf = mat_11.node_tree.nodes["Principled BSDF"]
texImage = mat_11.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/11.jpg")
mat_11.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])



#Textura 12
mat_12 = bpy.data.materials.new(name="Textura_12")
mat_12.use_nodes = True
bsdf = mat_12.node_tree.nodes["Principled BSDF"]
texImage = mat_12.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/12.jpg")
mat_12.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])


#Textura 13
mat_13 = bpy.data.materials.new(name="Textura_13")
mat_13.use_nodes = True
bsdf = mat_13.node_tree.nodes["Principled BSDF"]
texImage = mat_13.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/13.jpg")
mat_13.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])


#Textura 14
mat_14 = bpy.data.materials.new(name="Textura_14")
mat_14.use_nodes = True
bsdf = mat_14.node_tree.nodes["Principled BSDF"]
texImage = mat_14.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/14.jpg")
mat_14.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

#Textura 15
mat_15 = bpy.data.materials.new(name="Textura_15")
mat_15.use_nodes = True
bsdf = mat_15.node_tree.nodes["Principled BSDF"]
texImage = mat_15.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("/Users/nicolas/Desktop/tiles/15.jpg")
mat_15.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])



texturas = [mat_0,mat_1,mat_2,mat_3,mat_4,mat_5,mat_6,mat_7,mat_8,mat_9,mat_10,mat_11,mat_12,mat_13,mat_14,mat_15]

bottom_bb=[0,1,8,9]
bottom_by=[2,3,10,11]
bottom_yb=[4,5,12,13]
bottom_yy=[6,7,14,15]

top_bb=[0,2,4,6]
top_by=[1,3,5,7]
top_yb=[8,10,12,14]
top_yy=[9,11,13,15]

rigth_bb=[0,4,8,12]
rigth_by=[2,6,10,14]
rigth_yb=[1,5,9,13]
rigth_yy=[3,7,11,15]

left_bb=[0,1,8,9]
left_by=[2,3,10,11]
left_yb=[4,5,12,13]
left_yy=[6,7,14,15]


matAnt=0
x_0=-25
y_0=-25
bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD', location=(0+x_0, 0+y_0, 0), scale=(1, 1, 1))
ob = bpy.context.active_object
ob.data.materials.append(texturas[0])
first=True
ancho=50
alto=50

ob =  bpy.data.objects['Plane']
ob.name = "Ground"
ob.data.name = "Ground"


col= [1 for i in range(alto)]
for i in range(ancho):
    print(i)
    for j in range(alto):
        if not (j==0 and i==0):
            bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD', location=(i+x_0, j+y_0, 0), scale=(1, 1, 1))
            #bpy.ops.transform.rotate(value=2*3.14, orient_axis='Z')
            ob = bpy.context.active_object
            #Para la primera fila
            if(first):
                #Anterior en bb
                if (matAnt in top_bb):
                    n=randint(0,len(bottom_bb)-1)
                    a=bottom_bb[n]
                    mat=texturas[a]
                    matAnt=a
                    col[j]=a
                    ob.data.materials.append(mat)
                else:
                    #Anterior en by
                    if (matAnt in top_by):
                        n=randint(0,len(bottom_by)-1)
                        a=bottom_by[n]
                        mat=texturas[a]
                        matAnt=a
                        col[j]=a
                        ob.data.materials.append(mat)
                    else:
                    #Anterior en yb
                        if (matAnt in top_yb):
                            n=randint(0,len(bottom_yb)-1)
                            a=bottom_yb[n]
                            mat=texturas[a]
                            matAnt=a
                            col[j]=a
                            ob.data.materials.append(mat)
                        else:
                            #Anterior en yy
                            if (matAnt in top_yy):
                                n=randint(0,len(bottom_yy)-1)
                                a=bottom_yy[n]
                                mat=texturas[a]
                                matAnt=a
                                col[j]=a
                                ob.data.materials.append(mat)  
            #Para las otras filas             
            else:
                end=False
                elegibles=[]
                #Anterior Top BB and Rigth BB  check
                if (matAnt in top_bb and col[j] in rigth_bb and not end):
                    elegibles = list([0,1])
                    end=True
                    
                #Anterior Top BB and Rigth BY no tiene sentido
                if (matAnt in top_bb and col[j] in rigth_by and not end):
                    elegibles = list([0])
                    end=True
                    
                #Anterior Top BB and Rigth YB check
                if (matAnt in top_bb and col[j] in rigth_yb and not end):
                    elegibles = list([8,9])
                    end=True
                    
                #Anterior Top BB and Rigth YY no tiene sentiod
                if (matAnt in top_bb and col[j] in rigth_yy and not end):
                    elegibles = list([0])
                    end=True
                    
                #-----------------------------
                #Anterior Top BY and Rigth BB check
                if (matAnt in top_by and col[j] in rigth_bb and not end):
                    elegibles = list([2,3])
                    end=True
                    
                #Anterior Top BY and Rigth BY no debe llegar
                if (matAnt in top_by and col[j] in rigth_by and not end):
                    elegibles = list([0])
                    end=True
                    
                #Anterior Top BY and Rigth YB check
                if (matAnt in top_by and col[j] in rigth_yb and not end):
                    elegibles = list([10,11])
                    end=True
                    
                #Anterior Top BY and Rigth YY no tiene sentido
                if (matAnt in top_by and col[j] in rigth_yy and not end):
                    elegibles = list([0])
                    end=True
                    
                #------------------------------
                #Anterior Top YB and Rigth BB no debe llegar
                if (matAnt in top_yb and col[j] in rigth_bb and not end):
                    elegibles = list([0])
                    end=True
                    
                #Anterior Top YB and Rigth BY check
                if (matAnt in top_yb and col[j] in rigth_by and not end):
                    elegibles = list([4,5])
                    end=True
                    
                #Anterior Top YB and Rigth YB no debe llegar
                if (matAnt in top_yb and col[j] in rigth_yb and not end):
                    elegibles = list([0])
                    end=True
                    
                #Anterior Top YB and Rigth YY
                if (matAnt in top_yb and col[j] in rigth_yy and not end):
                    elegibles = list([12,13])
                    end=True
                    
                #------------------------------------
                #Anterior Top YY and Rigth BB and diag B no debe llegar
                if (matAnt in top_yy and col[j] in rigth_bb and not end):
                    elegibles = list([0])
                    end=True
                    
                #Anterior Top YY and Rigth BY check
                if (matAnt in top_yy and col[j] in rigth_by and not end):
                    elegibles = list([6,7])
                    end=True
                    
                #Anterior Top YY and Rigth YB no debe llegar
                if (matAnt in top_yy and col[j] in rigth_yb and not end):
                    elegibles = list([0])
                    end=True
                    
                #Anterior Top YY and Rigth YY
                if (matAnt in top_yy and col[j] in rigth_yy and not end):
                    elegibles = list([14,15])
                    end=True
                
                    
                n=randint(0,len(elegibles)-1)
                a=elegibles[n]
                mat=texturas[a]
                matAnt=a
                col[j]=a
                ob.data.materials.append(mat)
                #----------------------
            obs=[bpy.data.objects['Ground'],bpy.data.objects['Plane']]
            c = {}
            c["object"] = c["active_object"] = bpy.data.objects['Ground']
            c["selected_objects"] = c["selected_editable_objects"] = obs
            bpy.ops.object.join(c)
            ob =  bpy.data.objects['Ground']
            ob.name = "Ground"
            ob.data.name = "Ground"
                
                    
            
                
    first= False
                
                
                
