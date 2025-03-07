# TODO
## Problems
- [ ] Morph Targets, physics bones & most proxies dont get imported
- [ ] cgf weapon meshes get imported with the wrong origin, which throws out slot helper locations etc. These can just be moved into the correct position.
- [ ] Textures in .mtl files sometimes have texture paths to another directory, instead of relative.
- [ ] imported split normals sometimes all point in one direction on .cgf files.
- [ ] Fix crash when trying to export from edit mode or modes other than object. (hard to reproduce?)
- [x] Fix bone orientations.
- [x] Fix exporting error related to non-manifold geometry.
- [x] Vertex count is different after going through rc.exe. This kinda breaks the entire equipment system.



## New Features to Add
- [ ] Easier vertex color assignment for the alpha channel.
- [ ] Physics Proxy importing.
- [ ] Physics bone importing.
- [ ] Morph Target importing
- [ ] Import directly from .pak files
- [ ] Export .mtl files
- [ ] export item .xml files