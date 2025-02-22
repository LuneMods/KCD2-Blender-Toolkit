import bpy
import xml.etree.ElementTree as ET

class ItemProps_ShortSword:
    name = "Shortsword"
    attack = 80
    defense = 100
    str_req = 8
    agi_req = 12
    max_quality = 4
    weight = 1.6
    price = 2400

class Generate_ShortSword:
    def __init__(self, props, item_classes):
        self.props = props
        self.item_classes = item_classes
        self.generate_weapon_xml()

    def generate_weapon_xml(self):
        ET.SubElement(self.item_classes, "MeleeWeapon", {
            "Attack": str(self.props.attack),
            "AttackModStab": "0.95",
            "AttackModSlash": "1",
            "AttackModSmash": "0.15",
            "Class": "1",
            "Defense": str(self.props.defense),
            "MaxStatus": "58",
            "StrReq": str(self.props.str_req),
            "AgiReq": str(self.props.agi_req),
            "IsBreakable": "true",
            "BrokenItemClassId": "a912b643-04c2-4e56-802f-10060d4fdde5",
            "Visibility": "1",
            "Conspicuousness": "1",
            "Charisma": "5",
            "SocialClassId": "0",
            "WealthLevel": "0",
            "MaxQuality": str(self.props.max_quality),
            "Clothing": "Scabbard_ShortSword02",
            "IconId": self.props.name.lower(),
            "UIInfo": f"ui_in_{self.props.name.lower()}",
            "UIName": f"ui_nm_{self.props.name.lower()}",
            "Model": f"manmade/weapons/swords_short/{self.props.name.lower()}.cgf",
            "Weight": str(self.props.weight),
            "Price": str(self.props.price),
            "FadeCoef": "1",
            "VisibilityCoef": "10.20784",
            "Id": "efa237c7-3905-4813-b9c3-a32b449c17ad",
            "Name": self.props.name
        })
