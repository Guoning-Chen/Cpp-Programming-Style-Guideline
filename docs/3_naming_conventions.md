# 3 命名规范

## 3.1 通用命名规范

| 3. 【must】类型的名称中所有单词的首字母必须大写。 |
| :--- |
| `Line`，`SavingAccount` |
| C++开发社区中的通用做法。 |

| 4. 【must】变量名中的第一个单词必须小写，其余大写。 |
| :--- |
| `line`，`savingAcount` |
| C++开发社区中的通用做法。使得变量区别于各种类的名称，有效解决如`Line line`这种声明中潜在的命名冲突。 |

| 5. 【must】常量（包括枚举量）的名称中所有字母都必须大写，并用下划线分开。 |
| :----------------------------------------------------------- |
| `MAX_ITERATIONS`，`COLOR_RED`，`PI`                          |
| C++开发社区中的通用做法。通常应该尽可能避免使用常量。在大部分情况下，用函数代替是更好的选择： <br>`int getMaxIterations()`<br>`{`<br>`  ··return 25;`<br>`}`<br>用来代替`MAX_ITERATIONS = 25`<br>这样既容易阅读，又能保证和类的成员变量统一接口。 |



| 6. 【must】方法或函数的名称必须包含动词且首字母小写、其余大写。 |
| :--- |
| `getName()`，`computeTotalWidth()` |
| C++开发社区中的通用做法。虽然和变量的命名方式相同，但函数本身的特征已经足以将它和变量区别开来。 |

| 7. 【should】命名空间的名称中的字母应该全部小写。 |
| :--- |
| `model::analyzer`，`io::iomanager`，`common::math::geometry` |
| C++开发社区中的通用做法。 |

| 8. 【should】模板类的名称应该是一个大写英文字母。 |
| :--- |
| `template<class T> ...` <br>`template<class C, class D> ...` |
| C++开发社区中的通用做法。使得模板类的名称比其它名称都要显眼。 |

| 9.  【must】当用于命名的时候，缩写词汇只有首字母可以大写 \[4\] |
| :--- |
| 使用`exportHtmlSource();`，而不是`exportHTMLSource();`<br>使用`openDvdPlayer();`，而不是`openDVDPlayer();` |
| 如果将缩写词全部大写，将会破坏上述命名规范。相应类型的变量就只能命名为`dVD`，`hTML`等等，可读性显然不好。另一个问题在例子中已经说明：当名称中包含多个单词的时候，（如果将缩写词全部大写）可读性会严重降低，不再容易分辨出缩写词之后的单词。 |

| 10. 【should】应该一直通过 :: 操作符来使用全局变量。 |
| :--- |
| `::nameWindow.open()`，`::applicationContext.getNmae()` |
| 通常应该减少使用全局变量。考虑用单例对象来代替。 |

| 11. 【should】类的私有成员应该加下划线。                     |
| :----------------------------------------------------------- |
| `class SomeClass {`<br>`··private:`<br>`····int length_;`<br>`}` |
| 除了名称和类型之外，变量的**作用域**是最重要的特征。利用下划线来表明其作用域容易将类的成员变量和本地变量区别开来。这之所以很关键是因为类的成员变量比成员函数更重要，要特殊对待。<br>使用下划线带来的另一个好处是可以很好地解决如何给<u>setter</u>和构造函数的参数命名的问题：<br>`void setDepth (int depth)`<br>`{`<br>`··depth_ = depth;`<br>`}`<br>将下划线作为前缀还是后缀是个问题。这两种做法都很常见，但更推荐后者，因为似乎最完整地保留了名称的可读性。<br>值得注意的是——区分变量的作用域很久以来都是有争议的话题。不过现在这种做法似乎正逐渐被人们所接受，在专业开发社区中正逐渐成为一种惯例。 |

> 【译注】setter：目测是指给类中的成员变量赋值的一类成员函数

