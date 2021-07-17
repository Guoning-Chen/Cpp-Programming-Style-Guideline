# 6 布局和注释

## 6.1 布局

| 71. 【should】基本缩进的大小应该是2。 |
| :--- |
| `for (i = 0; i < nElements; i++)`<br>`··a[i] = 0;` |
| 1格缩进太小，不足以强调代码的逻辑结构。4格以上的缩进使得多层嵌套的代码难以阅读，同时增加了被迫换行的可能性。在2、3、4中，2格缩进和4格缩进最常见，而2格缩进能够减少了被迫换行的可能性。 |

| 72. 【should，must】代码块的布局应该参考下面的样例1（推荐）或样例2，禁止像样例3这样。函数体和类必须使用样例2的布局。 |
| :----------------------------------------------------------- |
| 【样例1】<br>`while (!done) {`<br>`··doSomething();`<br>`··done = moreTODO();`<br>`}`<br>【样例2】<br>`while (!done)`<br>`{`<br>`··doSomething();`<br/>`··done = moreTODO();`<br/>`}`<br>【样例3】<br>`while (!done)`<br/>`··{`<br/>`····doSomething();`<br/>`····done = moreTODO();`<br/>`··}`<br/> |
| 样例3引入了额外的缩进级别，导致代码结构不如样例1和样例2那么清晰。 |

| 73. 【should】`class`声明应该采用如下格式： |
| :--- |
| `class SomeClass : public BaseClass`<br>`{`<br>`public:`<br>`··...`<br>`protected:`<br/>`··...`<br/>`private:`<br/>`··...`<br/>`}` |
| 该格式符合上述的代码块通用格式。 |

| 74. 【should】方法的定义应该采用以下格式： |
| :--- |
| `void someMethod()`<br>`{`<br>`··...`<br>`}` |
| 该格式符合上述的代码块通用格式。 |

| 75.【should】 `if-else` 之类的语句应该采用如下格式： |
| :--- |
| `if (条件表达式) {`<br>`··语句;`<br>`}`<br><br>`if (条件表达式) {`<br/>`··语句;`<br/>`}`<br/>`else {`<br>`··语句;`<br/>`}`<br/><br>`if (条件表达式) {`<br/>`··语句;`<br/>`}`<br/>`else if (条件表达式) {`<br/>`··语句;`<br/>`}`<br/>`else {`<br/>`··语句;`<br/>`}`<br/> |
| 该格式符合上述的代码块通用格式。但有待讨论的是，`else`语句是否应该和前面`if`或`else if`语句的右花括号在同一行，像这样： <br>`if (条件表达式) {`<br/>`··语句;`<br/>`} else {`<br/>`··语句;`<br/>`}`<br/> 我们推荐的写法比这种写法要好，这是因为前者的`if`、`else`、`else if`等分支在文件单独成行，使得编辑它们比较容易，例如删除某个分支。 |

| 76. 【should】 `for` 应该采用如下格式： |
| :--- |
| `for (初始化; 条件表达式; 更新) {`<br>`··语句;`<br>`}` |
| 该格式符合上述的代码块通用格式。 |

| 77. 【should】空的 `for`语句应该采用如下格式： |
| :--- |
| `for (初始化; 条件表达式; 更新) {`<br/>`··;` |
| 该格式强调循环体是空的，并告诉读者是有意为之。不过事实上应该避免使用空循环。 |

| 78. 【should】 `while`语句应该采用如下格式： |
| :--- |
| `while (条件表达式) {`<br>`··语句;`<br>`}` |
| 该格式符合上述的代码块通用格式。 |

| 79. 【should】 `do-while` 语句应该采用如下格式： |
| :--- |
| `do {`<br>`··语句;`<br>`} while (条件表达式)` |
| 该格式符合上述的代码块通用格式。 |

| 80. 【should】 `switch` 语句应该采用如下格式： |
| :--- |
| `switch (条件表达式) {`<br>`··case ABC :`<br>`····语句;`<br>`····// fallthrough`<br><br>`··case DEF :`<br/>`····语句;`<br/>`····break;`<br/><br/>`··case XYZ :`<br/>`····语句;`<br/>`····break;`<br/><br>`··default :`<br/>`····语句;`<br/>`····break;`<br/>`}` |
| 注意每个`case`分支的整体都相对于`switch`语句都有一级缩进。这样就突出了整个`switch`语句。还有注意`:`前有一个空格。只要某个`case`分支没有`break`语句，都应该加上`// Fallthrough`注释。漏掉`break`语句是很常见的错误，如果缺少了`break`语句，应该清楚地表明是故意为之。 |

> 【译注】fall through：原意为落空、失败，中文注释时可以写成`// 继续执行`。

| 81. 【should】 `try-catch` 语句应该采用如下格式： |
| :--- |
| `try {`<br>`··语句;`<br>`}`<br>`catch (Exception& exception) {`<br>`··语句;`<br>`}` |
| 该格式符合上述的代码块通用格式。第75条讨论的`if-else`语句中右花括号的问题同样适用于`try-catch`语句。 |

| 82. 【can】仅包含一条语句的 `if-else`、 `for` 、 `while` 语句可以不加大括号。 |
| :----------------------------------------------------------- |
| `if (条件表达式)`<br>`··单条语句;`<br><br>`while (条件表达式)`<br/>`··单条语句;`<br/><br>`for (初始化; 条件表达式; 更新)`<br/>`··单条语句;` |
| 通常推荐无论任何时候都加大括号。但是花括号经常用于组合多条语句，对于单个语句来说是多余的。反对这种做法的一个常见理由是：如果添加新的语句却忘了加括号，容易导致程序出错。但是通常情况下，写代码时永远不应该适应将来可能出现的变化。 |

