
cube.location.z = 0
cube.location.z = 3

w = cc.window_manager.windows[0]
s = w.screen
[print(a.type) for a in w.screen.areas]
for a in w.screen.areas:
    if a.type == 'TEXT_EDITOR':
        break
o = bpy.context.copy()
o["window"] = w
o["screen"] = s
o["area"]   = a
o["space_data"] = a.spaces.active
o["region"]  = a.regions[-1]
o["workspace"]  = w.workspace
o["scene"]  = w.scene

bpy.ops.mesh.primitive_cube_add(o)
bpy.ops.import_scene.fbx(o, filepath='C:/Users/mrever/Downloads/3dmodels/ryu-hayabusa-from-warriors-orochi-3-ultimate/0.fbx')

oo.keys()
c2 = oo['Cube.001']


dir(w)
dir(s)
dir(a)
a.spaces.active
a.type

dir(a.regions[0])

for r in a.regions: print(r.type)

for item in dir(bpy.context): print(item, ':\t',eval('bpy.context.' + item))

print(bpy.context.area)



import bpy
objs = bpy.data.objects
objs.remove(objs["Camera"], do_unlink=True)

objectify()
armature.location
amt = armature
ls = amt.pose.bones['arm left shoulder 1']
rs = amt.pose.bones['arm right shoulder 1']
ls.rotation_quaternion
ls.rotation_quaternion.x += 0.3
ls.rotation_quaternion.z -= 0.2

rs.rotation_quaternion.x += 0.2

bpy.ops.object.posemode_toggle()


oo.keys()

bpy.data.objects['Light'].location
amt = bpy.data.objects['Armature']
light
armature

bpy.context.scene.objects.active = amt
bpy.ops.object.mode_set(mode='POSE')

[print(b) for b in amt.pose.bones.keys() if 'unused' not in b]

dir(ls)


ls.rotation_mode
ls.rotation_quaternion

ls.rotation_quaternion.w = 1.3422
ls.rotation_quaternion.x = 3.113
ls.rotation_quaternion.y = 0.50
ls.rotation_quaternion.z = 0.00


ls.rotation.quaternion.x += 0.3

bpy.bone = ls

ls.rotation_mode

amt.location.y += 2

amt = bpy.data.objects['Armature']
ls = amt.pose.bones['arm left shoulder 1']
ls.rotation_quaternion

ls.rotation_quaternion.rotate_axis

bpy.context.area

bpy.ops.object.mode_set(o, mode='EDIT')
bpy.ops.object.mode_set(o, mode='OBJECT')
bpy.ops.import_scene.fbx(o, filepath='C:/Users/mrever/Downloads/3dmodels/ryu-hayabusa-from-warriors-orochi-3-ultimate/0.fbx')

bpy.ops.object.mode_set.poll()


cube.data.vertices[4].co
cube.data.vertices[4].co.z = 0.5

c2.data.vertices[4].co.z = -3

for v in range(8):
    c2.data.vertices[v].co.x += 2*rd()-1
    c2.data.vertices[v].co.y += 2*rd()-1
    c2.data.vertices[v].co.z += 2*rd()-1


rd = np.random.rand

rd()