| 12. 【should】<u>通用变量</u>的名称应该和它的类型相同。      |
| :----------------------------------------------------------- |
|                                                              |
| 通过减少术语和名称的数量来降低代码的复杂度。同时根据变量名就很容易推断出它所属的类。<br>如果因为一些原因，该惯例**并不适合**你使用的场景，这很可能说明你选择了一个不合适的类名。<br>非通用变量通常扮演某种**角色**，通常可以结合他们各自的角色和所属的类给他们命名：<br>`Point   startingPoint, centerPoint;`<br>`Name    LoginName;` |

[^通用变量]: 我理解为出现在多个函数的参数列表中的形参

| 13. 【should】所有名称都应该用英文。 |
| ------------------------------------ |
| 使用`fileName;`，而不是`fileNavn`。  |
| 英语更加适合国际化开发。             |

| 14. 【should】作用域比较大的变量应该用长名字，作用域小的用段名字。 |
| :--- |
| 无 |
| 用于临时存储或索引的变量应该尽量短。程序员看到这样的变量应该可以假定其作用域不超过几行代码。用于整数的通用变量可以是`i`, `j`, `k`, `m`, `n`，对于字符常用`c`和`d`。 |

| 15. 【should】类方法中应该避免出现对象的名称。 |
| :--- |
| 使用`line.getLength();`，而不是`line.getLineLength();` |
| 如样例所示，后者虽然在类的定义中看起来很自然，但使用时显得多余。 |

## 3.2 特殊的命名规范

| 17. 【must】直接访问类的属性必须使用术语get或set。 |
| :--- |
| `employee.getName();`<br>`employee.setName(name);`<br><br>`matrix.getElement(2, 4);`<br>`matrix.setElement(2, 4, value);` |
| C++开发社区的常用做法。在Java中这种命名惯例已经多少成为了一种标准。 |

| 18. 【can】当计算某样东西时可以使用术语compute。 |
| :--- |
| `valueSet->computeAverage();`<br>`matrix->computeInverse();` |
| 明确提醒读者这很可能是一个消耗时间的运算，如果重复运行，可能需要考虑缓存计算结果。一致地使用该术语可以提高程序可读性。 |

| 19. 【can】当查找某样东西时可以在类方法中使用术语find。 |
| :--- |
| `vertex.findNearestVertex();`<br>`matrix.findMinElement();` |
| 明确提醒读者这是一个运算量较少的查找操作。一致使用该术语可以提高程序可读性。 |

| 20. 【can】当新建对象或concept时可以使用术语initialize。     |
| :----------------------------------------------------------- |
| `printer.initializeFontSet();`                               |
| 美式的`initialize`好于英式的`initialise`。应该避免用`init`。 |

| 21. 【should】代表GUI控件的变量应该用组件类型作为后缀。 |
| :--- |
| `mianWindow`，`porpertiesDialog`，`widthScale`，`loginText`，`leftScrollbar`，`mainForm`，`fileMenu`，`minLabel`，`exitButton`，`yesToggle`等等。 |
| 让用户立刻明白变量的类型和对象资源，从而提高代码可读性。 |

| 22. 【should】代表一组对象的变量名应该用复数。 |
| :--- |
| `vector<Point>  points;`<br>`int            values[];` |
| 这样的名字让用户立刻明白变量的类型和可以用于该变量的运算，从而提高可读性。 |

| 23. 【should】表示对象数量的变量应该使用前缀n。 |
| :--- |
| `nPoints`，`NLines` |
| 这种记号是数学中表示对象数量的已有惯例。 |

| 24. 【should】代表对象编号的变量应该使用后缀No。 |
| :--- |
| `tableNo`，`employeeNo` |
| 这种记号是数学中表示对象编号的惯例。 另一种优雅的命名是给变量加上前缀i，例如：`iTable`，`iEmployee`。这样这些变量就成了named iterator。 |

| 25. 【should】循环变量应该用i，j，k等命名。 |
| :--- |
| `for (int i = 0; i < nTables; i++)`<br>`··:`<br>`}`<br>`for (vector<MyClass>::iterator i = list.begin(); i != list.end(); i++) {`<br>`··Element element = *i;`<br>`}` |
| 这种表示方法是数学中的惯例。 变量`j`，`k`等应该只用于循环嵌套。 |

