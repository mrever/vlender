objectify()
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




###########################################

#bpy.ops.object.gpencil_add(align='WORLD', location=(0, 0, 0), type='EMPTY', name='shit')
#bpy.ops.object.add(align='WORLD', location=(0, 0, 0), type='GPENCIL')
q = bpy.data.grease_pencils.new(name='fuck')
gp3 = bpy.data.objects.new(name='bitch', object_data=q)
bpy.context.view_layer.active_layer_collection.collection.objects.link(gp3)
gp3

gp3.data.layers.new(name='ass')
gp3.data.layers[0].frames.new(frame_number=0)
gp3.data.layers[0].frames[0].strokes.new()
s = gp3.data.layers[0].frames[0].strokes[0]
s.points.add(count=5)
s.points[0].co = (2,2,3)
s.points[1].co = (1,3,2)
s.points[2].co = (1,2,1)
s.points[3].co = (4,2,0)
s.points[4].co = (1,-2,0)

gg = mkgpstroke(name='fuckfarts', numpoints=20)
gg.data.layers[0].frames[0].strokes[0].points[10].co.z = 3

def mkgpstroke(name="mygp", numpoints=10):
    q = bpy.data.grease_pencils.new(name=name)
    gp3 = bpy.data.objects.new(name=name, object_data=q)
    bpy.context.view_layer.active_layer_collection.collection.objects.link(gp3)
    gp3.data.layers.new(name=name)
    gp3.data.layers[0].frames.new(frame_number=0)
    gp3.data.layers[0].frames[0].strokes.new()
    s = gp3.data.layers[0].frames[0].strokes[0]
    s.points.add(count=numpoints)
    dx = 0
    for pt in s.points:
        pt.co.x += dx
        dx += 1
    gp3.data.pixel_factor = 19
    return gp3


pts = gpencil.data.layers[0].frames[0].strokes[0].points
pts[100].co.z = 10

gg.data.pixel_factor = 20
