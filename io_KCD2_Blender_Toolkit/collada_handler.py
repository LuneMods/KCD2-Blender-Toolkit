import bpy
import bmesh
import math

def import_collada(filepath, context, operator):
    # Import the COLLADA file
    bpy.ops.wm.collada_import(filepath=filepath)

    # Process imported meshes
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            mesh = obj.data

            # Ensure the mesh has vertex colors
            if mesh.vertex_colors:
                vc_layer = mesh.vertex_colors.active  # Get active vertex color layer
                new_layer = mesh.color_attributes.new(name="alpha", type='BYTE_COLOR', domain='CORNER')  

                bm = bmesh.new()
                bm.from_mesh(mesh)
                bm.loops.layers.color.verify()
                color_layer = bm.loops.layers.color.get(vc_layer.name)
                new_color_layer = bm.loops.layers.color.get(new_layer.name)

                # Copy alpha channel to the new color attribute
                for face in bm.faces:
                    for loop in face.loops:
                        original_color = loop[color_layer]
                        alpha = original_color[3]  # Extract alpha value
                        rounded_alpha = alpha * 0.255
                        loop[new_color_layer] = (rounded_alpha, 0, 0, 1)  # Store alpha in RGBA, full opacity in A

                bm.to_mesh(mesh)
                bm.free()

            else:
                operator.report({'WARNING'}, f"Skipping {obj.name}, no vertex colors found.")

    operator.report({'INFO'}, "Import and conversion completed successfully.")
    return {'FINISHED'}
