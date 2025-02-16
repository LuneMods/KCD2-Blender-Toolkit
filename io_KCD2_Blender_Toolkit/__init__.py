bl_info = {
    "name": "KCD2 Blender Toolkit",
    "author": "Lune",
    "version": (1, 0),
    "blender": (4, 3, 0),
    "location": "File > Import",
    "description": "A toolkit for working with KCD2 Assets",
    "category": "Import-Export",
}

import bpy
import bmesh
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty

class ImportKCD2Collada(bpy.types.Operator, ImportHelper):
    """Import KCD2 Collada"""
    bl_idname = "import_scene.kcd2_collada"
    bl_label = "Import KCD2 COLLADA file (.dae)"
    bl_options = {'REGISTER', 'UNDO'}
    
    filename_ext = ".dae"
    filter_glob: StringProperty(default="*.dae", options={'HIDDEN'}, maxlen=255)

    def execute(self, context):

        # Import the COLLADA file
        bpy.ops.wm.collada_import(filepath=self.filepath)

        # Process imported meshes
        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH':
                mesh = obj.data

                # Ensure the mesh has vertex colors
                if mesh.vertex_colors:
                    vc_layer = mesh.vertex_colors.active  # Get active vertex color layer
                    new_layer = mesh.color_attributes.new(name="Alpha_Channel", type='BYTE_COLOR', domain='CORNER')  

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
                else:
                    self.report({'WARNING'}, f"Skipping {obj.name}, no vertex colors found.")

        self.report({'INFO'}, "Import and conversion completed successfully.")
        return {'FINISHED'}

def menu_func_import(self, context):
    self.layout.operator(ImportKCD2Collada.bl_idname, text="Import KCD2 COLLADA file (.dae)")

def register():
    bpy.utils.register_class(ImportKCD2Collada)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(ImportKCD2Collada)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)

if __name__ == "__main__":
    register()
