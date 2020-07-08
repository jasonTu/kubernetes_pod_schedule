# NodeAffinity
- RequiredDuringSchedulingIgnoredDuringExecution：硬限制
- PrefreedDuringSchedulingIgnoredDuringExecution：软限制，设置权重

# 创建pod

```shell script
kubectl create -f NodeAffinity-test.yaml

kubectl get pods -o wide
```
