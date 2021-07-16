

# 3 命名规范

## 3.1 通用命名规范

| 3. 【must】类型的名称中所有单词的首字母必须大写。 |
| :------------------------------------------------ |
| ![avatar][3-png]                                  |
| C++开发社区中的通用做法。                         |

| 4. 【must】变量名中的第一个单词必须小写，其余大写。          |
| :----------------------------------------------------------- |
| <img src="https://raw.githubusercontent.com/Guoning-Chen/Cpp-Programming-Style-Guideline/main/source/figure/4.png" style="zoom:50%;" /> |
| C++开发社区中的通用做法。使得变量区别于各种类的名称，有效解决如`Line line`这种声明中潜在的命名冲突。 |

| 5. 【must】常量（包括枚举量）的名称中所有字母都必须大写，并用下划线分开。 |
| :----------------------------------------------------------- |
| <img src="https://raw.githubusercontent.com/Guoning-Chen/Cpp-Programming-Style-Guideline/main/source/figure/5-1.png" style="zoom:60%;" /> |
| C++开发社区中的通用做法。通常应该尽可能避免使用常量。在大部分情况下，用函数代替是更好的选择：<br><img src="figure\5-2.png" alt="image-20210703143643703" style="zoom:80%;" /> <br>这样既容易阅读，又能保证和<u>类的成员变量</u>统一接口。 |

| 6. 【must】方法或函数的名称必须包含动词且首字母小写、其余大写。 |
| :----------------------------------------------------------- |
| <img src="figure\6.png" alt="" style="zoom:80%;" />          |
| C++开发社区中的通用做法。虽然和变量的命名方式相同，但函数本身的特征已经足以将它和变量区别开来。 |

| 7. 【should】命名空间的名称中的字母应该全部小写。 |
| :------------------------------------------------ |
| <img src="figure\7.png" style="zoom:80%;" />      |
| C++开发社区中的通用做法。                         |

| 8. 【should】模板类的名称应该是一个大写英文字母。            |
| :----------------------------------------------------------- |
| <img src="figure\8.png" style="zoom:80%;" />                 |
| C++开发社区中的通用做法。使得模板类的名称比其它名称都要显眼。 |

| 9.  【must】当用于命名的时候，缩写词汇只有首字母可以大写 [4] |
| :----------------------------------------------------------- |
| <img src="figure\9.png" style="zoom:80%;" />                 |
| 如果将缩写词全部大写，将会破坏上述命名规范。相应类型的变量就只能命名为`dVD`，`hTML`等等，可读性显然不好。另一个问题在例子中已经说明：当名称中包含多个单词的时候，（如果将缩写词全部大写）可读性会严重降低，不再容易分辨出缩写词之后的单词。 |

| 10. 【should】应该一直通过 :: 操作符来使用全局变量。         |
| :----------------------------------------------------------- |
| <img src="https://raw.githubusercontent.com/Guoning-Chen/Cpp-Programming-Style-Guideline/main/docs/figure/10.png" style="zoom:80%;" /> |
| 通常应该减少使用全局变量。考虑用单例对象来代替。             |

[^单例对象]: 使用设计模式中的单例模式，可以创建唯一的对象。

| 11. 【should】类的私有成员应该加下划线。                     |
| :----------------------------------------------------------- |
| <img src="figure\11-1.png" alt="" style="zoom:80%;" />       |
| 除了名称和类型之外，变量的**作用域**是最重要的特征。利用下划线来表明其作用域容易将类的成员变量和本地变量区别开来。这之所以很关键是因为类的成员变量比成员函数更重要，要特殊对待。<br>使用下划线带来的另一个好处是可以很好地解决如何给<u>setter</u>和构造函数的参数命名的问题：<br><img src="figure\11-2.png" style="zoom:80%;" /><br>将下划线作为前缀还是后缀是个问题。这两种做法都很常见，但更推荐后者，因为似乎最完整地保留了名称的可读性。<br>值得注意的是——区分变量的作用域很久以来都是有争议的话题。不过现在这种做法似乎正逐渐被人们所接受，在专业开发社区中正逐渐成为一种惯例。 |

