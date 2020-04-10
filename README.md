## Base 全家桶编解码(自动识别并解码)
### 运行环境：Python3
#### 写这个巨垃圾脚本的原因：
```
1.渗透测试环境中，url的GET/POST请求中一些编码转换以及cookies中的某些参数值
2.CTF比赛中也能遇到一些乱七八糟的的base全家桶
3.有实战场景中见过一些编码用base62解码之后是userid  --->越权
```
#### 实现原理：
```
没啥原理
就是先判断输入的字符串是不是int型，如果是int型就用base36和base16去解码
base64 58 85 32 91 都不能解数字，再从input里做逐级判断(嵌套异常处理)
base62既能够解码int又能够解码str
懒得写函数套用了，毕竟本身技术要求就不高
```
### 注：
全自动识别解密的脚本返回值仅供参考，具体请用Decode.py和Encode.py往复测试
#### 新增
编解码方式

    1.Base58
    
    2.Base36
    
    3.Base91
    
    4.Base62
#### 新增全自动识别编码并解密
用法：
```
python3 auto.py
```
### 安装模块
```
git clone https://github.com/iamjazz/pythonbase.git
cd pythonbase
pip3 install -r requirements.txt
```


### 用法事例
```
全自动：

python3 test.py
请输入你想全自动解码的编码：BzgdpCQ
Base58解码后字符为: asdfa
OK

编码：
hudeMacBook-Pro:Base Family Bucket hu$ python3 Encode.py 
请输入你想转码的编码：
1.Base64编码;
2.Base85编码;
3.Base16编码;
4.Base32编码;
5.Base58编码;
6.Base36编码;
7.Base91编码;
8.Base62编码;

请输入编号：2
请输入要编码的Base85编码:ADMIN
编码后字符为: K}1bSP5

解码：
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

1.~~base全家桶识别脚本  Eg:输入字符串 K}1bSP5 识别为Base85编码格式~~

2.~~编码、解码、识别 融为一体~~

3.~~小bug:少许编码有同一解造成没有完全识别 Eg:字符串“1241”经过编码后是字符串"K1",auto解的时候，base85解出了 "K1"->">" 而没有进行到base62解密~~
4.上面那一条，我把base85和base62放一起输出暂时解决了
## 结语
##### 自动化识别没啥大bug了，凑合凑合结合着Decode.py用

##### 代码是真的垃圾，为了让识别逻辑更严谨，我竟然嵌套了十几层异常处理
