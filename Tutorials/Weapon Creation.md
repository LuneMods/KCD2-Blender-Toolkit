<!-- Creating Weapons -->
## Creating Weapons

This is a basic tutorial for how to create a new weapon model for Kingdom Come Deliverance 2.
It assumes you are somewhat familiar with blender/3d modelling, and uses the Longsword_Template.blend template.
Ensure you are using the latest version of the KCD2 Blender Toolkit.


### Overview

In the Longsword_Template.blend you will find an example of how a weapon should be set up in blender.

<img src="images/1. Scene Setup.png">

The models that will be exported are in the `cry_export_nodes` Collection.
The `WeaponName.cgf` collection inside `cry_export_nodes` is what will be exported in the final .CGF file.
There can be multiple .CGF files inside 1 .blend file, but i highly recommend only having 1 model per file.

inside `WeaponName.cgf` you will find the main model `Longsword` which has 6x Empties parented to it.
These are the `slots` which dictate the location of contact/alignment positions on the mesh.
unless you know what you are doing, you should not change the rotation or location of these at all.
They must be parented to the mesh, and NOT have their transforms applied.
You can delete the `Longsword` object, but ensure that you re-parent all of the `slots` to the new model using `ctrl+p` > `Object (Keep Transform)`

The `capsuleproxy's` are ?hitboxes? & physics proxies which determine the collisions of the weapon.
It is best practice to resize these in Edit Mode to suit your weapon.
If you need to create more, use the `Add Physics Proxy` feature in the `BCry Exporter` tab.

The `Longsword` & `capsuleproxy` objects must have their transforms applied (`ctrl+A`), so that the origin of the model is at 0,0,0 (which is the same location as `slt_0`)

<img src="images/Physics Proxies.png">

The hands in the `helpers` collection are just to assist you in lining up your model, and will not be exported.

Once you are ready to export your model, use the `Export to CryEngine` button in the `BCry Exporter` tab.

<img src="images/Export Button.png">