# 字符串

String 是redis最基本的类型，value 不仅可以是 String,也可以是数字。

使用 Strings 类型,可以完全实现目前
Memcached 的功能,并且效率更高。还可以享受 Redis 的定时持久化(可以选择 RDB 模式或者 AOF 模式). 

string类型是二进制安全的。意思是redis的string可以包含任何数据,比如jpg图片或者序列化的对象

string类型是Redis最基本的数据类型，一个键最大能存储512MB。



### 命令示例：



`set` ­­ 设置key对应的值为string类型的value。

```bash
> set name itcast
```

`setnx` ­­ 将key设置值为value，如果key不存在，这种情况下等同SET命令。 当key存在时，什么也不做。SETNX是”SET if Not eXists”的简写。

```bash
> get name
"itcast"
> setnx name itcast_new
(integer)0
>get name
"itcast"
```

`setex` ­­ 设置key对应字符串value，并且设置key在给定的`seconds`时间之后超时过期。

```bash
> setex color 10 red 
> get color
"red"
10秒后...
> get color (nil)
```

`setrange` ­­ 覆盖key对应的string的一部分，从指定的offset处开始，覆盖value的长度。
```bash
127.0.0.1:6379> set email wangbaoqiang@itcast.cn
OK
127.0.0.1:6379> setrange email 13 gmail.com 
(integer) 22
127.0.0.1:6379> get email
"wangbaoqiang@gmail.com"
127.0.0.1:6379>STRLEN email
(integer) 22
```
  其中的4是指从下标为13(包含13)的字符开始替换

`mset` ­­ 一次设置多个key的值,成功返回ok表示所有的值都设置了,失败返回0表示没有任何值被设置。

```bash
> mset key1 python key2 c++
  OK
```

`mget` ­­ 一次获取多个key的值,如果对应key不存在,则对应返回nil。

```bash
> mget key1 key2 key3
  1) "python"   
  2) "c++"   
  3) (nil)
```
`msetnx` ­­ 对应给定的keys到他们相应的values上。只要有一个key已经存在，MSETNX一个操作都不会执行。

```bash
> MSETNX key11 "Hello" key22 "there"
(integer) 1
> MSETNX key22 "there" key33 "world"
(integer) 0
```
认证了：MSETNX是原子的，所以所有给定的keys是一次性set的

`getset` ­­ 设置key的值,并返回key的**旧值**
```bash
> get name
"itcast"
> getset name itcast_new
"itcast"
> get name
"itcast_new"
```

`GETRANGE key start end` ­­ 获取指定key的value值的子字符串。是由start和end位移决定的

```bash
> getrange name 0 4
  "itcas"
```


`incr` ­­ 对key的值加1操作
```bash
> set age 20 
> incr age 
(integer) 21
```

`incrby` ­­ 同incr类似,加指定值 ,key不存在时候会设置key,并认为原来的value是 0

```bash
> incrby age 5
  (integer) 26
> incrby age1111 5
(integer) 5
> get age1111
"5"

```

`decr` ­­ 对key的值做的是减减操作,decr一个不存在key,则设置key为­1


`decrby` ­­ 同decr,减指定值


`append` ­­ 给指定key的字符串值追加value,返回新字符串值的长度。例如我们向name的值追加一个"redis"字符串:

```bash
127.0.0.1:6379> get name
"itcast_new"
127.0.0.1:6379> append name "value"
(integer) 15
127.0.0.1:6379> get name
"itcast_newvalue"
127.0.0.1:6379> 
```
