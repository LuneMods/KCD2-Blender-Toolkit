import bpy

# Base class for the panel
class UI_BasePanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "KCD2 Toolkit"


class UI_Import(UI_BasePanel):
    bl_label = "Import KCD2 Asset"
    bl_idname = "KCD2_PT_Import"

    def draw(self, context):
        layout = self.layout
        # Import Collada (.dae)
        layout.operator("import_scene.kcd2_collada", text="Import COLLADA (.dae)")

        # Import Skin (.skin)
        layout.operator("import_scene.kcd2_skin", text="Import Skin (.skin)")

        # Import CGF (.cgf)
        layout.operator("import_scene.kcd2_cgf", text="Import CGF (.cgf)")

def register():
    bpy.utils.register_class(UI_Import)

def unregister():
    bpy.utils.unregister_class(UI_Import)