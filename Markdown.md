# Markdown

一种轻量级标记语言

*******

~~胡思乱想~~

<u>动用逻辑思考</u>

事物只不过是[^类]的延申

[^类]: 事物总体的抽象

## 一. 由来

- Markdown 语言在 2004 由约翰·格鲁伯（英语：John Gruber）创建

## 二. 功能

### 1. 标题（使用 **#** 号可表示 1-6 级标题） ###

# 一级标题  # #

## 二级标题  ## ##

### 三级标题  ###

#### 四级标题  ####

##### 五级标题  #####

###### 六级标题  ######

 ### 2. 段落格式   ###

1. 字体

   - ```mm
     *斜体文本*
     _斜体文本_
     **粗体文本**
     __粗体文本__
     ***粗斜体文本***
     ___粗斜体文本___
     ~~删除线~~
     <u>带下划线文本</u>
     ```

2. 分割号

   - ```
     ***
     
     * * *
     
     *****
     
     - - -
     
     ----------
     ```

3. 脚注[^1]

   [^1]: 附在文章页面的最底端的，对某些东西加以说明

   - ```
     [^注明的文本]。
     [^RUNOOB]: 解释
     ```

### 3. 列表 ###

1. 有序列表

   - ```
     1. 第一项
     2. 第二项
     3. 第三项
     ```

2. 无序列表

   > （使用**(*)/(**+**)/(**-**)**作为列表标记，后面要添加**一个空格**）

   - ```
     * 第一项
     + 第一项
     + 第二项
     - 第一项
     - 第二项
     - 第三项
     ```

3. 列表嵌套

   > (只需在子列表中的选项前面添加**四个空格**即可)

   - ```
     1. 第一项：
         - 第一个
         - 第二个
     2. 第二项：
         - 第一个
         - 第二个
     ```

### 4. 区块 ###

> (引用在段落开头使用**符号(>)** 后面一个**空格**)

1. 层级

   - > (> 最外层)
     >
     > > (> > 第一层嵌套)
     > >
     > > > (> > > 第二层嵌套)

2. 列表中使用区块

   > 1. 第一项
   >    - 第一项
   >    2. 第二项
   >    3. 第三项
   > 2. 第二项
   > 3. 第三项

3. 区块中使用列表

   - 第一项

     > Markdown
     >
     > 标记

   - 第二项

   3. 第三项

### 5. 代码 ###

> 函数或片段的代码可以用**反引号（**`**）**把它包起来

1. 函数

   > 代码区块使用 **4 个空格**或者一个**制表符（Tab 键）**

   - `print` 函数

2. 代码区块

   > **(```)**包裹一段代码，并指定一种语言（也可以不指定）

   ```python
   def baoshu(a,b):
       N=list(range(1,a+1))
       n=0
       while N.count("o")<a-1:
           for i in N:
               if i=="o":
                   continue
               n+=1
               if n==b:
                   N[i-1]="o"
                   n=0
       while N.count("o")!=0:
           N.remove("o")
       print(N[0])
   baoshu(50,3)
   ```

### 6. 链接 ###

1. 显示网站

   ```
   <链接地址>
   ```

   <https://www.baidu.com/>

