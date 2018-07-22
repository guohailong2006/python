---
title: 对docker metadata的理解
date: 2018-03-07 20:53:24
---

## 相关目录的理解：

/var/lib/docker/devicemaper/devicemaper/data     shaper 目录
/var/lib/docker/devicemaper/devicemaper/medata   元存储目录

一次事故中发现，docker 的metadata在不进行特殊划分处理，它的缺省空间是不够的，可能会导致由于metadata产生的“空间报错”，这会导致docker service启动失败
我们可以通过查看一个容器的信息，例:docker info 我们可以知道metadata 只能存储107.4GB 的文件



###查询资料后，从两方面进行devicemapper进行处理


### 方法一：
通过挂载一个较大的磁盘，然后通过docker -g 改变存储路径到新的磁盘，将data目录dd 放大，然后link 到data



### 方法二：
观察docker 的启动参数，进行docker 的storage 的存储的路径的改变官方提供的方案是进行在进行docker storage的策略修改，比如修改成一个overlay的方案

