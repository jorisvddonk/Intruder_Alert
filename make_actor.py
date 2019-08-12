#!/usr/bin/env python

import os
from shutil import copyfile
from orz_locdata import AMBIENT_ANIM
from PIL import Image
import glob
import re

INDIR = './sc2/orz/'
OUTDIR = "./out/"

ani = open('%sorz.ani' % INDIR, 'r')
texturesf = open('%sTEXTURES.txt' % (OUTDIR), 'w')
actorsf = open('%sanimActors.zsc' % OUTDIR, 'w')

os.makedirs(OUTDIR, exist_ok=True)


def getCode(x, basename):
    x0 = chr(65 + int(x / 26))
    x1 = chr(65 + int(x % 26))
    return "%s%s%s0" % (basename, x0, x1)


def copyShip(inglob, basename):
    retval = []
    for g in glob.glob('./sc2/ships/%s*.png' % inglob):
        m = re.search('%s(.*)\.png' % inglob.split('/').pop(), g)
        anglei = int(m.group(1))
        outImageCode = getCode(anglei, basename)
        outImage = "%s.png" % outImageCode
        inImagePath = g
        outImagePath = '%s%s' % (OUTDIR, outImage)
        if not (os.path.exists(outImagePath)):
            copyfile(inImagePath, outImagePath)
        angle = (360 / 16) * anglei
        retval.append({"angle": angle, "anglei": anglei,
                       "imageCode": outImageCode, "imagePath": outImagePath})
    return retval


def writeBasicSprite(spriteInfo, scale):
    im = Image.open(spriteInfo["imagePath"])
    width = im.size[0]
    height = im.size[1]
    sname = spriteInfo["imageCode"]
    texturesf.write('''Sprite %s, %s, %s {
    XSCALE %s
    YSCALE %s
    Offset %s, %s
    Patch %s, 0, 0
}

''' % (sname, width, height, scale, scale, int(width*0.5), int(height*0.5), sname))


n = 1
for anim in AMBIENT_ANIM:
    codes = []
    for i in range(anim["StartIndex"], anim["StartIndex"] + anim["NumFrames"]):
        codes.append(getCode(i, "ORZ"))
    if anim["AnimFlags"] == "YOYO_ANIM":
        print('yo yo')
        for i in range(anim["StartIndex"] + anim["NumFrames"] - 2, anim["StartIndex"], -1):
            codes.append(getCode(i, "ORZ"))
    if anim["AnimFlags"] == "RANDOM_ANIM":
        print('todo random')
    print(codes)
    print('--')
    actorsf.write('''
Class OrzAnim%s : Actor {
    Default {
        +WALLSPRITE;
    }
    States
    {
        Spawn:
            Goto Ready;
        Ready:
%s
            loop;
    }
}

''' % (n, '\n'.join(["%s %s 3;" % (x[:-2], x[4:5]) for x in codes])))
    n += 1

ZERO_IMG = Image.open('%s%s' % (INDIR, 'orz-000.png'))
IMG_ZERO_WIDTH = ZERO_IMG.size[0]
IMG_ZERO_HEIGHT = ZERO_IMG.size[1]


for line in ani.read().splitlines():
    splitted = line.split()
    x = int(splitted[0][4:7])
    outImageCode = getCode(x, "ORZ")
    outImage = "%s.png" % outImageCode
    inImagePath = '%s%s' % (INDIR, splitted[0])
    outImagePath = '%s%s' % (OUTDIR, outImage)
    if not (os.path.exists(outImagePath)):
        copyfile(inImagePath, outImagePath)
    im = Image.open(inImagePath)
    width = im.size[0]
    height = im.size[1]
    ox = int((IMG_ZERO_WIDTH * 0.5) + int(splitted[3])+0.5)
    oy = int((IMG_ZERO_HEIGHT * 1.0) + int(splitted[4]))
    texturesf.write('''Sprite %s, %s, %s {
    XSCALE 0.5
    YSCALE 0.5
    Offset %s, %s
    Patch %s, 0, 0
}

''' % (outImageCode, width, height, ox, oy, outImageCode))

actorsf.close()


nemesis_base_images = copyShip('orz/nemesis-big-', 'NMB')
nemesis_turret_images = copyShip('orz/turret-big-', 'NMT')
cruiser_images = copyShip('human/cruiser-big-', 'CRU')

for imginfo in cruiser_images:
    writeBasicSprite(imginfo, 2)

for imginfo in nemesis_base_images:
    writeBasicSprite(imginfo, 2)

for imginfo in nemesis_turret_images:
    writeBasicSprite(imginfo, 2)

for g in glob.glob('./out/SPA*.png'):
    im = Image.open(g)
    width = im.size[0]
    height = im.size[1]
    m = re.search('(SPA.*0)\.png', g)
    sname = m.group(1)
    texturesf.write('''Sprite %s, %s, %s {
    XSCALE 1.0
    YSCALE 1.0
    Offset %s, %s
    Patch %s, 0, 0
}

''' % (sname, width, height, int(width*0.5), int(height*0.5), sname))


texturesf.close()
