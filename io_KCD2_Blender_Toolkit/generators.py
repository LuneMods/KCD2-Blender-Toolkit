import bpy
from bpy.types import Operator, Panel, PropertyGroup
from bpy.props import StringProperty, IntProperty, FloatProperty, PointerProperty, EnumProperty
import xml.etree.ElementTree as ET
from xml.dom import minidom
from bpy_extras.io_utils import ExportHelper
from .xml.weapons.LongSword import *
from .ui import UI_BasePanel

class ItemProps_Helmet(PropertyGroup):
    item_name: StringProperty(name="Name", default="New Helmet")
    attack: IntProperty(name="Attack", default=200, min=0)
    defense: IntProperty(name="Defense", default=150, min=0)
    str_req: IntProperty(name="Strength Req", default=18, min=0)
    agi_req: IntProperty(name="Agility Req", default=12, min=0)
    max_quality: IntProperty(name="Max Quality", default=4, min=1, max=10)
    weight: FloatProperty(name="Weight", default=3.0, min=0.0)
    price: IntProperty(name="Price", default=5000, min=0)
    noise: IntProperty(name="Noise", default=5000, min=0)

class ItemProps_Shield(PropertyGroup):
    block_power: IntProperty(name="Block Power", default=300, min=0)
    defense: IntProperty(name="Defense", default=200, min=0)


class ItemProps_Bow(PropertyGroup):
    range: IntProperty(name="Range", default=100, min=0)
    draw_strength: IntProperty(name="Draw Strength", default=50, min=0)


# Function to generate the item XML
def generate_item_xml(props, item_type):
    """Generate XML data for the given item properties."""
    # Create the root element
    root = ET.Element("database", {
        "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "name": "barbora",
        "xsi:noNamespaceSchemaLocation": "item.xsd"
    })

    # Create the ItemClasses element
    item_classes = ET.SubElement(root, "ItemClasses", {"version": "8"})

    # Generate the weapon-specific XML based on the item_type
    if item_type == 'LONGSWORD':
        Generate_LongSword(props, item_classes)
    elif item_type == 'HELMET':
        Generate_LongSword(props, item_classes)
    else:
        raise ValueError("Unsupported weapon type")

    # Convert the XML tree to a string
    xml_str = ET.tostring(root, encoding="us-ascii", xml_declaration=True)

    # Pretty-print the XML
    formatted_xml = format_xml(xml_str)

    return formatted_xml


def format_xml(xml_str):
    """Format the XML string with proper indentation and line breaks."""
    # Parse the XML string
    parsed_xml = minidom.parseString(xml_str)
    # Pretty-print the XML
    pretty_xml = parsed_xml.toprettyxml(indent="    ", encoding="us-ascii")
    # Decode the bytes to a string
    return pretty_xml.decode("us-ascii")


# Operator to create the selected item
class OBJECT_OT_create_item(bpy.types.Operator, ExportHelper):
    bl_idname = "object.create_item"
    bl_label = "Export Item"
    bl_options = {'REGISTER', 'UNDO'}

    # Filepath property for saving the XML
    filename_ext = ".xml"
    filter_glob: StringProperty(
        default="*.xml",
        options={'HIDDEN'},
    )

    def execute(self, context):
        scene = context.scene
        item_type = scene.item_type

        # Get the properties for the selected item type
        props = getattr(scene, f"item_props_{item_type.lower()}")
        
        xml_data = generate_item_xml(props, item_type)

        # Save XML to file
        file_path = self.filepath  # This is the path selected by the user through the file browser
        with open(file_path, "w", encoding="us-ascii") as file:
            file.write(xml_data)

        self.report({'INFO'}, f"XML exported to {file_path}")

        """ obj = context.object
        obj.name = props.item_name

        # Store all properties in the object
        for prop_name in props.__annotations__:
            obj[prop_name] = getattr(props, prop_name) """

        return {'FINISHED'}

# Panel for the addon
class UI_Create_Item(UI_BasePanel):
    bl_label = "Export Item"
    bl_idname = "KCD2_PT_CreateItem"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Dropdown to select item type
        layout.prop(scene, "item_type", text="Item Type")

        # Display properties based on the selected item type
        props = getattr(scene, f"item_props_{scene.item_type.lower()}")
        for prop_name in props.__annotations__:
            layout.prop(props, prop_name)

        # Button to create the item
        layout.operator("object.create_item")


# Register classes and properties
classes = (
    ItemProps_LongSword,
    ItemProps_Helmet,
    ItemProps_Shield,
    ItemProps_Bow,
    OBJECT_OT_create_item,
    UI_Create_Item
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # Add properties to the scene
    bpy.types.Scene.item_props_longsword = PointerProperty(type=ItemProps_LongSword)
    bpy.types.Scene.item_props_helmet = PointerProperty(type=ItemProps_Helmet)
    bpy.types.Scene.item_props_shield = PointerProperty(type=ItemProps_Shield)
    bpy.types.Scene.item_props_bow = PointerProperty(type=ItemProps_Bow)
    # Add more properties as needed...

    # Add item type enum property
    bpy.types.Scene.item_type = EnumProperty(
        name="Item Type",
        items=[
            ('LONGSWORD', "Long Sword", "Create a Long Sword"),
            ('HELMET', "Helmet", "Create a Helmet"),
            ('SHIELD', "Shield", "Create a Shield"),
            ('BOW', "Bow", "Create a Bow"),
            # Add more item types here...
        ],
        default='LONGSWORD',
    )


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    # Remove properties from the scene
    del bpy.types.Scene.item_props_longsword
    del bpy.types.Scene.item_props_helmet
    del bpy.types.Scene.item_props_shield
    del bpy.types.Scene.item_props_bow
    # Remove more properties as needed...
    del bpy.types.Scene.item_type