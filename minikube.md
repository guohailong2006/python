---
title: minikube 安装
date: 2018-06-12 10:53:24
---
由于minikube 大家在使用过程中，常规的做法，可能由于网络原因，不能安装使用，本篇文章用的aliyun 的镜像，会更加的稳定~

## 两种platom 的使用方式

### mac os

``` bash
$ curl -Lo minikube http://kubernetes.oss-cn-hangzhou.aliyuncs.com/minikube/releases/v0.28.0/minikube-darwin-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```


### linux

``` bash
$ curl -Lo minikube http://kubernetes.oss-cn-hangzhou.aliyuncs.com/minikube/releases/v0.28.0/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```

### more link
More info: [aliyun](https://yq.aliyun.com/articles/221687)
