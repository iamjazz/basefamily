## Base 全家桶编解码
### 本程序采用Python3编写
### 更新
#### 新增编解码
    1.Base58
    
    2.Base36
    
    3.Base91
    
    4.Base62

### 用法及安装
```
git clone https://github.com/iamjazz/pythonbase.git
cd pythonbase
pip3 install -r requirements.txt
```


### 用法事例
```
hudeMacBook-Pro:Base Family Bucket hu$ python3 Encode.py 
请输入你想转码的编码：
1.Base64编码;
2.Base85编码;
3.Base16编码;
4.Base32编码;
5.Base58编码;
6.Base36编码;
7.Base91解码;
8.Base62解码;

请输入编号：2
请输入要编码的Base85编码:ADMIN
编码后字符为: K}1bSP5

hudeMacBook-Pro:Base Family Bucket hu$ python3 Decode.py 
请输入你想转码的编码：
1.Base64解码;
2.Base85解码;
3.Base16解码;
4.Base32解码;
5.Base58解码;
6.Base36解码;
7.Base91解码;
8.Base62解码;
请输入编号：2
请输入要解码的Base85编码:K}1bSP5
解码后字符为: ADMIN
```
## 待补充

base全家桶识别脚本  Eg:输入字符串 K}1bSP5 识别为Base85编码格式

编码、解码、识别 融为一体
