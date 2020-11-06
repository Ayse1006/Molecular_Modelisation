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
    #Init Mcell
    bpy.ops.mcell.init_cellblender()
    bpy.context.scene.mcell.cellblender_main_panel.preferences_select = True
    bpy.ops.mcell.init_cellblender()
    bpy.ops.mcell.preferences_save(name="Cb")
    bpy.ops.mcell.set_mcell_binary(filepath="/Users/marlenebarus/Master2/StrubiGL/mcell_3.4_osx")
 
def select(indexes):
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
    bpy.ops.mesh.select_all(action='TOGGLE')
    obj = bpy.context.active_object
    bpy.ops.object.editmode_toggle()
    for index in indexes:
        obj.data.polygons[index].select = True
    
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

    
def addPlane(xl,yl,zl,xs,ys,name):
    bpy.ops.mesh.primitive_plane_add(location=(xl,yl,zl))
    bpy.ops.transform.resize(value=(xs, ys, 1))
    bpy.context.object.rotation_euler[0] = 1.5708
    bpy.context.object.rotation_euler[2] = 1.5708

    
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialName") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0, 0, 1) #change color

def modelObjects(name):
    bpy.ops.mcell.model_objects_add()
    bpy.context.object.name = name
    
    if(bpy.context.active_object.name == "Cube01"):
        select([8,2])
        bpy.ops.object.editmode_toggle()
        bpy.ops.mcell.region_add()
        bpy.context.object.mcell.regions.region_list[0].name = "Open1"
        bpy.ops.mcell.region_faces_assign()
        bpy.ops.object.editmode_toggle()
    
    if(bpy.context.active_object.name == "Cube02"):
        select([6,0])
        bpy.ops.object.editmode_toggle()
        bpy.ops.mcell.region_add()
        bpy.context.object.mcell.regions.region_list[0].name = "Open2"
        bpy.ops.mcell.region_faces_assign()
        bpy.ops.object.editmode_toggle()
        
    if(bpy.context.active_object.name == "Sphere"):
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
        bpy.ops.mcell.region_add()
        bpy.context.object.mcell.regions.region_list[0].name = "Open3"
        bpy.ops.mcell.region_faces_assign()
        bpy.ops.object.editmode_toggle()
        
        
def parameters(name,expr):
    bpy.ops.mcell.add_parameter()
    bpy.context.scene.mcell.parameter_system.active_name = name
    bpy.context.scene.mcell.parameter_system.active_expr = expr
    
def molecules(i,name,type,diffusion,x):
    bpy.ops.mcell.molecule_add()
    bpy.context.scene.mcell.molecules.molecule_list[i].name = name
    bpy.context.scene.mcell.molecules.molecule_list[i].type = type
    bpy.context.scene.mcell.parameter_system.panel_parameter_list[x].expr = diffusion

def surfaceClasses(index, name, object, region_name):
    bpy.ops.mcell.surface_class_add()
    bpy.context.scene.mcell.surface_classes.surf_class_list[index].name = name
    bpy.ops.mcell.surf_class_props_add()
    bpy.context.scene.mcell.surface_classes.surf_class_list[index].surf_class_props_list[0].affected_mols = 'ALL_VOLUME_MOLECULES'
    bpy.context.scene.mcell.surface_classes.surf_class_list[index].surf_class_props_list[0].surf_class_type = 'TRANSPARENT'
    bpy.ops.mcell.mod_surf_regions_add()
    bpy.context.scene.mcell.mod_surf_regions.mod_surf_regions_list[index].surf_class_name = name
    bpy.context.scene.mcell.mod_surf_regions.mod_surf_regions_list[index].object_name = object
    bpy.context.scene.mcell.mod_surf_regions.mod_surf_regions_list[index].region_selection = 'SEL'
    bpy.context.scene.mcell.mod_surf_regions.mod_surf_regions_list[index].region_name = region_name

def reaction(index1, reactants, products, rate, index2):
    bpy.ops.mcell.reaction_add()
    bpy.context.scene.mcell.reactions.reaction_list[index1].reactants = reactants
    bpy.context.scene.mcell.reactions.reaction_list[index1].products = products
    bpy.context.scene.mcell.parameter_system.panel_parameter_list[index2].expr = rate
    
def releaseSites(index1, name, molecule, object, quantity, index2):
    bpy.ops.mcell.release_site_add()
    bpy.context.scene.mcell.release_sites.mol_release_list[index1].name = name
    bpy.context.scene.mcell.release_sites.mol_release_list[index1].molecule = molecule
    bpy.context.scene.mcell.release_sites.mol_release_list[index1].shape = 'OBJECT'
    bpy.context.scene.mcell.release_sites.mol_release_list[index1].object_expr = object
    bpy.context.scene.mcell.parameter_system.panel_parameter_list[index2].expr = quantity

def reactionProducts(index, name):
    bpy.ops.mcell.rxn_output_add()
    bpy.context.scene.mcell.rxn_output.rxn_output_list[index].molecule_name = name

def runSimulation():
    bpy.context.scene.mcell.parameter_system.panel_parameter_list[0].expr = "iters"
    bpy.context.scene.mcell.parameter_system.panel_parameter_list[1].expr = "dt"
    bpy.context.scene.mcell.initialization.warnings = True
    bpy.context.scene.mcell.initialization.all_warnings = 'WARNING'



if __name__ == "__main__":
    clear()
    initiation()
    addSphere(-1.6,-1.9,4,1,0.5,0.5,"Mat0")
    modelObjects("Sphere")
    addCube(-6,-2,4,1,1.03,0.81, "Mat1")
    modelObjects("Cube01")
    addCube(-2.5,-2,4,3.5,1,0.8, "Mat2")
    modelObjects("Cube02")
    addPlane(-6.95,-2,4,0.8,0.8,"Mat3")
    modelObjects("Plane")
    parameters("iters","1500")
    parameters("dt","1e-5")
    parameters("dn","1e-4")
    parameters("di","1e-5")
    parameters("dc","1e-4")
    parameters("dr","1e-6")
    parameters("fwd_rc","1e8")
    parameters("nb_nt","2000")
    parameters("nb_i","4000")
    parameters("nb_rf","1500")
    molecules(0,"Neurotransmetteur","3D","dn",17)
    molecules(1,"Ion","3D","di",21)
    molecules(2,"Recepteur_ferme","2D","dr",25)
    molecules(3,"Cplx","3D","dc",29)
    molecules(4,"Recepteur_ouvert","2D","dr",33)
    surfaceClasses(0, "passage1", "Cube01", "Open1")
    surfaceClasses(1, "passage2", "Cube02", "Open2")
    surfaceClasses(2, "passage3", "Sphere", "Open3")
    reaction(0, "Neurotransmetteur + Ion", "Cplx", "fwd_rc", 40)
    reaction(1, "Cplx; + Recepteur_ferme,", "Recepteur_ouvert,", "fwd_rc", 42)
    releaseSites(0, "Release_Site_1", "Ion", "Cube02", "nb_i", 49)
    releaseSites(1, "Release_Site_2", "Neurotransmetteur", "Sphere", "nb_nt", 56)
    releaseSites(2, "Release_Site_3", "Recepteur_ferme", "Plane", "nb_rf", 63)
    reactionProducts(0, "Neurotransmetteur")
    reactionProducts(1, "Ion")
    reactionProducts(2, "Recepteur_ferme")
    reactionProducts(3, "Cplx")
    reactionProducts(4, "Recepteur_ouvert")
    runSimulation()