[^setter]: 目测是指给类中的成员变量赋值的一类成员函数</u>

| 12. 【should】<u>通用变量</u>的名称应该和它的类型相同。      |
| :----------------------------------------------------------- |
| <img src="figure\12-1.png" style="zoom:40%;" />              |
| 通过减少术语和名称的数量来降低代码的复杂度。同时根据变量名就很容易推断出它所属的类。<br>如果因为一些原因，该惯例**并不适合**你使用的场景，这很可能说明你选择了一个不合适的类名。<br>非通用变量通常扮演某种**角色**，通常可以结合他们各自的角色和所属的类给他们命名：<br><img src="figure\12-2.png" style="zoom:80%;" /> |

[^通用变量]: 我理解为出现在多个函数的参数列表中的形参

| 13. 【should】所有名称都应该用英文。          |
| --------------------------------------------- |
| <img src="figure\13.png" style="zoom:80%;" /> |
| 英语更加适合国际化开发。                      |

| 14. 【should】作用域比较大的变量应该用长名字，作用域小的用段名字。 |
| :----------------------------------------------------------- |
| 无                                                           |
| 用于临时存储或索引的变量应该尽量短。程序员看到这样的变量应该可以假定其作用域不超过几行代码。用于整数的通用变量可以是`i`, `j`, `k`, `m`, `n`，对于字符常用`c`和`d`。 |

| 15. 【should】类方法中应该避免出现对象的名称。               |
| :----------------------------------------------------------- |
| <img src="figure\15.png" style="zoom:80%;" />                |
| 如样例所示，后者虽然在类的定义中看起来很自然，但使用时显得多余。 |

## 3.2 特殊的命名规范

| 17. 【must】直接访问类的属性必须使用术语get或set。           |
| ------------------------------------------------------------ |
| <img src="figure\17.png" alt="" style="zoom:80%;" />         |
| C++开发社区的常用做法。在Java中这种命名惯例已经多少成为了一种标准。 |

| 18. 【can】当计算某样东西时可以使用术语compute。             |
| ------------------------------------------------------------ |
| <img src="figure\18.png" style="zoom:80%;" />                |
| 明确提醒读者这很可能是一个消耗时间的运算，如果重复运行，可能需要考虑缓存计算结果。一致地使用该术语可以提高程序可读性。 |

| 19. 【can】当查找某样东西时可以在类方法中使用术语find。      |
| ------------------------------------------------------------ |
| <img src="figure\19.png" style="zoom:80%;" />                |
| 明确提醒读者这是一个运算量较少的查找操作。一致使用该术语可以提高程序可读性。 |

| 20. 【can】当新建对象或concept时可以使用术语initialize。     |
| ------------------------------------------------------------ |
| <img src="figure\20.png" style="zoom:80%;" />                |
| 美式的`initialize`好于英式的`initialise`。应该避免用`init`。 |

| 21. 【should】代表GUI控件的变量应该用组件类型作为后缀。  |
| -------------------------------------------------------- |
| <img src="figure\21.png" style="zoom:80%;" />            |
| 让用户立刻明白变量的类型和对象资源，从而提高代码可读性。 |

| 22. 【should】代表一组对象的变量名应该用复数。               |
| ------------------------------------------------------------ |
| <img src="figure\22.png" style="zoom:80%;" />                |
| 这样的名字让用户立刻明白变量的类型和可以用于该变量的运算，从而提高可读性。 |

| 23. 【should】表示对象数量的变量应该使用前缀n。 |
| ----------------------------------------------- |
| <img src="figure\23.png" style="zoom:80%;" />   |
| 这种记号是数学中表示对象数量的已有惯例。        |

| 24. 【should】代表对象编号的变量应该使用后缀No。             |
| ------------------------------------------------------------ |
| <img src="figure\24.png" style="zoom:80%;" />                |
| 这种记号是数学中表示对象编号的惯例。<br>另一种优雅的命名是给变量加上前缀i，例如：`iTable`，`iEmployee`。这样这些变量就成了<u>named iterator</u>。 |

