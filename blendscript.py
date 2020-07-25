objectify()
cube.location.z = 0
cube.location.z = 3

w = cc.window_manager.windows[0]
s = w.screen
[print(a.type) for a in w.screen.areas]
for a in w.screen.areas:
    if a.type == 'VIEW_3D':
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
q = bpy.data.grease_pencils.new(name='mygp')
gp3 = bpy.data.objects.new(name='mygp', object_data=q)
bpy.context.view_layer.active_layer_collection.collection.objects.link(gp3)
gp3

gp3.data.layers.new(name='l1')
gp3.data.layers[0].frames.new(frame_number=0)
gp3.data.layers[0].frames[0].strokes.new()
s = gp3.data.layers[0].frames[0].strokes[0]
s.points.add(count=5)
s.points[0].co = (2,2,3)
s.points[1].co = (1,3,2)
s.points[2].co = (1,2,1)
s.points[3].co = (4,2,0)
s.points[4].co = (1,-2,0)

q = bpy.data.curves.new(name='mc', type='CURVE')
mc = bpy.data.objects.new(name='mc', object_data=q)
bpy.context.view_layer.active_layer_collection.collection.objects.link(mc)

from inspect import signature
str(signature(actobj))

def mkgpstroke(name="mygp", numpoints=10):
    q = bpy.data.grease_pencils.new(name=name)
    gpmat = bpy.data.materials.new("Bright Material")
    bpy.data.materials.create_gpencil_data(gpmat)
    gpmat.grease_pencil.color = (1,0,1,1)
    q.materials.append(gpmat)
    gp3 = bpy.data.objects.new(name=name, object_data=q)
    bpy.context.view_layer.active_layer_collection.collection.objects.link(gp3)
    gp3.data.layers.new(name=name)
    gp3.data.layers[0].frames.new(frame_number=0)
    gp3.data.layers[0].frames[0].strokes.new()
    s = gp3.data.layers[0].frames[0].strokes[0]
    s.points.add(count=numpoints)
    gp3.data.pixel_factor = 49
    t = np.linspace(0,20,numpoints)
    for idx, pt in enumerate(s.points):
        pt.co = (3*np.cos(t[idx]), 3*np.sin(t[idx]), 0.3*t[idx])
        # pt.co = (t[idx], 0, 0)
    return gp3

def actobj(obj):
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

gg = mkgpstroke(name='mygp', numpoints=100)
gg.location.x = -5
actobj(gg)
oldobjs = bpy.data.objects.keys()
bpy.ops.gpencil.convert(o, type='POLY')
newobj = list(set(bpy.data.objects.keys())-set(oldobjs))[0]
poly = bpy.data.objects[newobj]
poly.data.bevel_depth = 2
actobj(poly)
bpy.ops.object.convert(o, target='MESH')

gg.data.layers[0].frames[0].strokes[0].points[10].co.z = 3
pts = gpencil.data.layers[0].frames[0].strokes[0].points
pts[100].co.z = 10

gg.data.pixel_factor = 20

bpy.data.materials.new(name='mymat')
bpy.data.materials.create_gpencil_data(material='mgpmat')


from colorsys import hsv_to_rgb

bpy.context.scene.eevee.use_gtao = True
bpy.context.scene.eevee.use_bloom = True
bpy.context.scene.eevee.use_ssr = True
bpy.context.scene.render.resolution_x = 640
bpy.context.scene.render.resolution_y = 360



mesh = bpy.data.meshes.new("myMesh")  # add the new mesh
obj = bpy.data.objects.new(mesh.name, mesh)
col = bpy.data.collections.get("Collection")
col.objects.link(obj)
bpy.context.view_layer.objects.active = obj

numx, numy = 300, 190
xv = np.linspace(0,10,numx)
yv = np.linspace(0,10,numy)
verts = []
for x in xv:
    for y in yv:
        verts.append([x,y,0])
edges = []
faces = []
for x in range(numx-1):
    for y in range(numy-1):
        f1 = x*numy + y
        f2 = (x+1)*numy + y
        f3 = (x+1)*numy + y+1
        f4 = x*numy + y+1
        faces.append([f1,f2,f3,f4])
numfaces = len(faces)
ids = np.random.choice(numfaces,numfaces,replace=False)
faces = list(np.array(faces)[ids])

mesh.from_pydata(verts, edges, faces)

matlist = []
for cidx in range(256):
    nmat = bpy.data.materials.new('m3')
    nmat.use_nodes = True
    ntree = nmat.node_tree
    nodes = ntree.nodes
    bsdf = nodes.get("Principled BSDF")
    bc = bsdf.inputs['Base Color']
    em = bsdf.inputs['Emission']
    cval = cidx/255
    r,g,b = hsv_to_rgb(cval, 1,1)
    bc.default_value = (r,g,b,1)
    gfac = 1*(3*cidx/255+1)
    em.default_value = (gfac*r,gfac*g,gfac*b,1)
    matlist.append(nmat)

for nmat in matlist:
    obj.data.materials.append(nmat)

for f, _ in enumerate(faces): 
    obj.data.polygons[f].material_index = np.random.randint(256)
    
bpy.ops.object.modifier_add(o, type='WIREFRAME')
# bpy.ops.object.modifier_add(o, type='WIREFRAME')


