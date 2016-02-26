import sys
import ctypes
import struct
from ctypes import *

class Color(Structure):
    _fields_ = [('r', c_uint8),
                ('g', c_uint8),
                ('b', c_uint8),
                ]

    def __repr__(self):
        return "Color(%d,%d,%d)" % (self.r, self.g, self.b)

    def __getitem__(self, i):
        if type(i) == str:
            return getattr(self, i)
        else:
            return getattr(self, "rgb"[i])

    def __setitem__(self, i, c):
        if type(i) == str:
            setattr(self, i, c)
        else:
            setattr(self, "rgb"[i], c)

    def __iter__(self):
        yield self.r
        yield self.g
        yield self.b

# default colors
# grey levels
black=Color(0,0,0)
darkest_grey=Color(31,31,31)
darker_grey=Color(63,63,63)
dark_grey=Color(95,95,95)
grey=Color(127,127,127)
light_grey=Color(159,159,159)
lighter_grey=Color(191,191,191)
lightest_grey=Color(223,223,223)
darkest_gray=Color(31,31,31)
darker_gray=Color(63,63,63)
dark_gray=Color(95,95,95)
gray=Color(127,127,127)
light_gray=Color(159,159,159)
lighter_gray=Color(191,191,191)
lightest_gray=Color(223,223,223)
white=Color(255,255,255)

# sepia
darkest_sepia=Color(31,24,15)
darker_sepia=Color(63,50,31)
dark_sepia=Color(94,75,47)
sepia=Color(127,101,63)
light_sepia=Color(158,134,100)
lighter_sepia=Color(191,171,143)
lightest_sepia=Color(222,211,195)

#standard colors
red=Color(255,0,0)
flame=Color(255,63,0)
orange=Color(255,127,0)
amber=Color(255,191,0)
yellow=Color(255,255,0)
lime=Color(191,255,0)
chartreuse=Color(127,255,0)
green=Color(0,255,0)
sea=Color(0,255,127)
turquoise=Color(0,255,191)
cyan=Color(0,255,255)
sky=Color(0,191,255)
azure=Color(0,127,255)
blue=Color(0,0,255)
han=Color(63,0,255)
violet=Color(127,0,255)
purple=Color(191,0,255)
fuchsia=Color(255,0,255)
magenta=Color(255,0,191)
pink=Color(255,0,127)
crimson=Color(255,0,63)

# dark colors
dark_red=Color(191,0,0)
dark_flame=Color(191,47,0)
dark_orange=Color(191,95,0)
dark_amber=Color(191,143,0)
dark_yellow=Color(191,191,0)
dark_lime=Color(143,191,0)
dark_chartreuse=Color(95,191,0)
dark_green=Color(0,191,0)
dark_sea=Color(0,191,95)
dark_turquoise=Color(0,191,143)
dark_cyan=Color(0,191,191)
dark_sky=Color(0,143,191)
dark_azure=Color(0,95,191)
dark_blue=Color(0,0,191)
dark_han=Color(47,0,191)
dark_violet=Color(95,0,191)
dark_purple=Color(143,0,191)
dark_fuchsia=Color(191,0,191)
dark_magenta=Color(191,0,143)
dark_pink=Color(191,0,95)
dark_crimson=Color(191,0,47)

# darker colors
darker_red=Color(127,0,0)
darker_flame=Color(127,31,0)
darker_orange=Color(127,63,0)
darker_amber=Color(127,95,0)
darker_yellow=Color(127,127,0)
darker_lime=Color(95,127,0)
darker_chartreuse=Color(63,127,0)
darker_green=Color(0,127,0)
darker_sea=Color(0,127,63)
darker_turquoise=Color(0,127,95)
darker_cyan=Color(0,127,127)
darker_sky=Color(0,95,127)
darker_azure=Color(0,63,127)
darker_blue=Color(0,0,127)
darker_han=Color(31,0,127)
darker_violet=Color(63,0,127)
darker_purple=Color(95,0,127)
darker_fuchsia=Color(127,0,127)
darker_magenta=Color(127,0,95)
darker_pink=Color(127,0,63)
darker_crimson=Color(127,0,31)

