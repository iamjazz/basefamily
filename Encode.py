import base64
# -*- coding: utf-8 -*-
# Author:Jazz
print("请输入你想转码的编码：")
print("1.Base64编码;\n"
      "2.Base85编码;\n3.Base16编码;\n4.Base32编码;")
sel=int(input("请输入编号："))
if(sel==1):
    s64 = str(input("请输入要编码的Base64编码:"))
    b3 = s64.encode (encoding = "utf-8")
    d64 = base64.b64encode(b3)
    check64 = str(d64, 'utf8')
    print ("编码后字符为:",check64)
elif(sel==2):
    s85 = str(input("请输入要编码的Base85编码:"))
    b3 = s85.encode (encoding = "utf-8")
    d85 = base64.b85encode(b3)
    check85 = str(d85, 'utf8')
    print ("编码后字符为:",check85)
elif(sel==3):
    s16 = str(input("请输入要编码的Base16编码:"))
    b3 = s16.encode (encoding = "utf-8")
    d16 = base64.b16encode(b3)
    check16 = str(d16, 'utf8')
    print ("编码后字符为:", check16)
elif (sel == 4):
    s32 = str(input("请输入要编码的Base32编码:"))
    b3 = s32.encode (encoding = "utf-8")
    d32 = base64.b32encode(b3)
    check32 = str(d32, 'utf8')
    print ("编码后字符为:",check32)

