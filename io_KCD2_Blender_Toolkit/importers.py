import bpy
import bmesh
import math
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty
from .handlers import cgf_handler, skin_handler, collada_handler


class Importer_KCD2_Collada(bpy.types.Operator, ImportHelper):
    """Import KCD2 Collada"""
    bl_idname = "import_scene.kcd2_collada"
    bl_label = "Import KCD2 COLLADA file (.dae)"
    bl_options = {'REGISTER', 'UNDO'}
    
    filename_ext = ".dae"
    filter_glob: StringProperty(default="*.dae", options={'HIDDEN'}, maxlen=255)

    def execute(self, context):
        return collada_handler.import_collada(self.filepath, context, self)


class Importer_KCD2_SKIN(bpy.types.Operator, ImportHelper):
    """Import KCD2 Skin"""
    bl_idname = "import_scene.kcd2_skin"
    bl_label = "Import KCD2 Skin file (.skin)"
    bl_options = {'REGISTER', 'UNDO'}
    
    filename_ext = ".skin"
    filter_glob: StringProperty(default="*.skin", options={'HIDDEN'}, maxlen=255)

    def execute(self, context):
        skin_filepath = self.filepath

        try:
            dae_filepath = skin_handler.skin_to_dae(skin_filepath)
            self.report({'INFO'}, "Converting Skin to dae...")
            if not dae_filepath:
                raise Exception("Failed to Convert Skin to dae")
            
            collada_handler.import_collada(dae_filepath, context, self)
            self.report({'INFO'}, "Model imported successfully.")
            
        except Exception as e:
            self.report({'ERROR'}, f"Import failed: {e}")
            return {'CANCELLED'}

        return {'FINISHED'}
    

class Importer_KCD2_CGF(bpy.types.Operator, ImportHelper):
    """Import KCD2 CGF"""
    bl_idname = "import_scene.kcd2_cgf"
    bl_label = "Import KCD2 CGF file (.cgf)"
    bl_options = {'REGISTER', 'UNDO'}
    
    filename_ext = ".cgf"
    filter_glob: StringProperty(default="*.cgf", options={'HIDDEN'}, maxlen=255)
    
    def execute(self, context):
        skin_filepath = self.filepath

        try:
            dae_filepath = cgf_handler.cgf_to_dae(skin_filepath)
            self.report({'INFO'}, "Converting cgf to dae...")
            if not dae_filepath:
                raise Exception("Failed to Convert CGF to dae")
            
            collada_handler.import_collada(dae_filepath, context, self)
            self.report({'INFO'}, "Model imported successfully.")
            
        except Exception as e:
            self.report({'ERROR'}, f"Import failed: {e}")
            return {'CANCELLED'}

        return {'FINISHED'}

# === Registration ===
classes = (
    Importer_KCD2_Collada,
    Importer_KCD2_SKIN,
    Importer_KCD2_CGF
)

def register():
    for cls in classes:
        if not hasattr(bpy.types, cls.__name__):
            bpy.utils.register_class(cls)
    

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
