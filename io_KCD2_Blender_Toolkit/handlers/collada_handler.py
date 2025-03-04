import bpy
import bmesh
import math
import xml.etree.ElementTree as ET
import re
import os


def import_collada(filepath, context, operator):
    # Import the COLLADA file
    bpy.ops.wm.collada_import(filepath=filepath, custom_normals=operator.import_normals)
    filename = os.path.splitext(os.path.basename(filepath))[0]

    # Process imported meshes
    for obj in bpy.context.selected_objects:
        obj["mtl_directory"] = os.path.dirname(filepath)
        if obj.type == 'MESH':
            mesh = obj.data
            
            fix_material_slots(obj, filepath)
            set_smooth(mesh)
            create_export_node(operator) #only the export node so far

            break #only 1x mesh per import supported for now

    print(obj["mtl_directory"])
    operator.report({'INFO'}, "Import and conversion completed successfully.")
    return obj


def set_smooth(mesh):
    bm = bmesh.new()
    bm.from_mesh(mesh)

    for face in bm.faces:
        face.smooth = True
    
    bm.to_mesh(mesh)
    bm.free()

def get_matched_materials(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    ns = {'collada': 'http://www.collada.org/2005/11/COLLADASchema'}

    existing_materials = {mat.name: mat for mat in bpy.data.materials}
    
    return {
        mat_id.replace("-material", ""): existing_materials[mat_id.replace("-material", "")]
        for mat_id in (m.attrib.get('id') for m in root.findall('.//collada:material', ns))
        if mat_id.replace("-material", "") in existing_materials
    }

def fix_material_slots(obj, filepath): 
    if re.search('\.\d{3}$', obj.name):
        return

    matched_materials = get_matched_materials(filepath)

    # Store vertex material assignments
    material_vertex_map = {slot.name: [] for slot in obj.material_slots}
    for face in obj.data.polygons:
        material_vertex_map[obj.material_slots[face.material_index].name].append(face.index)

    # Add missing materials from the file
    for material in matched_materials.values():
        if material.name not in obj.material_slots:
            obj.data.materials.append(material)

    sorted_materials = sorted(obj.data.materials, key=lambda mat: int(mat.name.split('material')[-1]) if 'material' in mat.name else float('inf'))

    obj.data.materials.clear()
    for material in sorted_materials:
        obj.data.materials.append(material)

    for material_name, face_indices in material_vertex_map.items():
        new_material_index = obj.data.materials.find(material_name)
        
        for face_index in face_indices:
            obj.data.polygons[face_index].material_index = new_material_index

def create_export_node(operator):
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            bpy.context.view_layer.objects.active = obj  # Set active object
            bpy.ops.object.select_all(action='DESELECT')  # Deselect all
            obj.select_set(True)

            for child in obj.children_recursive:
                child.select_set(True)
    
    model_type = operator.model_type
    if model_type != "":
        bpy.ops.bcry.add_cry_export_node(node_type=model_type)