# uwsgi
:smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile: :smile:
## PreStop Test for HighLatency Api
### 目的+结论
目的：4~5s的高延迟Api，需要设置多长preStop时间可以有效遏制5XX的出现

结论：（测试环境有限，listen queue只有128导致不能测试高延迟的接口，后续到QA环境会继续测试）
- 从报告可以看出，随着preStop设置时间的增长，5XX请求的数量逐渐减少，preStop的设置在30~40s时，5XX趋近于0，对于特殊的4-5s延迟的API在RollingUpdate期间有很好的效果。
- 另外从RollingUpdate时间考虑：具有livenessProbe, readinessProbe, lifecycle, sidecar的Pod从初始化到达Running状态时间平均为9s左右，若副本数量为3,整个过程需要27s左右,**preStop生命钩子并不会影响整个RollingUpdate过程**

### 测试工具
```shell script
docker run -p 8080:8080 -p 8079:8079 fortio/fortio server & # For the server
```
### 测试方式
测试4s~5s的接口:/api/sleep/4 和 /api/sleep/5
- UI1界面填入信息
    - c(线程数):10
    - qps(每s期望发送请求数)：100
    - t(持续时间)：60s
    - URL：http://dev-bmonitoring-nabu.qa.cloudedge.trendmicro.com/api/sleep/4
- UI2界面填入信息
    - c(线程数):10
    - qps(每s期望发送请求数)：100
    - t(持续时间)：60s
    - URL：http://dev-bmonitoring-nabu.qa.cloudedge.trendmicro.com/api/sleep/5


### 测试用例
1. [uflask-deployment-v7](../uwsgi/uflask-deployment-v7.yaml): {v7:Configure livenessProbe, readinessProbe, lifecycle, sidecar}
2. [uflask-deployment-v8](../uwsgi/uflask-deployment-v8.yaml): {v8:Configure livenessProbe, readinessProbe, lifecycle, sidecar} 


### 报告
1. preStop=10s,Rolling Updates 28s
    - /api/sleep/4:出现错误23 [preStop=10,sleep4报告](./fortio-report/preStop=10,sleep4.pdf)
    - /api/sleep/5:出现错误37[preStop=10,sleep5报告](./fortio-report/preStop=10,sleep5.pdf)
2. preStop=20s,Rolling Updates 32s
    - /api/sleep/4:出现错误6[preStop=20,sleep4报告](./fortio-report/preStop=20,sleep4.pdf)
    - /api/sleep/5:出现错误5[preStop=20,sleep5报告](./fortio-report/preStop=20,sleep5.pdf)
3. preStop=30s,Rolling Updates 28s
    - /api/sleep/4:出现错误1[preStop=30,sleep4报告](./fortio-report/preStop=30,sleep4.pdf)
    - /api/sleep/5:出现错误4[preStop=30,sleep5报告](./fortio-report/preStop=30,sleep5.pdf)
