# Redis 订阅发布模式

Redis 发布订阅(pub/sub)是一种消息通信模式：发送者(pub)发送消息，订阅者(sub)接收消息。
Redis 客户端可以订阅任意数量的频道。
下图展示了频道 channel1 ， 以及订阅这个频道的三个客户端 —— client2、client5 和 client1 之间的关系：

![](/photos/04_pub.png)

当有新消息通过 PUBLISH 命令发送给频道 channel1 时， 这个消息就会被发送给订阅它的三个客户端：

![](/photos/04_pub2.png)

### 应用场景
在Redis中，你可以设定对某一个key值进行消息发布及消息订阅，当一个key值上进行了消息发布后，所有订阅它的客户端都会收到相应的消息。这一功能最明显的用法就是用作实时消息系统，比如普通的即时聊天，群聊等功能。

1. 今日头条订阅号、微信订阅公众号、新浪微博关注、邮件订阅系统

2. 即时通信系统（QQ、微信）

3. 群聊部落系统（微信群）

### 案例

微信班级群`class:20170101`，发布订阅模型

**学生A B C:**

订阅一个`主题`名叫： `class:20170101`

```bash
127.0.0.1:6379> SUBSCRIBE class:20170101
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "redisChat"
3) (integer) 1
```

**学生A:**

针对 `class:20170101` 主题发送 消息，那么所有订阅该主题的用户都能够收到该数据。
```cpp
127.0.0.1:6379> PUBLISH class:20170101 "i love peace!"
(integer) 1
```

**学生B:**

针对 `class:20170101` 主题发送 消息，那么所有订阅该主题的用户都能够收到该数据。

```cpp
127.0.0.1:6379> PUBLISH class:20170101 "go to hell"
(integer) 1
```

最后学生C会收到 A 和 B 发送过来的消息。

```cpp
python@ubuntu:~$ redis-cli 
127.0.0.1:6379> SUBSCRIBE class:20170101
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "class:20170101"
3) (integer) 1
1) "message"
2) "class:20170101"
3) "i love peace!"
1) "message"
2) "class:20170101"
3) "i love peace!"
1) "message"
2) "class:20170101"
3) "go to hell"

```