2. 显示名称

   ```
   [链接名称](链接地址)
   ```

   [百度一下](https://www.baidu.com/)

3. 高级链接

   ```
   这个链接用 1 作为网址变量 [Google][1]
   这个链接用 runoob 作为网址变量 [Runoob][runoob]
   然后在文档的结尾为变量赋值（网址）
   
     [1]: http://www.google.com/
     [runoob]: http://www.runoob.com/
   ```

   这个链接用 1 作为网址变量 [Google][1]
   这个链接用 runoob 作为网址变量 [Runoob][runoob]
   然后在文档的结尾为变量赋值（网址）

   [1]: http://www.google.com/
   [runoob]: http://www.runoob.com/

### 7. 图片 ###

> - 开头一个感叹号 !
> - 接着一个方括号，里面放上图片的替代文字
> - 接着一个普通括号，里面放上图片的网址，最后还可以用引号包住并加上选择性的 'title' 属性的文字。

```
![alt 属性文本](图片地址)
![alt 属性文本](图片地址 "可选标题")
```

![alt sky](C:\Users\Administrator\Desktop\sky.jpg)

```
![RUNOOB 图片](图片地址 "可调大小")
```

<img src="C:\Users\Administrator\Desktop\class21-1-10.png" alt="RUNOOB string" style="zoom:25%;" />

可以用HTML

<img src="http://static.runoob.com/images/runoob-logo.png" width="50%">

这个链接用 1 作为网址变量 [RUNOOB][1].
然后在文档的结尾为变量赋值（网址）

[1]: http://static.runoob.com/images/runoob-logo.png

### 8. 表格 ###

> 制作表格使用 **(|)**  来分隔不同的单元格，使用 **(-)** 来分隔表头和其他行

```
|  表头   | 表头  |
|  ----  | ----  |
| 单元格  | 单元格 |
| 单元格  | 单元格 |
```

| 表头   | 表头   |
| ------ | ------ |
| 单元格 | 单元格 |
| 单元格 | 单元格 |

> - **(-:)** 设置内容和标题栏居右对齐
> - **(:-)** 设置内容和标题栏居左对齐
> - **(:-:)** 设置内容和标题栏居中对齐

```
| 左对齐 | 右对齐 | 居中对齐 |
| :-----| ----: | :----: |
| 单元格 | 单元格 | 单元格 |
| 单元格 | 单元格 | 单元格 |
```

| 左对齐 | 右对齐 | 居中对齐 |
| :----- | -----: | :------: |
| 单元格 | 单元格 |  单元格  |
| 单元格 | 单元格 |  单元格  |

### 9. 高级技巧 ###

1. 支持的 HTML 元素

   > 不在 Markdown 涵盖范围之内的标签，都可以直接在文档里面用 HTML 撰写。
   >
   > 目前支持的 HTML 元素有：`<kbd> <b> <i> <em> <sup> <sub> <br>`等 

   ```
   使用 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd> 重启电脑 
   ```

   使用 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd> 重启电脑

2. 转义

   > Markdown 使用了很多特殊符号来表示特定的意义，如果需要显示特定的符号则需要转义，Markdown 使用反斜杠(\)转义特殊字符

   ```
   **文本加粗** 
   \*\* 正常显示星号 \*\*
   ```

   **文本加粗** 
   \*\* 正常显示星号 \*\*

   以下这些符号前面加上反斜杠来插入普通的符号：

   ```
   \   反斜线
   `   反引号
   *   星号
   _   下划线
   {}  花括号
   []  方括号
   ()  小括号
   #   井字号
   +   加号
   -   减号
   .   英文句点
   !   感叹号
   ```

3. 公式

   > 插入数学公式时，可以使用两个美元符 **($$) **包裹 TeX 或 LaTeX 格式的数学公式来实现,问答和文章页会根据需要加载 Mathjax 对数学公式进行渲染

   ```
   $$
   \mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix} 
   \mathbf{i} & \mathbf{j} & \mathbf{k} \\
   \frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\
   \frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\
   \end{vmatrix}
   ${$tep1}{\style{visibility:hidden}{(x+1)(x+1)}}
   $$
   ```

   $$
   \mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix} 
   \mathbf{i} & \mathbf{j} & \mathbf{k} \\
   \frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\
   \frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\
   \end{vmatrix}
   ${$tep1}{\style{visibility:hidden}{(x+1)(x+1)}}
   $$

## 三. 应用 ##

Markdown 编写的文档可以导出 <u>*HTML*</u> 、<u>*Word*</u>、<u>*图像*</u>、<u>*PDF*</u>、<u>*Epub*</u> 等多种格式的文档。

Markdown 能被使用来撰写电子书，如：Gitbook。

当前许多网站都广泛使用 Markdown 来撰写帮助文档或是用于论坛上发表消息



