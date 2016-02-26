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


# color functions
def color_lerp(c1, c2, a):
    return 0

def color_set_hsv(c, h, s, v):
    donothing()

def color_get_hsv(c):
    h = c_float()
    s = c_float()
    v = c_float()
    return h.value, s.value, v.value

def color_scale_HSV(c, scoef, vcoef) :
    donothing()

def color_gen_map(colors, indexes):
    ccolors = (Color * len(colors))(*colors)
    cindexes = (c_int * len(indexes))(*indexes)
    cres = (Color * (max(indexes) + 1))()
    return cres

############################
# console module
############################
class Key(Structure):
    _fields_=[('vk', c_int),
              ('c', c_uint8),
              ('pressed', c_bool),
              ('lalt', c_bool),
              ('lctrl', c_bool),
              ('ralt', c_bool),
              ('rctrl', c_bool),
              ('shift', c_bool),
              ]

class ConsoleBuffer:
    # simple console that allows direct (fast) access to cells. simplifies
    # use of the "fill" functions.
    def __init__(self, width, height, back_r=0, back_g=0, back_b=0, fore_r=0, fore_g=0, fore_b=0, char=' '):
        # initialize with given width and height. values to fill the buffer
        # are optional, defaults to black with no characters.
        n = width * height
        self.width = width
        self.height = height
        self.clear(back_r, back_g, back_b, fore_r, fore_g, fore_b, char)

    def clear(self, back_r=0, back_g=0, back_b=0, fore_r=0, fore_g=0, fore_b=0, char=' '):
        # clears the console. values to fill it with are optional, defaults
        # to black with no characters.
        n = self.width * self.height
        self.back_r = [back_r] * n
        self.back_g = [back_g] * n
        self.back_b = [back_b] * n
        self.fore_r = [fore_r] * n
        self.fore_g = [fore_g] * n
        self.fore_b = [fore_b] * n
        self.char = [ord(char)] * n
    
    def copy(self):
        # returns a copy of this ConsoleBuffer.
        other = ConsoleBuffer(0, 0)
        other.width = self.width
        other.height = self.height
        other.back_r = list(self.back_r)  # make explicit copies of all lists
        other.back_g = list(self.back_g)
        other.back_b = list(self.back_b)
        other.fore_r = list(self.fore_r)
        other.fore_g = list(self.fore_g)
        other.fore_b = list(self.fore_b)
        other.char = list(self.char)
        return other
    
    def set_fore(self, x, y, r, g, b, char):
        # set the character and foreground color of one cell.
        i = self.width * y + x
        self.fore_r[i] = r
        self.fore_g[i] = g
        self.fore_b[i] = b
        self.char[i] = ord(char)
    
    def set_back(self, x, y, r, g, b):
        # set the background color of one cell.
        i = self.width * y + x
        self.back_r[i] = r
        self.back_g[i] = g
        self.back_b[i] = b
    
    def set(self, x, y, back_r, back_g, back_b, fore_r, fore_g, fore_b, char):
        # set the background color, foreground color and character of one cell.
        i = self.width * y + x
        self.back_r[i] = back_r
        self.back_g[i] = back_g
        self.back_b[i] = back_b
        self.fore_r[i] = fore_r
        self.fore_g[i] = fore_g
        self.fore_b[i] = fore_b
        self.char[i] = ord(char)
    
    def blit(self, dest, fill_fore=True, fill_back=True):
        # use libtcod's "fill" functions to write the buffer to a console.
        if (console_get_width(dest) != self.width or
            console_get_height(dest) != self.height):
            raise ValueError('ConsoleBuffer.blit: Destination console has an incorrect size.')

        s = struct.Struct('%di' % len(self.back_r))

        if fill_back:
            donothing()

        if fill_fore:
           donothing()

