# 5 声明

## 5.1 类型

| 43. 【can】作用范围局限于某个文件内的变量类型可以在该文件内部声明。 |
| :--- |
| 无 |
| 强制隐藏信息。 |

| 44. 【must】类中的内容必须以`public`、`protected`、`private`的顺序排列。所有部分必须明确划分。不能遗漏任何有效的内容。 |
| :--- |
| 无 |
| 这样排序符合"most public first"的原则，如果某个程序员只是单纯为了使用这个类，当他看到`protected`或`private`部分时就可以停止阅读。 |

| 45. 【must】类型转换必须是显式的，永远不要依赖隐式类型转换。 |
| :--- |
| ![](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/tree/ea9f299fc53f099f8320b15fe672ea60f3e07766/gitbook/figure/45.png) |
| 这样做清楚地表明：代码的作者知道这里涉及了不同的变量类型，他是有意为之。 |

## 5.2 变量

| 46. 【should】应该在声明变量的位置同时对其初始化。 |
| :--- |
| 无 |
| 这样做保证了变量始终是有效的。有时侯可能会像下面这样初始化声明的变量： ![](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/tree/ea9f299fc53f099f8320b15fe672ea60f3e07766/gitbook/figure/46.png) 这种情况下，与其将其初始化为“假的”值，不如不初始化。 |

| 47. 【must】变量的名称永远不允许有双重含义。 |
| :--- |
| 无 |
| 保证所有concept被唯一地表示。减少由side effect产生的错误。 |

| 48. 【should】应该尽可能避免使用全局变量。 |
| :--- |
| 无 |
| 在C++中完全没有理由使用全局变量。global function和静态变量也一样。 |

| 49. 【should】类成员变量永远不应该被声明为public。 |
| :--- |
| 无 |
| 公有变量破坏了C++隐藏、封装信息的理念。应该用私有变量+成员函数来代替公有变量。一个例外是：如果某个类在本质上是一个数据结构（相当于C语言的结构体），最好令其成员变量都是公有的。 注意C++中的结构体只是为了和C语言兼容，避免使用结构体能够减少所使用的construct，提升代码可读性。请用类代替结构体。 |

| 51. 【should】C++指针和引用的操作符应该紧挨着变量类型而不是变量名。 |
| :--- |
| ![](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/tree/ea9f299fc53f099f8320b15fe672ea60f3e07766/gitbook/figure/51.png) |
| 变量的指针和引用是针对类型的属性，而非变量名的属性。C程序员通常采用前一种写法，但在C++中，后一种写法越来越常见。 |

| 53. 【should】除了布尔变量和指针之外，不应该使用隐含的方式测试其是否为0。 |
| :--- |
| ![](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/tree/ea9f299fc53f099f8320b15fe672ea60f3e07766/gitbook/figure/53.png) |
| C++标准并没有规定整数0和浮点数0.0必须由二进制的0来实现。此外，显式的测试还能清楚地表明测试对象的类型。 |

| 54. 【should】变量的作用域应该越小越好。 |
| :--- |
| 无 |
| 把对变量的操作限制在更小的作用域内，容易控制变量所造成的（希望出现和不希望出现）的影响。 |

## 5.3 循环

| 55. 【must】for循环体中只能包含与循环控制有关的语句。 |
| :--- |
| ![](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/tree/ea9f299fc53f099f8320b15fe672ea60f3e07766/gitbook/figure/55.png) |
| 提高维护性和可读性。将控制循环的语句和循环中的内容明确地区分开来。 |

| 56. 【should】循环变量应该在紧靠循环体的位置初始化。 |
| :--- |
| ![](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/tree/ea9f299fc53f099f8320b15fe672ea60f3e07766/gitbook/figure/56.png) |
| 无 |

| 57. 【can】可以避免使用do-while循环。 |
| :--- |
| 无 |
| do-while循环的可读性不如while循环和for循环，因为循环条件在循环体的下方。为了知道循环的范围，读者必须浏览整个循环体。 另外，没有必要使用do-while循环。任何do-while循环都很容易改写成while循环和for循环。减少construct的数量有助于提升可读性。 |

