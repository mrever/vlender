import bpy
from neovim import attach
from console.intellisense import complete
import numpy as np
import os
import subprocess
from time import sleep

print(os.getcwd())

os.environ['NVIM_LISTEN_ADDRESS'] = '\\\\.\\pipe\\nvim-12000-0'
subprocess.Popen(['./Neovim/bin/nvim-qt.exe'])
sleep(1)
for index in range(10):
    try:
        nvim = attach('socket', path='\\\\.\\pipe\\nvim-12000-0')
    except:
        sleep(1)


nvim.command('e returnbuf.py')
nvim.command('vsp outbuf.py')
nvim.command('e compbuf.py')
nvim.command('e compretbuf.py')
nvim.command('e ~/vlender/blendscript.py')

nvim.command('nnoremap <c-\> yy:b 2<cr>p<c-o>')
nvim.command('vnoremap <c-\> y:b 2<cr>p<c-o>')
nvim.command('inoremap <c-\> <esc>mpyy:b 2<cr>p<c-o>`pa')

nvim.command('nnoremap <c-b> :silent! normal 0v$F=<esc>hy:b 2<cr>ggiprint(<esc>pA)<esc><c-o>')
nvim.command('inoremap <c-b> <esc>:silent! normal mp0v$F=<esc>hy:b 2<cr>ggiprint(<esc>pA)<esc><c-o>`pa')

nvim.command('inoremap <c-u> <esc>mp0v$hy:b 3<cr>ggp<c-o>`pa')

nvim.command('colorscheme personal_dark')
nvim.command('set guifont=Consolas:h12')


def print(*args, **kwargs):
    outstr = ''
    for arg in args:
        outstr = ' '.join([str(arg) for arg in args])
    for line in outstr.split('\n'):
        nvim.buffers[1].append(line)
        

bb = bpy
cc = bpy.context
dd = bpy.data
oo = bpy.data.objects
ops = bpy.ops
mcontext = bpy.context.copy()

def objectify():
    for obj in oo.keys():
        globals()[obj.lower().replace('.','')] = oo[obj]
objectify()


def get_completions(linein):
    return complete(linein, len(linein), globals(), True)[0]

storevars = {}
def pollnvim():
    code = '\n'.join(nvim.buffers[2][:])
    nvim.buffers[2][:]=[]
    linein = nvim.buffers[3][0]
    if linein != '':
        nvim.buffers[4].append( [l[len(linein):] for l in get_completions(linein)] )
        del nvim.buffers[4][0]
        nvim.buffers[3][:] = []
    try:
        for ムラ in storevars.keys():
            locals()[ムラ] = storevars[ムラ]
        exec(code)
        for ムラ in locals().keys():
            storevars[ムラ] = locals()[ムラ]
    except Exception as e:
        print(e)
    return 0.2


nvim.command('py3 import vim')

compfun = \
'''
func! Pycomplete()
    py3 vim.command("call complete(col(\'.\'), " + repr( vim.buffers[4][:] ) + ')')
    py3 vim.buffers[4][:] = []
    return ''
endfunc
'''
nvim.command(compfun)
nvim.command('inoremap <c-y> <C-R>=Pycomplete()<CR>')

bpy.pollnvim = pollnvim
bpy.app.timers.register(bpy.pollnvim)

#bpy.app.timers.unregister(bpy.pollnvim)
