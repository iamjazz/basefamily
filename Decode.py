import base64
# -*- coding: utf-8 -*-
# Author:Jazz
print("请输入你想转码的编码：")
print("1.Base64解码;\n"
      "2.Base85解码;\n3.Base16解码;\n4.Base32解码;")
sel=int(input("请输入编号："))
if(sel==1):
    s64 = str(input("请输入要解码的Base64编码:"))
    d64 = base64.b64decode(s64)
    check64 = str(d64, 'utf8')
    print ("解码后字符为:",check64)
elif(sel==2):

    s85 = str(input("请输入要解码的Base85编码:"))
    d85 = base64.b85decode(s85)
    check85 = str(d85, 'utf8')
    print ("解码后字符为:",check85)
elif(sel==3):
    s16 = str(input("请输入要解码的Base16编码:"))
    d16 = base64.b16decode(s16)
    check16 = str(d16, 'utf8')
    print ("解码后字符为:",check16)
elif (sel == 4):
    s32 = str(input("请输入要解码的Base32编码:"))
    d32 = base64.b32decode(s32)
    check32 = str(d32, 'utf8')
    print ("解码后字符为:",check32)