| 26. 【should】布尔变量或返回布尔变量的方法应该加上前缀is。 |
| :--- |
| `isSet`，`isVisible`，`isFinished`，`isFound`，`isOpen` |
| C++开发社区中很常见，而Java中近乎强制使用这种命名。 `is`前缀的使用避免了常见的像`status`或`flag`这种不好的命名。`isStatus`或`isFlag`明显不合适，因此编程者不得不想出一个更有意义的名字。 在类似如下的情形中，用`has`、`can`和`should`代替`is`可能更合适： <br>`bool hasLicense();`<br>`bool canEvalute();`<br>`bool shouldSort();` |

| 27. 【must】成对的操作必须用成对的名称。 |
| :--- |
| `get/set`，`add/remove`，`create/destory`，`start/stop`，`insert/delete`，`increment/decrement`，`old/new`，`begin/end`，`first/last`，`up/down`，`min/max`，`next/previous`，`old/new`，`open/close`，`show/hide`，`suspend/resume`，等等。 |
| 通过对称降低代码复杂度。 |

| 28. 【should】命名时应该尽量避免用缩写。 |
| :--- |
| 使用`computeAverage();`，而不是`compAvg();` |
| 这里主要考虑两种词汇。第一种是字典中的常用词汇。这些一定不能缩写，**错误**示范：<br>`cmd`    代替   `command`<br>`cp`      代替   `copy`<br>`pt `      代替   `point`<br>`comp`  代替   `compute`<br>`init`  代替   `initialize`<br>第二种是特定领域的短语，它们的缩写广为人知。这些短语应该保持缩写，**错误**做法是：<br> `HypertextMarkupLanguage`   代替    `html`<br>`CenterlProcessingUnit`         代替   `cpu`<br>`PriceEaringRatio`                   代替    `pe` |

| 29. 【should】避免为指针特殊命名。 |
| :--- |
| 使用`Line* line;`，而不是`Line* pLine;`或`Line* linePtr;` |
| C/C++环境中很多变量都是指针，几乎不可能遵循这样的命名惯例。而且C++中的对象通常都是<u>oblique类型</u>，程序员应该忽略具体的实现。只有当一个对象的实际类型有特殊意义时，才应该强调他的类型。 |

| 30. 【must】布尔变量必须避免使用否定含义的名称。 |
| :--- |
| 使用`bool isError;`而不是`isNoError`<br>使用`bool isFound;`而不是`isNotFound` |
| 当进行逻辑非运算`!`时，这样的命名会产生双重否定，例如`!isNotFound`的真实含义就不是那么一目了然。 |

| 31. 【can】枚举常量可以用一个通用类型名称作为前缀。 |
| :--- |
| `enum Color {`<br>`··COLOR_RED,`<br>`··COLOR_GREEN,`<br/>`··COLOR_BLUE`<br/>`};` |
| 这一做法提供了以下信息：在哪里能找到其定义、哪些常量属于同一个集合、这些常量代表了什么含义。 另一种代替的做法是始终通过公共类型使用这些枚举常量：`Color::RED`，`Airline::AIR_FRANCE`等。 注意公共类型的名称应该是像`enum Color {...}`的单数形式，虽然`enum Colors {...}`的复数形式在在声明时看起来不错，但使用时会显得有点傻。 |

| 32. 【should】异常类应该以exception作为后缀。 |
| :--- |
| `class AccessException`<br>`{`<br>`··:`<br>`}` |
| 异常类并非程序设计的主要内容，这样命名能够把它们和其他类区分开来。 |

| 33. 【should】有返回值的函数应该以它返回的内容命名，没有返回值的函数应该以其执行的操作命名。 |
| :--- |
| 无 |
| 提升可读性。清楚地说明该函数应该执行的内容和（尤其是）不会执行的内容。这一做法容易避免side effect。 |