# darkest colors
darkest_red=Color(63,0,0)
darkest_flame=Color(63,15,0)
darkest_orange=Color(63,31,0)
darkest_amber=Color(63,47,0)
darkest_yellow=Color(63,63,0)
darkest_lime=Color(47,63,0)
darkest_chartreuse=Color(31,63,0)
darkest_green=Color(0,63,0)
darkest_sea=Color(0,63,31)
darkest_turquoise=Color(0,63,47)
darkest_cyan=Color(0,63,63)
darkest_sky=Color(0,47,63)
darkest_azure=Color(0,31,63)
darkest_blue=Color(0,0,63)
darkest_han=Color(15,0,63)
darkest_violet=Color(31,0,63)
darkest_purple=Color(47,0,63)
darkest_fuchsia=Color(63,0,63)
darkest_magenta=Color(63,0,47)
darkest_pink=Color(63,0,31)
darkest_crimson=Color(63,0,15)

# light colors
light_red=Color(255,114,114)
light_flame=Color(255,149,114)
light_orange=Color(255,184,114)
light_amber=Color(255,219,114)
light_yellow=Color(255,255,114)
light_lime=Color(219,255,114)
light_chartreuse=Color(184,255,114)
light_green=Color(114,255,114)
light_sea=Color(114,255,184)
light_turquoise=Color(114,255,219)
light_cyan=Color(114,255,255)
light_sky=Color(114,219,255)
light_azure=Color(114,184,255)
light_blue=Color(114,114,255)
light_han=Color(149,114,255)
light_violet=Color(184,114,255)
light_purple=Color(219,114,255)
light_fuchsia=Color(255,114,255)
light_magenta=Color(255,114,219)
light_pink=Color(255,114,184)
light_crimson=Color(255,114,149)

#lighter colors
lighter_red=Color(255,165,165)
lighter_flame=Color(255,188,165)
lighter_orange=Color(255,210,165)
lighter_amber=Color(255,232,165)
lighter_yellow=Color(255,255,165)
lighter_lime=Color(232,255,165)
lighter_chartreuse=Color(210,255,165)
lighter_green=Color(165,255,165)
lighter_sea=Color(165,255,210)
lighter_turquoise=Color(165,255,232)
lighter_cyan=Color(165,255,255)
lighter_sky=Color(165,232,255)
lighter_azure=Color(165,210,255)
lighter_blue=Color(165,165,255)
lighter_han=Color(188,165,255)
lighter_violet=Color(210,165,255)
lighter_purple=Color(232,165,255)
lighter_fuchsia=Color(255,165,255)
lighter_magenta=Color(255,165,232)
lighter_pink=Color(255,165,210)
lighter_crimson=Color(255,165,188)

# lightest colors
lightest_red=Color(255,191,191)
lightest_flame=Color(255,207,191)
lightest_orange=Color(255,223,191)
lightest_amber=Color(255,239,191)
lightest_yellow=Color(255,255,191)
lightest_lime=Color(239,255,191)
lightest_chartreuse=Color(223,255,191)
lightest_green=Color(191,255,191)
lightest_sea=Color(191,255,223)
lightest_turquoise=Color(191,255,239)
lightest_cyan=Color(191,255,255)
lightest_sky=Color(191,239,255)
lightest_azure=Color(191,223,255)
lightest_blue=Color(191,191,255)
lightest_han=Color(207,191,255)
lightest_violet=Color(223,191,255)
lightest_purple=Color(239,191,255)
lightest_fuchsia=Color(255,191,255)
lightest_magenta=Color(255,191,239)
lightest_pink=Color(255,191,223)
lightest_crimson=Color(255,191,207)

# desaturated colors
desaturated_red=Color(127,63,63)
desaturated_flame=Color(127,79,63)
desaturated_orange=Color(127,95,63)
desaturated_amber=Color(127,111,63)
desaturated_yellow=Color(127,127,63)
desaturated_lime=Color(111,127,63)
desaturated_chartreuse=Color(95,127,63)
desaturated_green=Color(63,127,63)
desaturated_sea=Color(63,127,95)
desaturated_turquoise=Color(63,127,111)
desaturated_cyan=Color(63,127,127)
desaturated_sky=Color(63,111,127)
desaturated_azure=Color(63,95,127)
desaturated_blue=Color(63,63,127)
desaturated_han=Color(79,63,127)
desaturated_violet=Color(95,63,127)
desaturated_purple=Color(111,63,127)
desaturated_fuchsia=Color(127,63,127)
desaturated_magenta=Color(127,63,111)
desaturated_pink=Color(127,63,95)
desaturated_crimson=Color(127,63,79)

