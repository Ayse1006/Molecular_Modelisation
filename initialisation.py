import bpy
from bpy.props import *

#Clearing of the scene
def clear():
    #gather list of item of interest
    bpy.ops.object.mode_set(mode = 'OBJECT')
    candidate_list = [item.name for item in bpy.data.objects if item.type =="MESH"]
    #select them only
    for object_name in candidate_list : 
        bpy.data.objects[object_name].select = True
    #remove all selected.
    bpy.ops.object.delete()
    #remove the meshes, they have no users anymors.
    for bpy_data_iter in (
        bpy.data.objects,
        bpy.data.meshes,
        bpy.data.lamps,
        bpy.data.cameras,
    ):
        for item in bpy_data_iter:
            bpy_data_iter.remove(item)

#Initiation of the scene with camera and lamp in the good directions
def initiation():
    #Create camera
    bpy.ops.object.camera_add(view_align = True, location=(10,10,15), rotation=(-1,0,-1))
    #Create lamp 
    bpy.ops.object.lamp_add(type='POINT', location=(-10,-10,15))
    print("Camera and lamp ok!")
    
def addSphere(xl,yl,zl,xs,ys,zs,name):
    bpy.ops.mesh.primitive_uv_sphere_add(location=(xl,yl,zl))
    bpy.ops.transform.resize(value=(xs, ys, zs))
    
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name) #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (1, 0, 0) #change color
    
def addCube(xl,yl,zl,xs,ys,zs,name):
    bpy.ops.mesh.primitive_cube_add(location=(xl,yl,zl))
    bpy.ops.transform.resize(value=(xs, ys, zs))
    bpy.context.object.show_transparent = True
    
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name) #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0.002,0.8,0.029) #change color
    bpy.context.object.active_material.use_transparency = True
    bpy.context.object.active_material.alpha = 0.5

    if(bpy.context.active_object.name == "Cube.001"):
        select([6,0])

def select(indexes):
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
    bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.object.editmode_toggle()
    obj = bpy.context.active_object
    for index in indexes:
        obj.data.polygons[index].select = True


    
def addPlane(xl,yl,zl,xs,ys,name):
    bpy.ops.mesh.primitive_plane_add(location=(xl,yl,zl))
    bpy.ops.transform.resize(value=(xs, ys, 1))
    bpy.context.object.rotation_euler[0] = 1.5708
    
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialName") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0, 0, 1) #change color


if __name__ == "__main__":
    clear()
    initiation()
    addSphere(-1.6,-1.9,4,1,0.5,0.5,"Mat0")
    addCube(-6,0,4,1,3.5,1, "Mat1")
    addCube(-2.5,-2,4,3.5,1,1, "Mat2")
    addPlane(-6.1,3.4,4,0.8,0.8,"Mat3")

    
    