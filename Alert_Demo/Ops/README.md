# 方式1
使用alertmanager.yaml 创建secret加入到alertmanager内
```shell script
# 加入规则
kubectl delete secret alertmanager-main -n istio-system

kubectl create secret generic alertmanager-main --from-file=alertmanager.yaml -n istio-system

# 检测是否有效
# 查看容器发送的错误
kubectl logs -f alertmanager-main-0 alertmanager -n istio-system
kubectl 
```

# 方式2 
创建configmap 挂载到 alertmanager内