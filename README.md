# ProGuardDictionary  

Android ProGuard 混淆字典生成脚本

## 生成字典

```bash
python main.py
```

[main.py](https://github.com/wuxiaosu/ProGuardDictionary/blob/master/main.py)

可以根据自己的需求自己设定 key

## 使用  

在 proguard-rules.pro 中添加  

```bash
-obfuscationdictionary dict.txt
-classobfuscationdictionary dict.txt
-packageobfuscationdictionary dict.txt
```

## 效果图

![1.png](https://raw.githubusercontent.com/wuxiaosu/ProGuardDictionary/master/imgs/1.png)

## 几个现成的

[dict_1.txt](https://github.com/wuxiaosu/ProGuardDictionary/blob/master/dict_1.txt)  
[dict_2.txt](https://github.com/wuxiaosu/ProGuardDictionary/blob/master/dict_2.txt)  
[dict_3.txt](https://github.com/wuxiaosu/ProGuardDictionary/blob/master/dict_3.txt)  
[dict_4.txt](https://github.com/wuxiaosu/ProGuardDictionary/blob/master/dict_4.txt)  

![2.png](https://raw.githubusercontent.com/wuxiaosu/ProGuardDictionary/master/imgs/2.png)
