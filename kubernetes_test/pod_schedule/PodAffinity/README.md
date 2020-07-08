

# 创建pod

```shell script
kubectl create -f pod-flag.yaml

kubectl get pods -o wide
```

# PodAffinity topologYKey 域的概念
- kubernetes.io/hostname
- failure-domain.beta.kubernetes.io/zone
- failure-domain.beta.kubernetes.io/regio

# PodAffinity Namespace 命令空间，在node下有多个namespace
podAntiAffinity或podAffinity下的Namespace概念

