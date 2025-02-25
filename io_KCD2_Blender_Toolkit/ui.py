import bpy
import os

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
        layout.operator("import_scene.kcd2_collada", text="Import COLLADA (.dae)")
        layout.operator("import_scene.kcd2_skin", text="Import Skin (.skin)")
        layout.operator("import_scene.kcd2_cgf", text="Import CGF (.cgf)")


class UI_Materials(UI_BasePanel):
    bl_label = "Materials"
    bl_idname = "KCD2_PT_Materials"

    def draw(self, context):
        layout = self.layout
        selected_obj = context.active_object

        if selected_obj and selected_obj.type == 'MESH' and "mtl_directory" in selected_obj:
            mtl_directory = selected_obj["mtl_directory"]
            if mtl_directory:
                try:
                    files = [f for f in os.listdir(mtl_directory) if f.endswith('.mtl')]
                except FileNotFoundError:
                    files = []
                
                if files:
                    layout.prop(context.scene, "mtl_file_dropdown", text="Select MTL File")
                else:
                    layout.label(text="No .mtl files found")
            else:
                layout.label(text="No mtl_directory found")
        else:
            layout.label(text="No mesh selected or mtl_directory not found")

        layout.operator("mtl.load_mtl", text="Load Material")


def update_mtl_files(self, context):
    selected_obj = context.active_object
    if selected_obj and selected_obj.type == 'MESH' and "mtl_directory" in selected_obj:
        mtl_directory = selected_obj["mtl_directory"]
        if os.path.exists(mtl_directory):
            try:
                files = [
                    (os.path.join(mtl_directory, f), f, "") 
                    for f in os.listdir(mtl_directory) if f.endswith('.mtl')
                ]
                return files if files else [("NO_FILE", "No .mtl files found", "")]
            
            except FileNotFoundError:
                print("Error: mtl_directory not found.")
                return [("NO_FILE", "No .mtl files found", "")]
    return [("NO_FILE", "No .mtl files found", "")]


def register_properties():
    bpy.types.Scene.mtl_file_path = bpy.props.StringProperty(
        name=".mtl File",
        description="Path to the .mtl file",
        subtype='FILE_PATH'
    )

    bpy.types.Scene.selected_mesh = bpy.props.PointerProperty(
        name="Mesh",
        description="Select a mesh to apply the materials to",
        type=bpy.types.Object,
        poll=lambda self, obj: obj.type == 'MESH'
    )

    bpy.types.Scene.mtl_file_dropdown = bpy.props.EnumProperty(
        name="MTL Files",
        description="Select a Material file",
        items=update_mtl_files
    )


def unregister_properties():
    del bpy.types.Scene.mtl_file_path
    del bpy.types.Scene.selected_mesh
    del bpy.types.Scene.mtl_file_dropdown


def register():
    register_properties()
    for cls in [UI_Import, UI_Materials]:
        bpy.utils.register_class(cls)


def unregister():
    for cls in [UI_Import, UI_Materials]:
        bpy.utils.unregister_class(cls)
    unregister_properties()