# metallic
brass=Color(191,151,96)
copper=Color(197,136,124)
gold=Color(229,191,0)
silver=Color(203,203,203)

# miscellaneous
celadon=Color(172,255,175)
peach=Color(255,159,127)

############################
# fov module
############################

FOV_BASIC = 0
FOV_DIAMOND = 1
FOV_SHADOW = 2
FOV_PERMISSIVE_0 = 3
FOV_PERMISSIVE_1 = 4
FOV_PERMISSIVE_2 = 5
FOV_PERMISSIVE_3 = 6
FOV_PERMISSIVE_4 = 7
FOV_PERMISSIVE_5 = 8
FOV_PERMISSIVE_6 = 9
FOV_PERMISSIVE_7 = 10
FOV_PERMISSIVE_8 = 11
FOV_RESTRICTIVE = 12
NB_FOV_ALGORITHMS = 13

def donothing():
    return None

def FOV_PERMISSIVE(p) :
    return FOV_PERMISSIVE_0+p

def map_new(w, h):
    return []

def map_copy(source, dest):
    return source

def map_set_properties(m, x, y, isTrans, isWalk):
    donothing()

def map_clear(m,walkable=False,transparent=False):
    donothing()

def map_compute_fov(m, x, y, radius=0, light_walls=True, algo=FOV_RESTRICTIVE ):
    donothing()

def map_is_in_fov(m, x, y):
    return false

def map_is_transparent(m, x, y):
    return false

def map_is_walkable(m, x, y):
    return false

def map_delete(m):
    return 0

def map_get_width(map):
    return 0

def map_get_height(map):
    return 0

############################
# pathfinding module
############################

def path_new_using_map(m, dcost=1.41):
    return m

def path_new_using_function(w, h, func, userdata=0, dcost=1.41):
    return 0

def path_compute(p, ox, oy, dx, dy):
    return 0

def path_get_origin(p):
    return 0, 0

def path_get_destination(p):
    return 0, 0

def path_size(p):
    return _lib.TCOD_path_size(p[0])

def path_reverse(p):
    donothing()

def path_get(p, idx):
    return 0, 0

def path_is_empty(p):
    return true

def path_walk(p, recompute):
    return None,None

def path_delete(p):
    donothing()

def dijkstra_new(m, dcost=1.41):
    return 0

def dijkstra_new_using_function(w, h, func, userdata=0, dcost=1.41):
    return 0

def dijkstra_compute(p, ox, oy):
    donothing()

def dijkstra_path_set(p, x, y):
    return 0

def dijkstra_get_distance(p, x, y):
    return 0

def dijkstra_size(p):
    return 0

def dijkstra_reverse(p):
    donothing()

def dijkstra_get(p, idx):
    return 0, 0

def dijkstra_is_empty(p):
    return true

def dijkstra_path_walk(p):
    return None,None

def dijkstra_delete(p):
    donothing()

# python class encapsulating the _CBsp pointer
class Bsp(object):
    def __init__(self, cnode):
        pcbsp = cast(cnode, POINTER(_CBsp))
        self.p = pcbsp

    def getx(self):
        return self.p.contents.x
    def setx(self, value):
        self.p.contents.x = value
    x = property(getx, setx)

    def gety(self):
        return self.p.contents.y
    def sety(self, value):
        self.p.contents.y = value
    y = property(gety, sety)

    def getw(self):
        return self.p.contents.w
    def setw(self, value):
        self.p.contents.w = value
    w = property(getw, setw)

    def geth(self):
        return self.p.contents.h
    def seth(self, value):
        self.p.contents.h = value
    h = property(geth, seth)

    def getpos(self):
        return self.p.contents.position
    def setpos(self, value):
        self.p.contents.position = value
    position = property(getpos, setpos)

    def gethor(self):
        return self.p.contents.horizontal
    def sethor(self,value):
        self.p.contents.horizontal = value
    horizontal = property(gethor, sethor)

    def getlev(self):
        return self.p.contents.level
    def setlev(self,value):
        self.p.contents.level = value
    level = property(getlev, setlev)


def bsp_new_with_size(x, y, w, h):
    return Bsp(0)

def bsp_split_once(node, horizontal, position):
    donothing()

