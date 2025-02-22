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
from bpy.types import AddonPreferences, PropertyGroup
from bpy.props import StringProperty, IntProperty, FloatProperty, EnumProperty
from . import importers, ui

class AddonSettings(AddonPreferences):
    bl_idname = __name__

    filepath: StringProperty(
        name="KCD2 Data Directory",
        description="The folder of the extracted .paks",
        subtype='FILE_PATH',
        default=""
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "filepath")

modules = [importers, ui]
classes = [AddonSettings]

def register():
    for module in modules:
        module.register()
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for module in reversed(modules):
        module.unregister()
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()