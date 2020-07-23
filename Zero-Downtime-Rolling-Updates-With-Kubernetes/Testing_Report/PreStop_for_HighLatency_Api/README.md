# uwsgi
## Zero-Dowentime-Test
### 目的+结论
目的：不同的高延迟Api，需要设置多长preStop时间
结论：（测试环境有限，listen queue只有128导致不能测试高延迟的接口）
- 从报告可以看出，随着preStop设置时间的增长，5XX请求的数量逐渐减少，preStop的设置在30~40s时，5XX趋近于0，对于特殊的4-5s延迟的API在RollingUpdate期间也有很好的效果。
- 另外从RollingUpdate时间考虑：具有livenessProbe, readinessProbe, lifecycle, sidecar的Pod从初始化到达Running状态时间平均为9s左右，若副本数量为3,整个过程需要27s左右,preStop生命钩子并不会影响整个RollingUpdate过程

具有livenessProbe, readinessProbe, lifecycle, sidecar的Pod启动时间为10s.
### 测试工具
```shell script
docker run -p 8080:8080 -p 8079:8079 fortio/fortio server & # For the server
```
### 测试方式：同时测试/api/,/api/sleep,两个接口观察状态码动态变化
- 测试/api/sleep/\<int:sleep_second\>接口，命令1：`go run .\main.go -c 50 -n 100000 -u http://dev-bmonitoring-nabu.qa.cloudedge.trendmicro.com/api/2`
- 测试/api/sleep/\<int:sleep_second\>接口，命令1：`go run .\main.go -c 50 -n 100000 -u http://dev-bmonitoring-nabu.qa.cloudedge.trendmicro.com/api/3`
- 测试/api/sleep/\<int:sleep_second\>接口，命令1：`go run .\main.go -c 50 -n 100000 -u http://dev-bmonitoring-nabu.qa.cloudedge.trendmicro.com/api/4`
- 测试/api/sleep/\<int:sleep_second\>接口，命令1：`go run .\main.go -c 50 -n 100000 -u http://dev-bmonitoring-nabu.qa.cloudedge.trendmicro.com/api/5`
- 测试/api/sleep/\<int:sleep_second\>接口，命令1：`go run .\main.go -c 50 -n 100000 -u http://dev-bmonitoring-nabu.qa.cloudedge.trendmicro.com/api/6`

### 测试用例
1. [uflask-deployment-v7](../uwsgi/uflask-deployment-v7.yaml): {v7:Configure livenessProbe, readinessProbe, lifecycle, sidecar}  新增Api /api/sleep/\<int:sleep_second\>
2. [uflask-deployment-v8](../uwsgi/uflask-deployment-v8.yaml): {v8:Configure livenessProbe, readinessProbe, lifecycle, sidecar}  新增Api /api/sleep/\<int:sleep_second\>

### 报告
1. preStop=10s
    - /api/sleep/4:出现错误[pdf](./fortio-report/preStop=10,sleep4.pdf)
    - /api/sleep/5:出现错误[pdf](./fortio-report/preStop=10,sleep5.pdf)
2. preStop=20s
    - /api/sleep/4:出现错误[pdf](./fortio-report/preStop=20,sleep4.pdf)
    - /api/sleep/5:出现错误[pdf](./fortio-report/preStop=20,sleep5.pdf)
3. preStop=30s
    - /api/sleep/4:出现错误[pdf](./fortio-report/preStop=20,sleep4.pdf)
    - /api/sleep/5:出现错误[pdf](./fortio-report/preStop=20,sleep5.pdf)
