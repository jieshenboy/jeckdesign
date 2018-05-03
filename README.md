# Python 设计模式

标签（空格分隔）： python 设计模式

---

常见的设计模式及相关代码（16个设计模式）。
#### 1、工厂方法
#### 2、建造者模式
#### 3、原型模式
#### 4、适配器模式
#### 5、修饰器模式
#### 6、外观模式
#### 7、享元模式
#### 8、模型-视图-控制器模式
#### 9、代理模式
#### 10、责任链模式
#### 11、命令模式
#### 12、解释器模式
#### 13、观察者模式
#### 14、状态模式
#### 15、策略模式
#### 16、模板模式

### 1、工厂方法
1.1工厂方法
工厂方法适用于不属于任何类的单一的函数或对象。他是单独的一部分，比如说解析数据库的方法。
#### code: factoryModel.py
#### using a model to deal with the commoned tings.

1.2抽象工厂
抽象工厂适用于单个类的许多工厂方法创建一系列种类的相关对象。
#### code: factoryModel2.py
#### using one pattern to create more tings.

### 2、建造者模式
1、对象复杂，由多个对象组成
2、要求一个对象有不同的表现
#### code: buldModel.py 
#### buldModel2.py

#### building differents pizz can using this pattern.

### 3、原型模式
1、创建一个浅副本时候，依赖引用（全部相同）
2、创建深副本，完全copy，但不会随着改变而改变。
#### code: prototype.py
#### when one file changed, other one can following change.

### 4、适配器模式
让两个不兼容的接口兼容。绑定函数接口。

#### code: adapter.py
#### when the two interface is not adaper the other one, building a adapter to deal with it.

### 5、修饰器模式
添加处理函数的函数，这个函数可以处理函数。

#### code: mymath.py
#### we can using a decorator to add function on others.

### 6、外观模式
可以封装一些复杂的功能，提供简单的接口给外观。

#### code: facade.py
#### builiding a interface in black box.

### 7、享元模式
可以避免重复创建对象，如果对象存在，那么对象引用。
#### code: flyweight.py
#### obj if obj else building a new object.

### 8、模型-视图-控制器模式
MVC(Model-View-Controller)
模型负责访问数据，管理应用状态
视图是模型的外在表现。
控制器是模型与视图之间的连接。
#### code: mvc.py
#### Pay to Caesar what belongs to Caesar, and God what belongs to God.

### 9、代理模式
1、远程代理，代表活跃于远程位置的对象；
2、虚拟代理，将一个对象的初始化延迟到真正需要使用时进行；
3、防护代理，用于对敏感信息的访问控制；
4、添加帮助信息扩展对象的行为。
#### code: proxy.py
#### visit a object be abide by object's rules. 

### 10、责任链模式
若首个节点不能处理，则交给他的父亲去处理。
#### code: chain.py
#### if you can't, make your father to help you.

### 11、命令模式
1、可以在任何时候执行一个命令，而不是在命令创建的时候；
2、执行一个命令的客户端代码并不需要知道命令的细节；
3、可以对命令分组，按照一定顺序执行。
#### code: command.py
#### make a command that can using anywhere.

### 12、解释器模式
可以创建语法格式来解决问题。
#### code: interpreter.py
#### make a new rule tu deal with it.

### 13、观察者模式
敌不动我不动，我们一起在行动。
#### code: observer.py
#### we are working together, if noting and I'm noting.

### 14、状态模式
一个苹果只有红苹果、黄苹果、绿苹果，再也没有其他的了。
#### code: state.py
#### tings is only in some states.

### 15、策略模式
同一个问题有不同的解决方式，我们可以选择性的选择方案。
#### code: strategy.py
#### different working to make different ways to deal.

### 16、模板模式
就是一个模板，当有相近结构的时候，不如创建个模板，让代码避免冗余。
#### code: template.py
#### a template is for somtings.








