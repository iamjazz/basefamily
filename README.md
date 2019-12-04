## Base 全家桶编解码

### 基于base64模块编写

### 用法及安装
```
git clone https://github.com/iamjazz/pythonbase.git
cd pythonbase
```

```
python3 Decode.py  
请输入你想转码的编码：
1.Base64解码;
2.Base85解码;
3.Base16解码;
4.Base32解码;
请输入编号：1
请输入要解码的Base64编码:
```

```
python3 Encode.py  
请输入你想转码的编码：
1.Base64解码;
2.Base85解码;
3.Base16解码;
4.Base32解码;
请输入编号：1
请输入要编码的Base64编码:
```

### 用法事例
```
hudeMacBook-Pro:Base Family Bucket hu$ python3 Encode.py 
请输入你想转码的编码：
1.Base64编码;
2.Base85编码;
3.Base16编码;
4.Base32编码;
请输入编号：2
请输入要编码的Base85编码:ADMIN
编码后字符为: K}1bSP5

hudeMacBook-Pro:Base Family Bucket hu$ python3 Decode.py 
请输入你想转码的编码：
1.Base64解码;
2.Base85解码;
3.Base16解码;
4.Base32解码;
请输入编号：2
请输入要解码的Base85编码:K}1bSP5
解码后字符为: ADMIN
```
## 待补充
base58编解码
