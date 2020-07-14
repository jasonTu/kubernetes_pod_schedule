# 方式1
使用alertmanager.yaml 创建secret加入到alertmanager内
```shell script
kubectl delete secret alertmanager-main -n istio-system

kubectl create secret generic alertmanager-main --from-file=alertmanager.yaml -n istio-system
```

# 方式2 
创建configmap 挂载到 alertmanager内