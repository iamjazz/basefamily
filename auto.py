import base64
import base58
import base36
import base91
import base62
# -*- coding: utf-8 -*-
# Author:Jazz

autodecode=input("请输入你想全自动解码的编码：")
if autodecode.isdigit():
    try:
        try:
            s36=int(autodecode)
            assert type(s36) == int
            d36=base36.dumps(s36)
            print("Base36解码后字符为:",d36)
            s16 = str(autodecode)
            d16 = base64.b16decode(s16)
            check16 = str(d16, 'utf8')
            print ("Base16解码后字符为:",check16)
            s62=autodecode
            d62=base62.decode(s62)
            print("Base62解码后字符为:", d62)
        except:
            s16 = str(autodecode)
            d16 = base64.b16decode(s16)
            check16 = str(d16, 'utf8')
            print ("Base16解码后字符为:",check16)
            s62=autodecode
            d62=base62.decode(s62)
            print("Base62解码后字符为:", d62)
    except:
        s62=autodecode
        d62=base62.decode(s62)
        print("Base62解码后字符为:", d62)
else:    
    try:
        try:
            try:
                try:
                    try:
                        try:
                            try:
                                try:
                                    try:
                                        try:
                                            try:
                                                try:
                                                    try:
                                                        try:
                                                            try:
                                                                try:
                                                                    try:
                                                                        s64 = str(autodecode)
                                                                        d64 = base64.b64decode(s64)
                                                                        check64 = str(d64, 'utf8')
                                                                        print ("Base64解码后字符为:",check64)
                                                                    except:
                                                                        s85 = str(autodecode)
                                                                        d85 = base64.b85decode(s85)
                                                                        check85 = str(d85, 'utf8')
                                                                        print ("Base85解码后字符为:",check85)
                                                                        s62=autodecode
                                                                        d62=base62.decode(s62)
                                                                        print("Base61解码后字符为:", d62)
                                                                except:    
                                                                    s58 = str(autodecode)
                                                                    d58 = base58.b58decode(s58)
                                                                    check58 = str(d58, 'utf8')
                                                                    print ("Base58解码后字符为:",check58)
                                                            except:
                                                                s58 = str(autodecode)
                                                                d58 = base58.b58decode(s58)
                                                                check58 = str(d58, 'utf8')
                                                                print ("Base58解码后字符为:",check58)
                                                        except:
                                                            s91=autodecode
                                                            d91=base91.decode(s91)
                                                            check91 = str(d91, 'utf8')
                                                            print("Base91解码后字符为:",check91)
                                                    except:
                                                        s32 = str(autodecode)
                                                        d32 = base64.b32decode(s32)
                                                        check32 = str(d32, 'utf8')
                                                        print ("Base32解码后字符为:",check32)
                                                except:
                                                    s85 = str(autodecode)
                                                    d85 = base64.b85decode(s85)
                                                    check85 = str(d85, 'utf8')
                                                    print ("Base85解码后字符为:",check85)
                                            except:
                                                s58 = str(autodecode)
                                                d58 = base58.b58decode(s58)
                                                check58 = str(d58, 'utf8')
                                                print ("Base58解码后字符为:",check58)
                                        except:
                                            s58 = str(autodecode)
                                            d58 = base58.b58decode(s58)
                                            check58 = str(d58, 'utf8')
                                            print ("Base58解码后字符为:",check58)
                                    except:
                                        s91=autodecode
                                        d91=base91.decode(s91)
                                        check91 = str(d91, 'utf8')
                                        print("Base91解码后字符为:",check91)
                                except:
                                    s32 = str(autodecode)
                                    d32 = base64.b32decode(s32)
                                    check32 = str(d32, 'utf8')
                                    print ("Base32解码后字符为:",check32)
                            except:
                                s58 = str(autodecode)
                                d58 = base58.b58decode(s58)
                                check58 = str(d58, 'utf8')
                                print ("Base58解码后字符为:",check58)
                        except:
                            s91=autodecode
                            d91=base91.decode(s91)
                            check91 = str(d91, 'utf8')
                            print("Base91解码后字符为:",check91)
                    except:
                        s32 = str(autodecode)
                        d32 = base64.b32decode(s32)
                        check32 = str(d32, 'utf8')
                        print ("Base32解码后字符为:",check32)
                except:
                    s91=autodecode
                    d91=base91.decode(s91)
                    check91 = str(d91, 'utf8')
                    print("Base91解码后字符为:",check91)
            except:
                s32 = str(autodecode)
                d32 = base64.b32decode(s32)
                check32 = str(d32, 'utf8')
                print ("Base32解码后字符为:",check32)
        except:
            s32 = str(autodecode)
            d32 = base64.b32decode(s32)
            check32 = str(d32, 'utf8')
            print ("Base32解码后字符为:",check32)
    except:
        s62=autodecode
        d62=base62.decode(s62)
        print("Base62解码后字符为:", d62)
