

# 污点设置

```shell script
# 键为key，值为value，效果是NoSchedule
kubectl taint nodes node1 key=value:NoSchedule


kubectl get pods -o wide
```

# Tolerations
operator:
- Exists（无需指定value）
- Equal (默认值)
- 空key+ Equal = 所有键值对
- 空effect = 所有effect

# Taints
## 调度方式
- NoSchedule ：开始调度时有用
- PreSchedule ：软调度
- NoExecute ： node一旦设置新的规则，若Pod没有设置Tolerations会被驱逐
## 特殊属性
- dedicated=groupName ： 独占节点
- special=true：