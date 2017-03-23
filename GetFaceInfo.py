# -*- coding: UTF-8 -*-
import os,sys
from FaceDec import *
reload(sys)
sys.setdefaultencoding('utf-8')

fd = FaceDectect()
fd.load_Face()
fd.changeFaceset('Test1')
fd.getFaceInfo('2.png')