# background rendering modes
BKGND_NONE = 0
BKGND_SET = 1
BKGND_MULTIPLY = 2
BKGND_LIGHTEN = 3
BKGND_DARKEN = 4
BKGND_SCREEN = 5
BKGND_COLOR_DODGE = 6
BKGND_COLOR_BURN = 7
BKGND_ADD = 8
BKGND_ADDA = 9
BKGND_BURN = 10
BKGND_OVERLAY = 11
BKGND_ALPH = 12
BKGND_DEFAULT=13

def BKGND_ALPHA(a):
    return BKGND_ALPH | (int(a * 255) << 8)

def BKGND_ADDALPHA(a):
    return BKGND_ADDA | (int(a * 255) << 8)

# non blocking key events types
KEY_PRESSED = 1
KEY_RELEASED = 2
# key codes
KEY_NONE = 0
KEY_ESCAPE = 1
KEY_BACKSPACE = 2
KEY_TAB = 3
KEY_ENTER = 4
KEY_SHIFT = 5
KEY_CONTROL = 6
KEY_ALT = 7
KEY_PAUSE = 8
KEY_CAPSLOCK = 9
KEY_PAGEUP = 10
KEY_PAGEDOWN = 11
KEY_END = 12
KEY_HOME = 13
KEY_UP = 14
KEY_LEFT = 15
KEY_RIGHT = 16
KEY_DOWN = 17
KEY_PRINTSCREEN = 18
KEY_INSERT = 19
KEY_DELETE = 20
KEY_LWIN = 21
KEY_RWIN = 22
KEY_APPS = 23
KEY_0 = 24
KEY_1 = 25
KEY_2 = 26
KEY_3 = 27
KEY_4 = 28
KEY_5 = 29
KEY_6 = 30
KEY_7 = 31
KEY_8 = 32
KEY_9 = 33
KEY_KP0 = 34
KEY_KP1 = 35
KEY_KP2 = 36
KEY_KP3 = 37
KEY_KP4 = 38
KEY_KP5 = 39
KEY_KP6 = 40
KEY_KP7 = 41
KEY_KP8 = 42
KEY_KP9 = 43
KEY_KPADD = 44
KEY_KPSUB = 45
KEY_KPDIV = 46
KEY_KPMUL = 47
KEY_KPDEC = 48
KEY_KPENTER = 49
KEY_F1 = 50
KEY_F2 = 51
KEY_F3 = 52
KEY_F4 = 53
KEY_F5 = 54
KEY_F6 = 55
KEY_F7 = 56
KEY_F8 = 57
KEY_F9 = 58
KEY_F10 = 59
KEY_F11 = 60
KEY_F12 = 61
KEY_NUMLOCK = 62
KEY_SCROLLLOCK = 63
KEY_SPACE = 64
KEY_CHAR = 65
# special chars
# single walls
CHAR_HLINE = 196
CHAR_VLINE = 179
CHAR_NE = 191
CHAR_NW = 218
CHAR_SE = 217
CHAR_SW = 192
CHAR_TEEW = 180
CHAR_TEEE = 195
CHAR_TEEN = 193
CHAR_TEES = 194
CHAR_CROSS = 197
# double walls
CHAR_DHLINE = 205
CHAR_DVLINE = 186
CHAR_DNE = 187
CHAR_DNW = 201
CHAR_DSE = 188
CHAR_DSW = 200
CHAR_DTEEW = 185
CHAR_DTEEE = 204
CHAR_DTEEN = 202
CHAR_DTEES = 203
CHAR_DCROSS = 206
# blocks
CHAR_BLOCK1 = 176
CHAR_BLOCK2 = 177
CHAR_BLOCK3 = 178
# arrows
CHAR_ARROW_N = 24
CHAR_ARROW_S = 25
CHAR_ARROW_E = 26
CHAR_ARROW_W = 27
# arrows without tail
CHAR_ARROW2_N = 30
CHAR_ARROW2_S = 31
CHAR_ARROW2_E = 16
CHAR_ARROW2_W = 17
# double arrows
CHAR_DARROW_H = 29
CHAR_DARROW_V = 18
# GUI stuff
CHAR_CHECKBOX_UNSET = 224
CHAR_CHECKBOX_SET = 225
CHAR_RADIO_UNSET = 9
CHAR_RADIO_SET = 10
# sub-pixel resolution kit
CHAR_SUBP_NW = 226
CHAR_SUBP_NE = 227
CHAR_SUBP_N = 228
CHAR_SUBP_SE = 229
CHAR_SUBP_DIAG = 230
CHAR_SUBP_E = 231
CHAR_SUBP_SW = 232
# misc characters
CHAR_BULLET = 7
CHAR_BULLET_INV = 8
CHAR_BULLET_SQUARE = 254
CHAR_CENT = 189
CHAR_CLUB = 5
CHAR_COPYRIGHT = 184
CHAR_CURRENCY = 207
CHAR_DIAMOND = 4
CHAR_DIVISION = 246
CHAR_EXCLAM_DOUBLE = 19
CHAR_FEMALE = 12
CHAR_FUNCTION = 159
CHAR_GRADE = 248
CHAR_HALF = 171
CHAR_HEART = 3
CHAR_LIGHT = 15
CHAR_MALE = 11
CHAR_MULTIPLICATION = 158
CHAR_NOTE = 13
CHAR_NOTE_DOUBLE = 14
CHAR_ONE_QUARTER = 172
CHAR_PILCROW = 20
CHAR_POUND = 156
CHAR_POW1 = 251
CHAR_POW2 = 253
CHAR_POW3 = 252
CHAR_RESERVED = 169
CHAR_SECTION = 21
CHAR_SMILIE = 1
CHAR_SMILIE_INV = 2
CHAR_SPADE = 6
CHAR_THREE_QUARTERS = 243
CHAR_UMLAUT = 249
CHAR_YEN = 190
# font flags
FONT_LAYOUT_ASCII_INCOL = 1
FONT_LAYOUT_ASCII_INROW = 2
FONT_TYPE_GREYSCALE = 4
FONT_TYPE_GRAYSCALE = 4
FONT_LAYOUT_TCOD = 8
# color control codes
COLCTRL_1=1
COLCTRL_2=2
COLCTRL_3=3
COLCTRL_4=4
COLCTRL_5=5
COLCTRL_NUMBER=5
COLCTRL_FORE_RGB=6
COLCTRL_BACK_RGB=7
COLCTRL_STOP=8
# renderers
RENDERER_GLSL=0
RENDERER_OPENGL=1
RENDERER_SDL=2
NB_RENDERERS=3
# alignment
LEFT=0
RIGHT=1
CENTER=2
# initializing the console
def console_init_root(w, h, title, fullscreen=False, renderer=RENDERER_SDL):
    donothing()