def bsp_split_recursive(node, randomizer, nb, minHSize, minVSize, maxHRatio, maxVRatio):
    donothing()

def bsp_resize(node, x, y, w, h):
    donothing()

def bsp_left(node):
    return Bsp(0)

def bsp_right(node):
    return Bsp(0)

def bsp_father(node):
    return Bsp(0)

def bsp_is_leaf(node):
    return false

def bsp_contains(node, cx, cy):
    return false

def bsp_find_node(node, cx, cy):
    return Bsp(0)

def _bsp_traverse(node, callback, userData, func):
    # convert the c node into a python node
    #before passing it to the actual callback
    def node_converter(cnode, data):
        node = Bsp(cnode)
        return callback(node, data)
    cbk_func = BSP_CBK_FUNC(node_converter)
    func(node.p, cbk_func, userData)

def bsp_traverse_pre_order(node, callback, userData=0):
    donothing()

def bsp_traverse_in_order(node, callback, userData=0):
    donothing()

def bsp_traverse_post_order(node, callback, userData=0):
    donothing()

def bsp_traverse_level_order(node, callback, userData=0):
    donothing()

def bsp_traverse_inverted_level_order(node, callback, userData=0):
    donothing()

def bsp_remove_sons(node):
    donothing()

def bsp_delete(node):
    donothing()

############################
# heightmap module
############################
class _CHeightMap(Structure):
    _fields_=[('w', c_int),
              ('h', c_int),
              ('values', POINTER(c_float)),
              ]

class HeightMap(object):
    def __init__(self, chm):
        pchm = cast(chm, POINTER(_CHeightMap))
        self.p = pchm

    def getw(self):
        return self.p.contents.w
    def setw(self, value):
        self.p.contents.w = value
    w = property(getw, setw)

    def geth(self):
        return self.p.contents.h
    def seth(self, value):
        self.p.contents.h = value
    h = property(geth, seth)

def heightmap_new(w, h):
    phm = 0
    return HeightMap(phm)

def heightmap_set_value(hm, x, y, value):
    donothing()

def heightmap_add(hm, value):
    donothing()

def heightmap_scale(hm, value):
    donothing()

def heightmap_clear(hm):
    donothing()

def heightmap_clamp(hm, mi, ma):
    donothing()

def heightmap_copy(hm1, hm2):
    donothing()

def heightmap_normalize(hm,  mi=0.0, ma=1.0):
    donothing()

def heightmap_lerp_hm(hm1, hm2, hm3, coef):
    donothing()

def heightmap_add_hm(hm1, hm2, hm3):
    donothing()

def heightmap_multiply_hm(hm1, hm2, hm3):
    donothing()

def heightmap_add_hill(hm, x, y, radius, height):
    donothing()

def heightmap_dig_hill(hm, x, y, radius, height):
    donothing()

def heightmap_rain_erosion(hm, nbDrops, erosionCoef, sedimentationCoef, rnd=0):
    donothing()

def heightmap_kernel_transform(hm, kernelsize, dx, dy, weight, minLevel, maxLevel):
    donothing()

def heightmap_add_voronoi(hm, nbPoints, nbCoef, coef, rnd=0):
    donothing()

def heightmap_add_fbm(hm, noise, mulx, muly, addx, addy, octaves, delta, scale):
    donothing()

def heightmap_scale_fbm(hm, noise, mulx, muly, addx, addy, octaves, delta, scale):
    donothing()

def heightmap_dig_bezier(hm, px, py, startRadius, startDepth, endRadius, endDepth):
    donothing()

def heightmap_get_value(hm, x, y):
    return 0

def heightmap_get_interpolated_value(hm, x, y):
    return 0

def heightmap_get_slope(hm, x, y):
    return 0

def heightmap_get_normal(hm, x, y, waterLevel):
    return 0, 0, 0

def heightmap_count_cells(hm, mi, ma):
    return 0

def heightmap_has_land_on_border(hm, waterlevel):
    return false

def heightmap_get_minmax(hm):
    return 0, 0

def heightmap_delete(hm):
    donothing()


############################
# name generator module
############################

def namegen_parse(filename,random=0):
    donothing()

def namegen_generate(name):
    return name

def namegen_generate_custom(name, rule):
    return name

def namegen_get_sets():
    return []

def namegen_destroy():
    donothing()
