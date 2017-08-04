# -*- coding: utf-8 -*-
from PIL import Image,ImageDraw,ImageFont
import random
import math, string
import logging
# logger = logging.Logger(name='gen verification')

class RandomChar():
    @staticmethod
    def Unicode():
        val = random.randint(0x4E00, 0x9FBF)
        return unichr(val)    

    @staticmethod
    def GB2312():
        head = random.randint(0xB0, 0xCF)
        body = random.randint(0xA, 0xF)
        tail = random.randint(0, 0xF)
        val = ( head << 8 ) | (body << 4) | tail
        s = val.to_bytes(2, byteorder='big').decode('gb2312')  
        # s = "%x" % val
        print(s);
        return s    
        # return s;

class ImageChar():
    def __init__(self, fontColor = (0, 0, 0),
    size = (100, 40),
    fontPath = 'resource/simkai.ttf',
    bgColor = (255, 255, 255),
    fontSize = 20):
        self.size = size
        self.fontPath = fontPath
        self.bgColor = bgColor
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.font = ImageFont.truetype(self.fontPath, self.fontSize)
        self.image = Image.new('RGB', size, bgColor)

    def drawText(self, pos, txt, fill):
        draw = ImageDraw.Draw(self.image)
        draw.text(pos, txt, font=self.font, fill=fill)
        del draw    

    def drawTextV2(self, pos, txt, fill, angle=180):
        image=Image.new('RGB', (25,25), (255,255,255))
        draw = ImageDraw.Draw(image)
        draw.text( (0, -3), txt,  font=self.font, fill=fill)
        w=image.rotate(angle,  expand=1)
        self.image.paste(w, box=pos)
        del draw

    def randRGB(self):
        return (0,0,0)

    def randChinese(self, num):
        gap = 1
        start = 0
        # num_flip_list = random.sample(range(num), num_flip)
        # logger.info('num flip list:{0}'.format(num_flip_list))
        # print 'num flip list:{0}'.format(num_flip_list)
        char_list = []
        for i in range(0, num):
            char = RandomChar().GB2312()
            char_list.append(char)
            x = start + self.fontSize * i + gap + gap * i
            self.drawTextV2((x, 6), char, self.randRGB(),0)
            # if i in num_flip_list:
            #     self.drawTextV2((x, 6), char, self.randRGB())
            # else:
            #     self.drawText((x, 0), char, self.randRGB())
        return char_list
    def save(self, path):
        self.image.save(path)



err_num = 0
for i in range(1):
    try:
        ic = ImageChar(fontColor=(100,211, 90), size=(60,23), fontSize = 18)
        word = '口哨'
        ic.drawText((2,2),word,(0, 0, 0))
        # char_list = ic.randChinese(3)
        ic.save(word+".jpeg")
    except  Exception as err:
        print(err)
        err_num += 1
        continue