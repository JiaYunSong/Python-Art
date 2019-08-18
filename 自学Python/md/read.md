# C# 集成开发环境：Visual Studio

## 结构：
```
using System;
```
> 包含 System 命名空间
```
class hello{	/*注释*/
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
> **命名空间声明**
```
	public class Test{
```
> > 可以多个class
> > 构造函数、析构函数、静态成员...

> **变量...**
```
decimal a=10;
```
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

> **字符串**
```
		"hhh\"hhh\nhhh"	==
		@"hhh"hhh\nhhh"	==
		@"hhh"hhh
			hhh"
		"hhh" + "hhh"
```
> > 字符串一堆方法：拆分，复制...

> **可空类型，即可以赋值为null**
```
		int? a,b=null;	//a==null
		int a;		//a==0
```

> **合并运算符**
```
		int b=a ?? 5;	//a为null则b=5,否则b=a
```

> **多维数组**
```
		int [,] a = new int [3,4] {
 			{0, 1, 2, 3} ,	/*  初始化索引号为 0 的行 */
 			{4, 5, 6, 7} ,	/*  初始化索引号为 1 的行 */
 			{8, 9, 10, 11}	/*  初始化索引号为 2 的行 */
			};
```

> **交错数组**
```
		int[][] scores = new int[5][];
		for (int i = 0; i < scores.Length; i++) 
			scores[i] = new int[4];
```

> **Array 类**
```
		scores.Rank;	//获取数组的秩（维度）
		scores.Length;
		Array.Copy(Array, Array, Int32);
		/*从数组的第一个元素开始复制某个范围的元素
			到另一个数组的第一个元素位置*/
```

> **其他运算符**
```
		&a	//地址
		*a	//指针
		obj is Car	// 检查 obj 是否是 Car 类的一个对象。
		obj as int	//强制转换，即使转换失败也不会抛出异常。
```

> **常量**
```
		const
```
> > 其他常量例如8进制数
```
		0213
```
> **装箱与拆箱**
```
		object obj;
		obj = 100; 	//这是装箱
		int a=obj as int;	//这是拆箱
```

> **循环**
```
		foreach(变量 in 数组){}
```

> **方法...**
```
		public int plus(int a){return a+1;}
```
> > 重载
```
		public int plus(char a){return a+2;}
```
> > 运算符重载
```
		public static Box operator+ (Box b, Box c){...}
```
> > 可重载
> > * \+, \-, !, \~, \+\+, \-\-		( op-type operand )
> > * \+, \-, \*, \/, %，\=\=, \!\=, \<, \>, \<\=, \>\=	( op-type operand, op-type2 operand2 )

> > 不可直接重载
> > * &&, ||

> > 不可重载
> > * +=, -=, *=, /=, %=，=, ., ?:, ->, new, is, sizeof, typeof

		(int a)	//按值传递
		(ref int a)	//引用
		(out int a)	//按输出传递，即变量最后一个值赋回去

		//传递数组给函数
		(int[] a)

		//参数数组
		int plus(params int[] arr)
		//传递时--->
		plus(512, 720, 250, 567, 889)

		public：所有对象都可以访问；
		internal：同一个程序集的对象可以访问；
		protected internal：访问限于当前程序集或派生自包含类的类型。
		
	}

}

namespace second{			//命名空间声明
	public class Test{
	}

	namespace second{		//嵌套命名空间
	}

}

class TestClass{			//命名空间运用
	void hhh(){
		first.Test;
		second.Test;
	}
}

using second;		//using指令：引入命名空间
using static System.Math;	//指定无需指定类型名称即可访问其静态成员的类型
using Project = PC.MyCompany;		//起别名
using (Font font3 = new Font("Arial", 10.0f),	//将实例与代码绑定
            font4 = new Font("Arial", 10.0f))

//预处理器指令
#define PIQ	//定义一系列成为符号的字符
#if(PIW)	{不会执行}	//测试符号是否为真
#elif(PIQ)	{会执行}
#else	{}
#endif		//指定一个条件指令的结束
#undef PIQ	//取消定义符号

#line number filename	//修改编译器的行数以及（可选地）输出错误和警告的文件名
#line default		//恢复默认行号
#error 你错了！		//从代码的指定位置生成一个错误
#warning	你就错了！	//从代码的指定位置生成一级警告
#pragma warning disable 169    //取消编号 169 的警告（即字段未使用的警告）
#pragma warning restore 169   // 恢复编号 169 的警告

#region		//在使用 Visual Studio Code Editor 的大纲特性时，指定一个可展开或折叠的代码块
#endregion	//标识着 #region 块的结束

//大神用法
#define  CONNECT(a,b)   a##b	//##粘连两个标识符，只有宏定义中使用(#define)
int  CONNECT(a,1);			//int a1

	//传统方式：
typedef struct _tag_Student Student;
struct _tag_Student{
	char* name;
	int id;
};
	//用宏定义方式
#define STRUCT(type)    typedef struct _tag_##type type;\
		       struct _tag_##type
STRUCT(Student){
	char* name;
	int id;
}; 

//异常处理
try	{throw a;}		//a为throwable
catch(a)	{}
finally	{}


class _throw{
void _throw(){
//在 catch 块中使用 throw 语句来抛出当前的对象
try{
	MethodThatThrowsException();
}
catch (Exception ex){
	//和根本不存在这个catch块的时候一样
	throw;
}
catch (Exception ex){
	//stack trace认为你catch到的异常已经被处理了
	//只不过处理过程中又抛出新的异常
	//这时候stack trace就把throw ex;当作错误根源了
	throw ex;
}
catch (Exception ex){	
	//stack trace会自动认为内部异常是导致当前异常的原因
	//也就会把内部异常的stack trace也递归显示出来
	throw new Exception("oops!", ex);
}
}}

//System.ApplicationException 类：
//支持由应用程序生成的异常。所以程序员定义的异常都应派生自该类。

//输入与输出
using System;
class _IO{
void _IO(){
	console.write("C#很迷");
	console.writeline("显示的信息");
	Console.WriteLine("第一个学生的姓名{0},成绩{1}",name1,score1);
		//“格式字符串”和变量列表，当有多个变量需要输出时可以使用该方法
		//{0}、{1}叫做占位符，代表后面依次排列的变量表
	console.readkey();	//等待用户按下任意键，一次读入一个字符
	console.readline();	//string,当用户按下enter键的时候一次读取一行
	convert.toint32/todouble("32"); //convert用于不同类型数据之间的转化
	int.Parse("32");	//这个也能转化
}}

//正则表达式：匹配专用，可以用于输入readline()的整理
//Regex 类用于表示一个正则表达式
//自己去看吧~[https://www.runoob.com/csharp/csharp-regular-expressions.html]

//文件的输入与输出
//[https://www.runoob.com/csharp/csharp-file-io.html]

//特性，类似于Java的/**   */，生成说明注释
[attribute(positional_parameters, name_parameter = value, ...)]
class || method || 变量 ......
//[https://www.runoob.com/csharp/csharp-attribute.html]

/*反射：
允许在运行时查看特性（attribute）信息。
允许审查集合中的各种类型，以及实例化这些类型。
允许延迟绑定的方法和属性（property）。
允许在运行时创建新类型，然后使用这些类型执行一些任务。*/

//不安全代码
/*由于C#中声明的变量在内存中的存储受垃圾回收器管理；因此一个变量（例如一个大数组）有可能在运行过程中被移动到内存中的其他位置。如果一个变量的内存地址会变化，那么指针也就没有意义了。*/
//解决方法就是使用fixed关键字来固定变量位置不移动。
int[]  list = {10, 100, 200};
fixed(int *ptr = list)
//或者在方法上标明unsafe
public unsafe static void Main(){
	int var = 20;
	int* p = &var;
}
//或程序里标明unsafe
unsafe{	int var = 20;
	int* p = &var;
}
//注意，编译时需要命令行编译或者修改编译器设置
