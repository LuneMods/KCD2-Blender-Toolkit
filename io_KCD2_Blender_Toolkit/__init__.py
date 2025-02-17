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
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty
from . import collada_handler, skin_handler

class ImportKCD2ColladaOperator(bpy.types.Operator, ImportHelper):
    """Import KCD2 Collada"""
    bl_idname = "import_scene.kcd2_collada"
    bl_label = "Import KCD2 COLLADA file (.dae)"
    bl_options = {'REGISTER', 'UNDO'}
    
    filename_ext = ".dae"
    filter_glob: StringProperty(default="*.dae", options={'HIDDEN'}, maxlen=255)

    def execute(self, context):
        return collada_handler.import_collada(self.filepath, context, self)

class ImportKCD2SkinOperator(bpy.types.Operator, ImportHelper):
    """Import KCD2 Skin"""
    bl_idname = "import_scene.kcd2_skin"
    bl_label = "Import KCD2 Skin file (.skin)"
    bl_options = {'REGISTER', 'UNDO'}
    
    filename_ext = ".skin"
    filter_glob: StringProperty(default="*.skin", options={'HIDDEN'}, maxlen=255)

    def execute(self, context):
        skin_filepath = self.filepath

        try:
            #convert the skin to dae
            dae_filepath = skin_handler.skin_to_dae(skin_filepath)
            self.report({'INFO'}, "Converting Skin to dae...")
            if not dae_filepath:
                raise Exception("Failed to Convert Skin to dae")
            
            #then import the dae
            collada_handler.import_collada(dae_filepath, context, self)
            self.report({'INFO'}, "Model imported successfully.")
            
        except Exception as e:
            self.report({'ERROR'}, f"Import failed: {e}")
            return {'CANCELLED'}

        return {'FINISHED'}

def menu_func_import(self, context):
    self.layout.operator(ImportKCD2ColladaOperator.bl_idname, text=ImportKCD2ColladaOperator.bl_label)
    self.layout.operator(ImportKCD2SkinOperator.bl_idname, text=ImportKCD2SkinOperator.bl_label)

def register():
    bpy.utils.register_class(ImportKCD2ColladaOperator)
    bpy.utils.register_class(ImportKCD2SkinOperator)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(ImportKCD2ColladaOperator)
    bpy.utils.unregister_class(ImportKCD2SkinOperator)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)

if __name__ == "__main__":
    register()