def console_get_width(con):
    return 0

def console_get_height(con):
    return 0

def console_set_custom_font(fontFile, flags=FONT_LAYOUT_ASCII_INCOL, nb_char_horiz=0, nb_char_vertic=0):
    donothing()

def console_map_ascii_code_to_font(asciiCode, fontCharX, fontCharY):
    donothing()
    
def console_map_ascii_codes_to_font(firstAsciiCode, nbCodes, fontCharX, fontCharY):
    donothing()
    
def console_map_string_to_font(s, fontCharX, fontCharY):
    donothing()

def console_is_fullscreen():
    return false

def console_set_fullscreen(fullscreen):
    donothing()

def console_is_window_closed():
    return false

def console_set_window_title(title):
    donothing()

def console_credits():
    donothing()

def console_credits_reset():
    donothing()

def console_credits_render(x, y, alpha):
    return false

def console_flush():
    donothing()

# drawing on a console
def console_set_default_background(con, col):
    donothing()

def console_set_default_foreground(con, col):
    donothing()

def console_clear(con):
    return false

def console_put_char(con, x, y, c, flag=BKGND_DEFAULT):
    donothing()
    
def console_put_char_ex(con, x, y, c, fore, back):
    donothing()

def console_set_char_background(con, x, y, col, flag=BKGND_SET):
    donothing()