| 83. 【can】函数返回值可以放在紧邻函数名的上一行。 |
| :--- |
| `void`<br>`MyClass::myMethod(void)`<br>`{`<br>`··:`<br>`}` |
| 这样更容易定位到文件中的函数名，因为它们都在行首。 |

## 6.2 空格

| 84. 【should】 <br> - 传统运算符两边都应该有1个空格 <br> - C++保留字、逗号（`,`）、冒号（`:`）、`for`语句中的分号（`;`）之后都应该有1个空格 |
| :----------------------------------------------------------- |
| `a = (b + c) * d;`<br>而不是<br>`a=(b+c)*d`<br><br>`while (true)`<br>而不是<br>`while(true)`<br/><br>`doSomething (a, b, c, d);`<br>而不是<br>`doSomething (a, b, c, d);`<br><br>`case 100 :`（`:`左右都有空格） <br>而不是<br>`case 100:`<br><br>`for (i = 0; i < 10; i++)`<br>而不是<br>`for(i=0;i<10;i++)` |
| 突出语句中每个独立的部分。提高可读性。虽然很难给出在C++中使用空格的完整建议，但上述例子给出了大致的思路。 |

| 85. 【can】如果函数的参数列表非空，函数名之后可以加一个空格。 |
| :--- |
| `doSomething (currentFile);` |
| 突出函数名，从而提高可读性。如果函数列表为空，可以不加空格（例如`doSomething()`），因为这时函数名已经足够显眼。 另一种做法是在左括号之后加一个空格。采用这种做法的人通常也会在右括号之前加一个空格：`doSomething( currentFile );`。这样确实也能突出函数名，但右括号之前的空格显得太刻意，不加的话 \(像`doSomething( currentFile);`\)语句看起来又不对称。 |

| 86. 【should】同一个代码块中的逻辑单元应该用空行分隔开。 |
| :--- |
| `Matrix4x4 matrix = new Matrix4x4();`<br><br>`double cosAngle = Math.cos(angle);`<br>`double sinAngle = Math.sin(angle);`<br/><br>`matrixl.setElement(1, 1,  cosAngle);`<br>`matrixl.setElement(1, 2,  sinAngle);`<br/>`matrixl.setElement(2, 1, -sinAngle);`<br/>`matrixl.setElement(2, 2,  cosAngle);`<br/><br>`multiply(matrix);` |
| 通过在逻辑单元间插入空行来提高可读性。 |

| 87. 【should】类的成员函数应该用3行空行分隔。 |
| :--- |
| 无 |
| 使（类成员函数之间的）空白区域大于函数体内的空白区域，从而在类中突出它们。 |

| 88. 【can】声明时的变量可以左对齐。 |
| :--- |
| `AsciiFile* file;`<br>`int        nPoints;`<br>`float      x, y;` |
| 提高可读性。通过对齐容易区分类型名称和变量名称。 |

| 89. 【can】任何能够提高可读性的对齐都可以使用。 |
| :--- |
| `if      (a == lowValue)  computeSomething(); `<br>`else if  (a == mediumValue) computeSomething(); `<br/>`else if  (a == highValue) computeSomethingElseYet(); `<br/><br>`value = (potential        * oilDensity)   / constant1 +`<br>`········(depth            * waterDensity) / constant2 +`<br/>`········(zCoordinateValue * gasDensity)   / constant3;`<br/><br>`minPosition     = computeDistance(min,     x, y, z);`<br>`averagePosition = computeDistance(average, x, y, z);`<br/><br>`switch (value) {` <br>`··case PHASE_OIL   : strcpy(phase, "Oil");   break;`<br>`··case PHASE_WATER : strcpy(phase, "Water"); break;`<br/>`··case PHASE_GAS   : strcpy(phase, "Gas");   break;`<br/>`}` |
| 代码中有很多位置都可以利用空格提高可读性，即使违反了上述的某些建议。其中许多情形都需要使用对齐。虽然很难给出关于代码对齐的通用建议，但上面的这些例子提供了通用的思路。 |

## 6.3 注释

| 90. 【should】棘手的代码不应该注释，而是直接重写！\[1\] |
| :--- |
| 无 |
| 通常，应该通过选择合适的名称和清晰的逻辑结构使得代码的含义不言自明，从而减少注释。 |

| 91. 【should】所有注释都应该用英语。 \[2\] |
| :--- |
| 无 |
| 在国际化环境下，英语是最适合的语言。 |

| 92.  所有注释都应该用`//`（行注释），即使有多行。 |
| :--- |
| `// 横跨多行`<br>`// 的注释` |
| 由于不支持<u>多级C‐commenting</u>，使用行注释总是能够保证在调试时可以通过`/**/`注释掉整块代码。 |

| 93. 【should】注释的位置应该和被注释对象保持一致 \[1\] |
| :--- |
| `while (true) {`<br>`··// 注释`<br>`··something();`<br>`}`<br>而不是<br>`while (true) {`<br/>`// 注释`<br/>`··something();`<br/>`}`<br/> |
| 这样做是为了避免注释破坏代码原本的逻辑结构。 |

| 94. 【should】类和方法的头文件的注释应该遵循 JavaDoc 的惯例。 |
| :--- |
| 无 |
| 说到类和方法的标准化文档，Java开发社区中比C/C++更成熟。这是因为标准且自动化的Javadoc已经成为开发工具的一部分，并且有助于根据注释生成高质量的超文本文档。 C++也有类似于Javadoc的工具，它们采用和Javadoc相同的标记语法，例如 [Doc++](http://www.zib.de/Visual/software/doc++/) or [Doxygen](http://www.stack.nl/~dimitri/doxygen/index.html)。 |

