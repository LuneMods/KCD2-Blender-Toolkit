import bpy
import xml.etree.ElementTree as ET
from bpy.types import PropertyGroup
from bpy.props import StringProperty, IntProperty, FloatProperty

class ItemProps_LongSword(PropertyGroup):
    item_name: StringProperty(name="Name", default="NewLongsword")
    attack: IntProperty(name="Attack", default=200, min=0)
    defense_stab: IntProperty(name="Defense Stab", default=200, min=0)
    defense: IntProperty(name="Defense", default=124, min=0)
    str_req: IntProperty(name="Strength Req", default=18, min=0)
    agi_req: IntProperty(name="Agility Req", default=12, min=0)
    max_quality: IntProperty(name="Max Quality", default=4, min=1, max=10)
    weight: FloatProperty(name="Weight", default=3.0, min=0.0)
    price: IntProperty(name="Price", default=5000, min=0)


class Generate_LongSword:
    def __init__(self, props, item_classes):
        self.props = props
        self.item_classes = item_classes
        self.generate_weapon_xml()

    def generate_weapon_xml(self):
        ET.SubElement(self.item_classes, "MeleeWeapon", {
            "Attack": str(self.props.attack),
            "AttackModStab": "1.05",
            "AttackModSlash": "1",
            "AttackModSmash": "0.2",
            "Class": "4",
            "Defense": str(self.props.defense),
            "MaxStatus": "200",
            "StrReq": str(self.props.str_req),
            "AgiReq": str(self.props.agi_req),
            "IsBreakable": "true",
            "BrokenItemClassId": "caa97b58-3bf5-4b99-8281-0c0c4edc082f",
            "Visibility": "1",
            "Conspicuousness": "1",
            "Charisma": "5",
            "SocialClassId": "0",
            "WealthLevel": "0",
            "MaxQuality": str(self.props.max_quality),
            "Clothing": "Scabbard_LongSword02",
            "IconId": self.props.item_name,
            "UIInfo": f"ui_in_{self.props.item_name}",
            "UIName": f"ui_nm_{self.props.item_name}",
            "Model": f"manmade/weapons/swords_long/{self.props.item_name}.cgf",
            "Weight": str(self.props.weight),
            "Price": str(self.props.price),
            "FadeCoef": "1",
            "VisibilityCoef": "13.0153751",
            "Id": "3858560f-cf48-436f-8815-4426003288fb",
            "Name": self.props.item_name
        })