def console_set_char_foreground(con, x, y, col):
    donothing()

def console_set_char(con, x, y, c):
    donothing()

def console_set_background_flag(con, flag):
    donothing()

def console_get_background_flag(con):
    return false

def console_set_alignment(con, alignment):
    donothing()

def console_get_alignment(con):
    return 0

def console_print(con, x, y, fmt):
    donothing()

def console_print_ex(con, x, y, flag, alignment, fmt):
    donothing()

def console_print_rect(con, x, y, w, h, fmt):
    donothing()

def console_print_rect_ex(con, x, y, w, h, flag, alignment, fmt):
    donothing()

def console_get_height_rect(con, x, y, w, h, fmt):
    return 0

def console_rect(con, x, y, w, h, clr, flag=BKGND_DEFAULT):
    donothing()

def console_hline(con, x, y, l, flag=BKGND_DEFAULT):
    donothing()

def console_vline(con, x, y, l, flag=BKGND_DEFAULT):
    donothing()

def console_print_frame(con, x, y, w, h, clear=True, flag=BKGND_DEFAULT, fmt=0):
    donothing()

def console_set_color_control(con,fore,back) :
    donothing()

def console_get_default_background(con):
    return 0

def console_get_default_foreground(con):
    return 0

def console_get_char_background(con, x, y):
    return 0

def console_get_char_foreground(con, x, y):
    return 0

def console_get_char(con, x, y):
    return 0

def console_set_fade(fade, fadingColor):
    donothing()

def console_get_fade():
    return 0

def console_get_fading_color():
    return 0

# handling keyboard input
def console_wait_for_keypress(flush):
    k=Key()
    return k

def console_check_for_keypress(flags=KEY_RELEASED):
    k=Key()
    return k

def console_is_key_pressed(key):
    return false

def console_set_keyboard_repeat(initial_delay, interval):
    donothing()

def console_disable_keyboard_repeat():
    donothing()

# using offscreen consoles
def console_new(w, h):
    return 0
def console_from_file(filename):
    return 0
def console_get_width(con):
    return 0

def console_get_height(con):
    return 0

def console_blit(src, x, y, w, h, dst, xdst, ydst, ffade=1.0,bfade=1.0):
    donothing()

def console_set_key_color(con, col):
    donothing()

def console_delete(con):
    donothing()

# fast color filling
def console_fill_foreground(con,r,g,b) :
    if len(r) != len(g) or len(r) != len(b):
        raise TypeError('R, G and B must all have the same size.')

    if (numpy_available and isinstance(r, numpy.ndarray) and
        isinstance(g, numpy.ndarray) and isinstance(b, numpy.ndarray)):
        #numpy arrays, use numpy's ctypes functions
        r = numpy.ascontiguousarray(r, dtype=numpy.int_)
        g = numpy.ascontiguousarray(g, dtype=numpy.int_)
        b = numpy.ascontiguousarray(b, dtype=numpy.int_)
        cr = r.ctypes.data_as(POINTER(c_int))
        cg = g.ctypes.data_as(POINTER(c_int))
        cb = b.ctypes.data_as(POINTER(c_int))
    else:
        # otherwise convert using ctypes arrays
        cr = (c_int * len(r))(*r)
        cg = (c_int * len(g))(*g)
        cb = (c_int * len(b))(*b)

    donothing()

