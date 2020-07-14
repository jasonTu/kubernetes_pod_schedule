# Ops
基础设施由Operator维护
- EKS
- Prometheus
    - alertManager
    - grafana
- Istio


# Dev
由Service开发者维护
- Application
    - Deployment
    - Service
    - ServiceMonitor(based on Labels to select Service)
- Maintain
    - metrics
    - alert(based on metrics)
- Expand
    - HPA(based on metrics)