This is my WIP blender toolkit for working with KCD2 files in Blender 4.3.

The repo contains the `KCD2 Toolkit` blender addon and a custom branch of the `BCry Exporter` Addon, so make sure you remove the original addon if you have it installed.
This will (hopefully) be updated regularly, as I add/fix things.

Copy the `io_KCD2_Blender_Toolkit` & `io_bcry_exporter` files to the blender addon directory, \
usually found at: `\AppData\Roaming\Blender Foundation\Blender\4.3\scripts\addons`

You can find the Import tool in the right hand tools panel, alongside BCry Exporter. Toggle this with `N` if you cant see it.

Tutorials/Documentation: https://github.com/LuneMods/KCD2-Blender-Toolkit/tree/main/Tutorials

Templates: https://github.com/LuneMods/KCD2-Blender-Toolkit/tree/main/Templates

Current features:
- Directly importing .skin & .cgf files
- Vertex Colors (RGB and Alpha layers)
- Exporting to .skin & .cgf using a custom branch of BCry Exporter

I have tested creating the following Assets & can confirm that they work (mostly):
- Weapons
- Helmets (need to modify the visor bone roll -180 deg in edit mode)
- Clothing
- Body Meshes (there might be some funky morphtargets missing but seems OK in practice?) 
