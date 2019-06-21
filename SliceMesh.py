import bpy
import bmesh
from numpy import interp

bpy.ops.object.editmode_toggle()

# Slicing

min = 0
max = 50

for i in range(min, max):
    t = interp(i,[min,(max-1)],[0.8,1.8])  # Slicing Travel
    r = interp(i,[min,(max-1)],[-1.0,1.0]) # Slicing rotation
    
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.bisect(plane_co=(0, 0, t), plane_no=(0, 0, 1))
    bpy.ops.mesh.edge_split()
    
print('Slicing Done!\n')

# Fill holes

bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
bpy.ops.mesh.select_non_manifold()
bpy.ops.mesh.edge_face_add()
bpy.ops.mesh.faces_shade_flat()

print('Filling Done!')

# Separate

bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.separate(type='LOOSE')

bpy.ops.object.editmode_toggle()