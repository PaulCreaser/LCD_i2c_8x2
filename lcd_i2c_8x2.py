# coding: utf-8
import smbus
import time

class LCD_I2C:
    lcd_addr = 0x3E
    bus = None
    lookup = { ' ': 0x20, '!': 0x21, '\"': 0x22, '#': 0x23,
        '$': 0x24, '%': 0x25, '&': 0x26, '`': 0x27, '(': 0x28,
        '(': 0x29,
        '*': 0x2a, '+': 0x2b, ',': 0x2c, '-': 0x2d, '.': 0x2e,
        '/': 0x2f,
        '0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33,
        '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37, '8': 0x38, 
        '9': 0x39, ':': 0x3A, ';': 0x3B, '<': 0x3C, '=': 0x3D,
        '>': 0x3E, '?': 0x3F, '@': 0x40, 'A': 0x41 , 'B': 0x42,
        'C': 0x43, 'D': 0x44, 'E': 0x45, 'F': 0x46, 'G': 0x47,
        'H': 0x48, 'I': 0x49, 'J': 0x4A, 'K': 0x4B, 'L': 0x4C,
        'M': 0x4D, 'N': 0x4E, 'O': 0x4F, 'P': 0x50, 'Q': 0x51,
        'R': 0x52, 'S': 0x53, 'T': 0x54, 'U': 0x55, 'V': 0x56,
        'W': 0x57, 'X': 0x58, 'Y': 0x59, 'Z': 0x5A, '[': 0x5B,
        ']': 0x5D, '^': 0x5E, '_': 0x5F, '`': 0x60, 'a': 0x61,
        'b': 0x62, 'c': 0x63, 'd': 0x64, 'e': 0x65, 'f': 0x66,
        'g': 0x67, 'h': 0x68, 'i': 0x69, 'j': 0x6a, 'k': 0x6b,
        'l': 0x6c, 'm': 0x6d, 'n': 0x6e, 'o': 0x6f, 'p': 0x70,
        'q': 0x71, 'r': 0x72, 's': 0x73, 't': 0x74, 'u': 0x75,
        'v': 0x76, 'w': 0x77, 'x': 0x78, 'y': 0x79, 'z': 0x7a,
        '{': 0x7b, '|': 0x7c, '}': 0x7d,
	'ア':0xB1, 'イ':0xB2, 'ウ':0xB3, 'エ':0xB4, 'オ':0xB5,
	'カ':0xB6, 'キ':0xB7, 'ク':0xB8, 'ケ':0xB9, 'コ':0xBA,
	'サ':0xBB, 'シ':0xBC, 'ス':0xBD, 'セ':0xBE, 'ソ':0xBF,
	'タ':0xC0, 'チ':0xC1, 'ツ':0xC2, 'テ':0xC3, 'ト':0xC4,
	'ニ':0xC5, 'ナ':0xC6, 'ヌ':0xC7, 'ネ':0xC8, 'ノ':0xC9,
	'ハ':0xCA, 'ヒ':0xCB, 'フ':0xCC, 'ヘ':0xCD, 'ホ':0xCE,
	'マ':0xCF, 'ミ':0xD0, 'ム':0xD1, 'メ':0xD2, 'モ':0xD3,
	'ヤ':0xD4, 'ユ':0xD5, 'ヨ':0xD6, 'ラ':0xD7, 'リ':0xD8,
	'ル':0xD9, 'レ':0xDA, 'ロ':0xDB, 'ワ':0xDC, 'ン':0xDD,
	'”':0xDE,  '。':0xDF   };

    def init(self):
        self.bus = smbus.SMBus(1)
        self.on()

    def new_line(self):
        self.bus.write_byte_data(self.lcd_addr, 0x00, 0xc0)
        time.sleep(0.001)
        
    def on(self):
        self.bus.write_i2c_block_data(self.lcd_addr, 0x38, [0x39, 0x14, 0x70, 0x56, 0x6c])
        time.sleep(0.001)
        self.bus.write_i2c_block_data(self.lcd_addr, 0x38, [0x0d, 0x01])
        time.sleep(0.001)

    def off(self):
        self.bus.write_byte_data(self.lcd_addr, 0x00, 0x08)
        time.sleep(0.001)

    def cursor_on(self):
        self.bus.write_byte_data(self.lcd_addr, 0x00, 0x0D)
        time.sleep(0.001)

    def cursor_off(self):
        self.bus.write_byte_data(self.lcd_addr, 0x00, 0x0C)
        time.sleep(0.001)

    def cursor_blink_on(self):
        self.bus.write_byte_data(self.lcd_addr, 0x00, 0x0E)
        time.sleep(0.001)

    def cursor_blink_off(self):
        self.bus.write_byte_data(self.lcd_addr, 0x00, 0x0D)
        time.sleep(0.001)

    def home(self):
        self.bus.write_byte_data(self.lcd_addr, 0x00, 0x02)
        time.sleep(0.001)
        
    def clear(self):
        self.bus.write_byte_data(self.lcd_addr, 0x00, 0x01)
        time.sleep(0.001)

    def ascii_to_lcd(self, char):
        return self.lookup[char]

    def write_data(self, top_title, top_num, bot_title, bot_num):
        top_array = []
        top_num =  str(top_num)
        for char in top_title:
            top_array.append(self.ascii_to_lcd(char))
        for char in top_num:
            top_array.append(self.ascii_to_lcd(char))

        bot_array = []
        for char in bot_title:
            bot_array.append(self.ascii_to_lcd(char))
        bot_num = str(bot_num)
        for char in bot_num:
            bot_array.append(self.ascii_to_lcd(char))

        self.write(top_array, bot_array)

    def write_num(self, top_num,  bot_num):
        top_array = []
        top_num =  str(top_num)
        print "Top ",  top_num
        for char in top_num:
            top_array.append(self.ascii_to_lcd(char))

        bot_array = []
        bot_num = str(bot_num)
        for char in bot_num:
            bot_array.append(self.ascii_to_lcd(char))

        self.write(top_array, bot_array)

    def write(self, top, bottom):
        # TOP
        self.bus.write_i2c_block_data(self.lcd_addr, 0x40, top)
        time.sleep(0.001)
        # New line
        self.new_line()
        time.sleep(0.001)
        # Bottom Line
        self.bus.write_i2c_block_data(self.lcd_addr, 0x40,  bottom)
        time.sleep(0.001)

if __name__ == '__main__':
    mylcd = LCD_I2C()
    mylcd.init()
    mylcd.clear()
    mylcd.write_data("LON ", 12, "LAT ", 34)
    time.sleep(1)
    mylcd.home()
    time.sleep(1)
    mylcd.cursor_off()
    time.sleep(1)
    mylcd.cursor_on()
    time.sleep(1)
    mylcd.cursor_on()
    time.sleep(1)
    mylcd.cursor_blink_on()
    time.sleep(1)
    mylcd.cursor_blink_off()
    time.sleep(1)
    mylcd.clear()
    time.sleep(1)
    mylcd.on()
    time.sleep(1)
    mylcd.write_data("LON ", 12, "LAT ", 34)
    time.sleep(1)


