# 译者附录

部分单词没有找到合适的译法，在上面的译文中保留了英文形式，根据我搜集的资料尝试解释如下：

- **side effect**（11, 32, 42, 47, 54）：直译是“副作用”，但听起来并不直白。根据[维基百科](https://en.wanweibaike.com/wiki-Side%20effect%20(programming))，我的理解是：side effect是指某个操作、函数或表达式在返回目标值之外，还修改了作用域之外的内容，例如：
  - 修改了非局部变量、静态局部变量、通过引用传递的可变参数
  - 执行I/O操作
  - 调用其他会产生side effect的函数

- **concept**（20, 47, 49）：根据[维基百科](https://en.wanweibaike.com/wiki-Concept%20(generic%20programming))，我的理解是：concept是指某个类可以执行的操作。
- **constructs**（49, 57）：第49条谈到struct结构体和第57条谈到do-while循环时，都提到了construct这个单词，第49条是说class完全可以代替struct，第57条是说完全可以用while循环和for循环代替do-while，这两条建议都在强调：减少使用construct的数量有助于提高代码可读性。根据[维基百科](http://en.volupedia.org/wiki/Language_construct)对于**language construct**的解释，我认为可以把本文档中的construct理解为**代码的布局或结构**，当用C++来实现某种功能时，代码结构越单一、代码结构形式的种类越少，当然就越容易让别人看懂。