| 25. 【should】循环变量应该用i，j，k等命名。                  |
| ------------------------------------------------------------ |
| <img src="figure\25.png" alt="" style="zoom:80%;" />         |
| 这种表示方法是数学中的惯例。<br>变量`j`，`k`等应该只用于循环嵌套。 |

| 26. 【should】布尔变量或返回布尔变量的方法应该加上前缀is。   |
| ------------------------------------------------------------ |
| <img src="figure\26-1.png" style="zoom:80%;" />              |
| C++开发社区中很常见，而Java中近乎强制使用这种命名。<br>is前缀的使用避免了常见的像`status`或`flag`这种不好的命名。`isStatus`或`isFlag`明显不合适，因此编程者不得不想出一个更有意义的名字。<br>在类似如下的情形中，用`has`、`can`和`should`代替`is`可能更合适：<br><img src="figure\26-2.png" style="zoom:80%;" /> |

| 27. 【must】成对的操作必须用成对的名称。      |
| --------------------------------------------- |
| <img src="figure\27.png" style="zoom:80%;" /> |
| 通过对称降低代码复杂度。                      |

| 28. 【should】命名时应该尽量避免用缩写。                     |
| ------------------------------------------------------------ |
| <img src="figure\28.png" style="zoom:80%;" />                |
| 这里主要考虑两种词汇。第一种是字典中的常用词汇。这些一定不能缩写，**错误**示范：<br><img src="C:\Users\chengn\iCloudDrive\iCloud~com~coderforart~iOS~MWeb\我的Markdown笔记\Computer\《C++编程风格指南》\figure\28-2.png" style="zoom:80%;" /><br>第二种是特定领域的短语，它们的缩写广为人知。这些短语应该保持缩写，**错误**做法是：<br><img src="figure\28-3.png" style="zoom:80%;" /> |

| 29. 【should】避免为指针特殊命名。                           |
| ------------------------------------------------------------ |
| <img src="figure\29.png" style="zoom:80%;" />                |
| C/C++环境中很多变量都是指针，几乎不可能遵循这样的命名惯例。而且C++中的对象通常都是<u>oblique类型</u>，程序员应该忽略具体的实现。只有当一个对象的实际类型有特殊意义时，才应该强调他的类型。 |

| 30. 【must】布尔变量必须避免使用否定含义的名称。             |
| :----------------------------------------------------------- |
| <img src="figure\30.png" style="zoom:80%;" />                |
| 当进行逻辑非运算`!`时，这样的命名会产生双重否定，例如`!isNotFound`的真实含义就不是那么一目了然。 |

| 31. 【can】枚举常量可以用一个通用类型名称作为前缀。          |
| ------------------------------------------------------------ |
| <img src="figure\31.png" style="zoom:80%;" />                |
| 这一做法提供了以下信息：在哪里能找到其定义、哪些常量属于同一个集合、这些常量代表了什么含义。<br>另一种代替的做法是始终通过公共类型使用这些枚举常量：`Color::RED`，`Airline::AIR_FRANCE`等。<br>注意公共类型的名称应该是像`enum Color {...}`的单数形式，虽然`enum Colors {...}`的复数形式在在声明时看起来不错，但使用时会显得有点傻。 |

| 32. 【should】异常类应该以exception作为后缀。                |
| ------------------------------------------------------------ |
| <img src="figure\32.png" style="zoom:80%;" />                |
| 异常类并非程序设计的主要内容，这样命名能够把它们和其他类区分开来。 |

| 33. 【should】有返回值的函数应该以它返回的内容命名，没有返回值的函数应该以其执行的操作命名。 |
| ------------------------------------------------------------ |
| 无                                                           |
| 提升可读性。清楚地说明该函数应该执行的内容和（尤其是）不会执行的内容。这一做法容易避免<u>side effect</u>。 |

[3-png]: data:image/png;base64,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