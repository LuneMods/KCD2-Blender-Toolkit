import bpy
import bmesh

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
                new_layer = mesh.color_attributes.new(name="Alpha", type='BYTE_COLOR', domain='CORNER')  

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
                        loop[new_color_layer] = (alpha, alpha, alpha, 1.0)  # Store alpha in RGB, full opacity in A

                bm.to_mesh(mesh)
                bm.free()

                # Remove non-alpha color layers
                for layer in mesh.color_attributes:
                    if layer.name != "Alpha":
                        mesh.color_attributes.remove(layer)
                        break

            else:
                operator.report({'WARNING'}, f"Skipping {obj.name}, no vertex colors found.")

    operator.report({'INFO'}, "Import and conversion completed successfully.")
    return {'FINISHED'}
