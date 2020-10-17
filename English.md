# 1 Introduction

This document lists C++ coding recommendations common in the C++ development community.

The recommendations are based on established standards collected from a number of sources, individual experience, local requirements/needs, as well as suggestions given in [1] - [4].

There are several reasons for introducing a new guideline rather than just referring to the ones above. The main reason is that these guides are far too general in their scope and that more specific rules (especially naming rules) need to be established. Also, the present guide has an annotated form that makes it far easier to use during project code reviews than most other existing guidelines. In addition, programming recommendations generally tend to mix style issues with language technical issues in a somewhat confusing manner. The present document does not contain any C++ technical recommendations at all, but focuses mainly on programming style. For guidelines on C++ programming style refer to the C++ Programming Practice Guidelines.

While a given development environment (IDE) can improve the readability of code by access visibility, color coding, automatic formatting and so on, the programmer should never rely on such features. Source code should always be considered larger than the IDE it is developed within and should be written in a way that maximise its readability independent of any IDE.

## 1.1 Layout of the Recommendations

The recommendations are grouped by topic and each recommendation is numbered to make it easier to refer to during reviews.

Layout of the recommendations is as follows:

| n. Guideline short description                     |
| -------------------------------------------------- |
| Example if applicable                              |
| Motivation, background and additional information. |

The motivation section is important. Coding standards and guidelines tend to start "religious wars", and it is important to state the background for the recommendation.

In the guideline sections the terms *must*, *should* and *can* have special meaning. A *must* requirement must be followed, a *should* is a strong recommendation, and a *can* is a general guideline.

## 1.2 Recommendations Importance

In the guideline sections the terms *must*, *should* and *can* have special meaning. A *must* requirement must be followed, a *should* is a strong recommendation, and a *can* is a general guideline.

# 2 General Recommendations

| 1. Any violation to the guide is allowed if it enhances readability. |
| ------------------------------------------------------------ |
|                                                              |
| The main goal of the recommendation is to improve readability and thereby the understanding and the maintainability and general quality of the code. It is impossible to cover all the specific cases in a general guide and the programmer should be flexible. |

| 2. The rules can be violated if there are strong personal objections against them. |
| ------------------------------------------------------------ |
|                                                              |
| The attempt is to make a guideline, not to force a particular coding style onto individuals. Experienced programmers normally want to adopt a style like this anyway, but having one, and at least requiring everyone to get familiar with it, usually makes people start *thinking* about programming style and evaluate their own habits in this area. |

# 3 Naming Conventions

## 3.1 General

## 3.2 Specific

# 4 Files

## 4.1 Source Files

## 4.2 Include Files and Include Statements

# 5 Statements

## 5.1 Types

## 5.2 Variables

## 5.3 Loops

## 5.4 Conditionals

## 5.5 Miscellaneous

# 6 Layout and Comments

## 6.1 Layout

## 6.2 White space

## 6.3 Comments

# 7 References