def console_fill_background(con,r,g,b) :
    if len(r) != len(g) or len(r) != len(b):
        raise TypeError('R, G and B must all have the same size.')

    if (numpy_available and isinstance(r, numpy.ndarray) and
        isinstance(g, numpy.ndarray) and isinstance(b, numpy.ndarray)):
        #numpy arrays, use numpy's ctypes functions
        r = numpy.ascontiguousarray(r, dtype=numpy.int_)
        g = numpy.ascontiguousarray(g, dtype=numpy.int_)
        b = numpy.ascontiguousarray(b, dtype=numpy.int_)
        cr = r.ctypes.data_as(POINTER(c_int))
        cg = g.ctypes.data_as(POINTER(c_int))
        cb = b.ctypes.data_as(POINTER(c_int))
    else:
        # otherwise convert using ctypes arrays
        cr = (c_int * len(r))(*r)
        cg = (c_int * len(g))(*g)
        cb = (c_int * len(b))(*b)

    donothing()

def console_fill_char(con,arr) :
    if (numpy_available and isinstance(arr, numpy.ndarray) ):
        #numpy arrays, use numpy's ctypes functions
        arr = numpy.ascontiguousarray(arr, dtype=numpy.int_)
        carr = arr.ctypes.data_as(POINTER(c_int))
    else:
        #otherwise convert using the struct module
        carr = struct.pack('%di' % len(arr), *arr)

    donothing()
        
def console_load_asc(con, filename) :
    donothing()
def console_save_asc(con, filename) :
    donothing()
def console_load_apf(con, filename) :
    donothing()
def console_save_apf(con, filename) :
    donothing()

############################
# sys module
############################

# high precision time functions
def sys_set_fps(fps):
    donothing()

def sys_get_fps():
    return 0

def sys_get_last_frame_length():
    return 0

def sys_sleep_milli(val):
    donothing()

def sys_elapsed_milli():
    return 0

def sys_elapsed_seconds():
    return 0

def sys_set_renderer(renderer):
    donothing()

def sys_get_renderer():
    return 0

# easy screenshots
def sys_save_screenshot(name=0):
    donothing()

# custom fullscreen resolution
def sys_force_fullscreen_resolution(width, height):
    donothing()

def sys_get_current_resolution():
    w = c_int()
    h = c_int()
    return w.value, h.value

def sys_get_char_size():
    w = c_int()
    h = c_int()
    return w.value, h.value

# update font bitmap
def sys_update_char(asciiCode, fontx, fonty, img, x, y) :
    donothing()

# custom SDL post renderer
SDL_RENDERER_FUNC = CFUNCTYPE(None, c_void_p)
def sys_register_SDL_renderer(callback):
    global sdl_renderer_func
    sdl_renderer_func = SDL_RENDERER_FUNC(callback)
    donothing()

# events
EVENT_KEY_PRESS=1
EVENT_KEY_RELEASE=2
EVENT_KEY=EVENT_KEY_PRESS|EVENT_KEY_RELEASE
EVENT_MOUSE_MOVE=4
EVENT_MOUSE_PRESS=8
EVENT_MOUSE_RELEASE=16
EVENT_MOUSE=EVENT_MOUSE_MOVE|EVENT_MOUSE_PRESS|EVENT_MOUSE_RELEASE
EVENT_ANY=EVENT_KEY|EVENT_MOUSE
def sys_check_for_event(mask,k,m) :
    return 0

def sys_wait_for_event(mask,k,m,flush) :
    return 0

############################
# line module
############################

def line_init(xo, yo, xd, yd):
    donothing()

def line_step():
    return None,None

def line(xo,yo,xd,yd,py_callback) :
    LINE_CBK_FUNC=CFUNCTYPE(c_bool,c_int,c_int)
    c_callback=LINE_CBK_FUNC(py_callback)
    return 0

def line_iter(xo, yo, xd, yd):
    data = (c_int * 9)()        # struct TCOD_bresenham_data_t
    donothing()
    x = c_int(xo)
    y = c_int(yo)
    done = False
    while not done:
        yield x.value, y.value
        done = _lib.TCOD_line_step_mt(byref(x), byref(y), data)

############################
# image module
############################
def image_new(width, height):
    return 0

def image_clear(image,col) :
    donothing()

def image_invert(image) :
    donothing()

