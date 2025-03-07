import bpy
import os
import mathutils
import math

def import_glb(filepath, context, operator):
    bpy.ops.import_scene.gltf(filepath=filepath, import_pack_images=False, disable_bone_shape=True)
    
    filename = os.path.splitext(os.path.basename(filepath))[0]
    mesh = None
    armature = None
    
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            mesh = obj
        elif obj.type == 'ARMATURE':
            armature = obj

            rotation_matrix = mathutils.Matrix.Rotation(math.radians(180), 4, 'Z')
            armature.matrix_world = rotation_matrix @ armature.matrix_world
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

            bpy.ops.object.mode_set(mode='EDIT')
            new_length = 0.01
            for bone in armature.data.edit_bones:
                bone.roll -= math.radians(90)
                bone_matrix = bone.matrix.to_3x3()
                x_axis = bone_matrix.col[0].normalized()
                rotation_matrix = mathutils.Matrix.Rotation(math.radians(90), 3, x_axis)
                bone.tail = bone.head + rotation_matrix @ (bone.tail - bone.head)

                # dirty hack to change the length of the bones (the whole thing is a dirty hack tbh)
                direction = (bone.tail - bone.head).normalized()
                bone.tail = bone.head + direction * new_length

                

            bpy.ops.object.mode_set(mode='OBJECT')

            armature.data.display_type = 'STICK'

    if mesh is not None:
        bpy.data.objects.remove(mesh)

    if armature is not None:
        operator.report({'INFO'}, "Import and conversion completed successfully.")
        return armature

    operator.report({'ERROR'}, "No valid object imported.")
    return None




