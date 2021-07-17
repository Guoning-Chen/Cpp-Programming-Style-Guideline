# 译者前言

## 一份适合C++初学者的C++编程风格指南

## 如何使用

**在线阅读**

* GitBook链接：[https://chengn.gitbook.io/programing-style-for-beginner/](https://chengn.gitbook.io/programing-style-for-beginner/)
* 图片加载比较慢，翻墙会好很多。

**离线阅读（推荐）**

* Chinese.pdf：PDF格式的完整译文。
* Chines.md：Markdown格式的完整译文，推荐使用[Typora](https://www.typora.io/)打开。

## 内容简介

众所周知，对于一名合格的程序员而言，保持良好的代码风格非常重要。好的代码风格能够让别人（也不只是别人，还可能是写完代码N天之后的自己）快速地掌握一段代码的逻辑结构，从而高效地进行维护，这对于团队协作开发一个大型项目是非常有利的。另外，良好的代码风格甚至还能够从源头上避免自己无意间造成的一些bug。

关于代码风格的书或在线文档有很多，已经出版的书籍有《重构-改善既有代码的设计》、《代码整洁之道》等等；很多大公司也有完善的编程规范，例如：[Google 开源项目风格指南 \(中文版\)](https://zh-google-styleguide.readthedocs.io/en/latest/)。虽然这些资料的内容都很详细、很权威，但缺点就是——**太长**（Google编程规范中文版就长达5万字），不太适合**C++初学者**。

我接触到这份指南是在刚开始学习C++的时候，由MOOC公开课——[北京邮电大学《C++程序设计（面向对象进阶）》](https://www.icourse163.org/course/BUPT-1003564002?outVendor=zw_mooc_pclszykctj_)的老师推荐的。**之所以说这份指南适合初学者，主要有以下原因：**

1. **字数少**：翻译之后不到8000字。
2. **格式友好，方便阅读**：这里面其实是一条一条的建议，只有90条左右；每条建议还给出了示例和**之所以这样做的原因**（这一点对于记忆很有用！）；另外格式很清晰，方便多次回看。
3. **内容很基础，初学者也能用得到**：学习编程规范的最好方法就是**边学边用**，但是像Google编程规范中的很多内容，初学者的日常编程其实是用不到的，而这份规范中的大部分内容都很基础，也很常用；又因为它很短，用到的时候可以很快翻到相应的地方，不至于太影响编程体验。
4. **有利于培养代码规范的意识**：正如作者前两条建议所说——**“只要能够提升可读性，允许采用不同于该指南的做法。” “如果你个人很抵触该指南的某项建议，可以不采纳。”**作者一直在强调，重要的是这种**下意识为阅读代码的人着想的意识**，而不是某种固定、死板的做法，这一点让我受益很多。

总之，**这篇指南适合以下读者：**

1. **从一开始就想养成良好编程习惯的C++初学者**

   对你来说，这份短小精悍的指南将是一个非常好的选择。

2. **想要从现在开始纠正之前的编程习惯的C++使用者**

   相信会有很多人像我一样，因为畏惧Google编程规范之类文档的过于庞杂而不知道从何处开始，这份指南同样适合你们。万事开头难，你完全可以把阅读这份指南当做一个相对轻松的开头，等到培养一定的习惯之后再考虑学习那些更加复杂、也更加完善的编程指南。

## 注意事项

1. 由于水平有限，文中部分名词和句子翻译的似乎不太通顺，但未找到更好的译法，已在文中用下划线标出；
2. 部分单词未找到合适的译法，在文中**保留了英文**，同样用下划线标出；
3. 部分标记了下划线的英文单词在原文中出现多次，我推测可能是术语，在**译者附录**中给出了我自己的理解；
4. 如果你发现翻译内容有误或对下划线部分有新的见解，欢迎在[issue](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/issues)中指出或通过[邮箱](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline/tree/35b4125ba008b206b9d35ef4ef4f7fb66490f66d/cgn1874@163.com)联系我，同样欢迎任何其他的意见。

## 相关信息

英文名：C++ Programming Style Guidelines

中文名：C++编程风格指南

原作者：_Geotechnical Software Services_

版本：4.9

时间：2011年1月

英文原文：[http://geosoft.no/development/cppstyle.html](http://geosoft.no/development/cppstyle.html)

译者：[Guoning-Chen](https://github.com/Guoning-Chen)

译者邮箱：cgn1874@163.com

翻译版本：v1.0

Github仓库：[https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline](https://github.com/Guoning-Chen/Cpp-Programming-Style-Guideline)

