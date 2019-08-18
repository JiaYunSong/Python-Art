# C# 集成开发环境：Visual Studio

## 结构：
```
using System;
```
> 包含 System 命名空间
```
class hello{	\/\*注释\*\/
	static void Main(string\[\] args){
```

>  一个文件一个main函数
```
	}
}
```

## 结构体
```
struct Books{变量...}
```
> 结构不支持继承。
> 结构不能声明默认的构造函数

## 枚举
```
enum Day { Sun, Mon, tue, Wed, thu, Fri, Sat };
```
> Day.Sun==0
> Day.Mon==1

## 接口
```
public interface PaintCost {int getCost(int area);}
```

## 派生类
```
class Rectangle : hello, PaintCost{}
```

## 全析
```
namespace first{
```
> 命名空间声明
```
	public class Test{
```
> > 可以多个class
> > 构造函数、析构函数、静态成员...
> 变量...
> `decimal a=10;`
> > 128 位精确的十进制值，28-29 有效位数
```
		sbyte b=2;
```
> > 8 位有符号整数类型
```
		uint c;
```
> > 32 位无符号整数类型
```
		ulong d;
```
> > 64 位无符号整数类型
```
		ushort e;
```
> > 16 位无符号整数类型
```
		dynamic f=a,g=b;
```
> > 存储任何类型的值在动态数据类型变量中