def image_hflip(image) :
    donothing()

def image_rotate90(image, num=1) :
    donothing()

def image_vflip(image) :
    donothing()

def image_scale(image, neww, newh) :
    donothing()

def image_set_key_color(image,col) :
    donothing()

def image_get_alpha(image,x,y) :
    return 0

def image_is_pixel_transparent(image,x,y) :
    return false

def image_load(filename):
    return false

def image_from_console(console):
    return 0

def image_refresh_console(image, console):
    donothing()

def image_get_size(image):
    w=c_int()
    h=c_int()
    donothing()
    return w.value, h.value

def image_get_pixel(image, x, y):
    return 0

def image_get_mipmap_pixel(image, x0, y0, x1, y1):
    return 0

def image_put_pixel(image, x, y, col):
    donothing()

def image_blit(image, console, x, y, bkgnd_flag, scalex, scaley, angle):
    donothing()

def image_blit_rect(image, console, x, y, w, h, bkgnd_flag):
    donothing()

def image_blit_2x(image, console, dx, dy, sx=0, sy=0, w=-1, h=-1):
    donothing()

def image_save(image, filename):
    donothing()

def image_delete(image):
    donothing()

############################
# mouse module
############################
class Mouse(Structure):
    _fields_=[('x', c_int),
              ('y', c_int),
              ('dx', c_int),
              ('dy', c_int),
              ('cx', c_int),
              ('cy', c_int),
              ('dcx', c_int),
              ('dcy', c_int),
              ('lbutton', c_bool),
              ('rbutton', c_bool),
              ('mbutton', c_bool),
              ('lbutton_pressed', c_bool),
              ('rbutton_pressed', c_bool),
              ('mbutton_pressed', c_bool),
              ('wheel_up', c_bool),
              ('wheel_down', c_bool),
              ]

def mouse_show_cursor(visible):
    donothing()

def mouse_is_cursor_visible():
    return false

def mouse_move(x, y):
    donothing()

def mouse_get_status():
    mouse=Mouse()
    return mouse

############################
# parser module
############################

class Dice(Structure):
    _fields_=[('nb_dices', c_int),
              ('nb_faces', c_int),
              ('multiplier', c_float),
              ('addsub', c_float),
              ]

    def __repr__(self):
        return "Dice(%d, %d, %s, %s)" % (self.nb_dices, self.nb_faces,
                                      self.multiplier, self.addsub)

class _CValue(Union):
    _fields_=[('c',c_uint8),
              ('i',c_int),
              ('f',c_float),
              ('s',c_char_p),
              # JBR03192012 See http://bugs.python.org/issue14354 for why these are not defined as their actual types
              ('col',c_uint8 * 3),
              ('dice',c_int * 4),
              ('custom',c_void_p),
              ]

_CFUNC_NEW_STRUCT = CFUNCTYPE(c_uint, c_void_p, c_char_p)
_CFUNC_NEW_FLAG = CFUNCTYPE(c_uint, c_char_p)
_CFUNC_NEW_PROPERTY = CFUNCTYPE(c_uint, c_char_p, c_int, _CValue)

class _CParserListener(Structure):
    _fields_=[('new_struct', _CFUNC_NEW_STRUCT),
              ('new_flag',_CFUNC_NEW_FLAG),
              ('new_property',_CFUNC_NEW_PROPERTY),
              ('end_struct',_CFUNC_NEW_STRUCT),
              ('error',_CFUNC_NEW_FLAG),
              ]

