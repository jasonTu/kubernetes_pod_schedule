
# Pod优点调度
提高集群的资源利用率：采用优先级方案，不同类型负载对应不同优先级。且允许负载所需资源总量 > 集群提供量，超出，系统可释放不重要资源。

## 抢占式调度

维度定义优先级
- Priority，优先级
- Qos，服务质量等级
- 系统定义的其他质量指标

两种行为
- Eviction ：驱逐
- Preemption ： 抢占

问题：
优先级来解决资源紧张的局面，是不稳定的。应该采用扩容的方式