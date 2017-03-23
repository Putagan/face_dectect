# -*- coding: UTF-8 -*-
import os,sys
from FaceDec import *
reload(sys)
sys.setdefaultencoding('utf-8')

fd = FaceDectect()
fd.delete_Faceset('Test1')
fd.changeFaceset('Test1')
# 一次只能上传5个人脸tokens
for root,dirs,files in os.walk("./data"):
    for file_name in files:
        file_path = root+"/"+file_name
        print file_path
        try:
            fd.addFaceToSet(file_path,file_name[:-4])
        except Exception as e:
            print "非法路径!"
        
        # os.system("say -v Ting-Ting %s"%file_name[:-12])

fd.addFaceToInternet()
fd.save_Face()