| 58. 【should】应该避免在循环中使用`continue`和`break` |
| :--- |
| 无 |
| 仅当二者的可读性要比他们的structured counterparts更好时才使用它们。 |

| 60. 【should】对于死循环应该用 `while(true)` 。 |
| :--- |
| ![](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/tree/ea9f299fc53f099f8320b15fe672ea60f3e07766/gitbook/figure/60.png) |
| 测试是否为1既无必要也无意义。`for (;;)`的可读性不太好，也不能明确表示是一个死循环。 |

## 5.4 条件表达式

| 61. 【should】避免使用复杂的条件表达式，推荐使用临时的布尔变量\[1\]。 |
| :--- |
| ![](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/tree/ea9f299fc53f099f8320b15fe672ea60f3e07766/gitbook/figure/61.png) |
| 通过将布尔变量传入表达式，程序变得像文档一样清晰。这样的代码结构容易阅读、调试和维护。 |

| 62. 【should】使用if-else语句时，正常执行的语句应该放在`if`分支中，处理异常的语句放在`else`分支\[1\]。 |
| :--- |
| ![](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/tree/ea9f299fc53f099f8320b15fe672ea60f3e07766/gitbook/figure/62.png) |
| 保证异常处理部分的代码不会模糊代码正常的执行顺序。这一点对于程序的可读性和性能都很重要。 |

| 63. 【should】条件表达式必须独占一行。 |
| :--- |
| ![](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/tree/ea9f299fc53f099f8320b15fe672ea60f3e07766/gitbook/figure/63.png) |
| 这一点为了调试着想。如果把二者写在同一行，将很难判断条件表达式的运行结果是`true`还是`false`。 |

| 64. 【must】条件表达式中不能有可执行语句。 |
| :--- |
| ![](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/tree/ea9f299fc53f099f8320b15fe672ea60f3e07766/gitbook/figure/64.png) |
| 带有可执行语句的条件表达式的可读性很差。尤其是对于C/C++的新手。 |

## 5.5 其他

| 65. 【should】应该避免使用“魔法数字”。对于0和1之外的数字都应该考虑将其声明为常量。 |
| :--- |
| 无 |
| 如果一个数字本身含义不明，将其定义为常量可以提升可读性。另一种可行的方法是定义一个返回该数字的函数。 |

| 66.【should】浮点数应该始终有小数点并且至少有一位小数。 |
| :--- |
| ![](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/tree/ea9f299fc53f099f8320b15fe672ea60f3e07766/gitbook/figure/66.png) |
| 这种写法强调了浮点数与整数的不同。在数学中，二者是完全不同的概念。 |

| 67. 【should】浮点数常量的小数点之前应该总是有数字。 |
| :--- |
| ![](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/tree/ea9f299fc53f099f8320b15fe672ea60f3e07766/gitbook/figure/67.png) |
| C++中的数字和表达式体系借鉴自数学，我们应该始终遵守数学中的惯例。另外，`0.5`的可读性要比`.5`好得多，完全不会和`5`混淆。 |

| 68. 【must】必须始终指定函数返回值的类型。 |
| :--- |
| ![](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/tree/ea9f299fc53f099f8320b15fe672ea60f3e07766/gitbook/figure/68.png) |
| 如果没有显式指定，C++会自动推断返回值的类型为int。程序员永远都不能依赖这种特性， |

| 69. 【should】不应该使用`goto` 。 |
| :--- |
| 无 |
| `goto`违背了代码结构化的初衷。只有在极少数情况下（例如从多层嵌套的循环中跳出），且仅当用于代替`goto`的写法可读性更差时，才应该考虑使用`goto`语句。 |

| 70. 【should】应该用 0 替换`NULL`。 |
| :--- |
| 无 |
| `NULL` 是标准C语言库的内容，但在C++中已经不再使用。 |

