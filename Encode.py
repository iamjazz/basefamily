import base64
import base58
import base36
import base91
import base62
# -*- coding: utf-8 -*-
# Author:Jazz
print("请输入你想转码的编码:")
print("1.Base64编码;\n"
      "2.Base85编码;\n3.Base16编码;\n4.Base32编码;\n5.Base58编码;\n6.Base36编码;\n7.Base91编码;\n8.Base62编码;")
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
elif (sel == 5):
    s58 = str(input("请输入要编码的Base58编码:"))
    d58 = base58.b58encode(s58)
    check58 = str(d58, 'utf8')
    print ("编码后字符为:",check58)
elif (sel == 6):
    s36=input("请输入要编码的Base36编码:")
    d36=base36.loads(s36)
    print("编码后字符为:",d36)
elif (sel == 7):
    s91=input("请输入要编码的Base91编码:")
    d91=base91.encode(str.encode(s91))
    print("编码后字符为:",d91)
elif (sel == 8):
    s62=int(input("请输入要编码码的Base62编码:"))
    d62 = base62.encode(s62)
    assert type(s62) == int
    print("编码后字符为:",d62)