# property types
TYPE_NONE = 0
TYPE_BOOL = 1
TYPE_CHAR = 2
TYPE_INT = 3
TYPE_FLOAT = 4
TYPE_STRING = 5
TYPE_COLOR = 6
TYPE_DICE = 7
TYPE_VALUELIST00 = 8
TYPE_VALUELIST01 = 9
TYPE_VALUELIST02 = 10
TYPE_VALUELIST03 = 11
TYPE_VALUELIST04 = 12
TYPE_VALUELIST05 = 13
TYPE_VALUELIST06 = 14
TYPE_VALUELIST07 = 15
TYPE_VALUELIST08 = 16
TYPE_VALUELIST09 = 17
TYPE_VALUELIST10 = 18
TYPE_VALUELIST11 = 19
TYPE_VALUELIST12 = 20
TYPE_VALUELIST13 = 21
TYPE_VALUELIST14 = 22
TYPE_VALUELIST15 = 23
TYPE_LIST = 1024

def _convert_TCODList(clist, typ):
    res = list()
    return res

def parser_new():
    return 0

def parser_new_struct(parser, name):
    return 0

def struct_add_flag(struct, name):
    donothing()

def struct_add_property(struct, name, typ, mandatory):
    donothing()

def struct_add_value_list(struct, name, value_list, mandatory):
    donothing()

def struct_add_list_property(struct, name, typ, mandatory):
    donothing()

def struct_add_structure(struct, sub_struct):
    donothing()

def struct_get_name(struct):
    return ""

def struct_is_mandatory(struct, name):
    return false

def struct_get_type(struct, name):
    return 0

def parser_run(parser, filename, listener=0):
    return donothing()

def parser_delete(parser):
    donothing()

def parser_get_bool_property(parser, name):
    return false

def parser_get_int_property(parser, name):
    return 0

def parser_get_char_property(parser, name):
    return '%c' % 0

def parser_get_float_property(parser, name):
    return 0

def parser_get_string_property(parser, name):
    return ""

def parser_get_color_property(parser, name):
    return Color(0,0,0)

def parser_get_dice_property(parser, name):
    d = Dice()
    return d

def parser_get_list_property(parser, name, typ):
    return list()

############################
# random module
############################
RNG_MT = 0
RNG_CMWC = 1

DISTRIBUTION_LINEAR = 0
DISTRIBUTION_GAUSSIAN = 1
DISTRIBUTION_GAUSSIAN_RANGE = 2
DISTRIBUTION_GAUSSIAN_INVERSE = 3
DISTRIBUTION_GAUSSIAN_RANGE_INVERSE = 4

def random_get_instance():
    return 0

def random_new(algo=RNG_CMWC):
    return 0

def random_new_from_seed(seed, algo=RNG_CMWC):
    return 0

def random_set_distribution(rnd, dist) :
	donothing()

def random_get_int(rnd, mi, ma):
    return 0

def random_get_float(rnd, mi, ma):
    return 0

def random_get_double(rnd, mi, ma):
    return 0

def random_get_int_mean(rnd, mi, ma, mean):
    return 0

def random_get_float_mean(rnd, mi, ma, mean):
    return 0

def random_get_double_mean(rnd, mi, ma, mean):
    return 0

def random_save(rnd):
    return 0

def random_restore(rnd, backup):
    donothing()

def random_delete(rnd):
    donothing()

############################
# noise module
############################
NOISE_DEFAULT_HURST = 0.5
NOISE_DEFAULT_LACUNARITY = 2.0

NOISE_DEFAULT = 0
NOISE_PERLIN = 1
NOISE_SIMPLEX = 2
NOISE_WAVELET = 4

_NOISE_PACKER_FUNC = (None,
                      (c_float * 1),
                      (c_float * 2),
                      (c_float * 3),
                      (c_float * 4),
                      )

def noise_new(dim, h=NOISE_DEFAULT_HURST, l=NOISE_DEFAULT_LACUNARITY, random=0):
    return 0

def noise_set_type(n, typ) :
    donothing()

def noise_get(n, f, typ=NOISE_DEFAULT):
    return typ

def noise_get_fbm(n, f, oc, typ=NOISE_DEFAULT):
    return typ

def noise_get_turbulence(n, f, oc, typ=NOISE_DEFAULT):
    return typ

def noise_delete(n):
    donothing()

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
