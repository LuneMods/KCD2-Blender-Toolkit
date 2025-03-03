# TODO
## Problems
### HIGH PRIORITY
- [ ] Vertex count is different after going through rc.exe. This kinda breaks the entire equipment system.
- [ ] Importing of physics bones & proxies, for belt physics etc.
- [ ] cgf meshes get imported with the wrong origin, throws out slot helper locations etc.
- [ ] Importing of Morph Targets
- [ ] Textures in .mtl files sometimes have texture paths to another directory, instead of relative.

### Low Priority
- [ ] imported split normals sometimes all point in one direction on .cgf files.


## New Features to Add
- [ ] Vertex color assignment in alpha channel.
- [ ] Import directly from .pak files
- [ ] Export .mtl files
- [ ] export item .xml files


## Random Comments:
Exporting of static meshes (cgf) seems to be working alright. 

The issues are mainly with skinned meshes. 
Currently running a .dae file through rc.exe creates extra vertices which breaks the entire equipment layering system somehow.

FBX works through rc.exe, but this loses all the cryengine attributes.

