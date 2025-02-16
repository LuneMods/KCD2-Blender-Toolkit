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
from . import collada_handler  # Import the logic from another script

class ImportKCD2ColladaOperator(bpy.types.Operator, ImportHelper):
    """Import KCD2 Collada"""
    bl_idname = "import_scene.kcd2_collada"
    bl_label = "Import KCD2 COLLADA file (.dae)"
    bl_options = {'REGISTER', 'UNDO'}
    
    filename_ext = ".dae"
    filter_glob: StringProperty(default="*.dae", options={'HIDDEN'}, maxlen=255)

    def execute(self, context):
        return collada_handler.import_collada(self.filepath, context, self)

def menu_func_import(self, context):
    self.layout.operator(ImportKCD2ColladaOperator.bl_idname, text="Import KCD2 COLLADA file (.dae)")

def register():
    bpy.utils.register_class(ImportKCD2ColladaOperator)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(ImportKCD2ColladaOperator)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)

if __name__ == "__main__":
    register()
