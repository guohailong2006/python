---
title: ElasticSearch 性能优化与实践总结
---
性能优化的几点方向：

## 每个nodes 的的分片的设置

``` bash
$ index.routing.allocation.total_shards_per_node

```
表示每个nodes 最大的shards 的数量。   假如10个分片，0个索引，一个副本，4个nodes，即(10+10)/4=5  即�但是实际我们应该比其设置的更大点，因为假如某个nodes的下线，就可能分片迁移失败


## 线程连接数

``` bash
$ thread_pool.bulk.queue_size: 5000 

```
这个为了防止较高，吃cpu，也是为了调高，提高es 的调用程序的效率

## shards 的设定

假如是多个nodes，如果是搜索场景，每个shards 不能超过15g，如果是日志场景，每个shards 不要超过30g

默认是五个shards，简单可以先调整成单个shards ，这样就能知道多大的量，然后用shard 单个（即总量）/nodes 数量就会得到每个shards 的量

另：基于磁盘的分片

``` bash
$ cluster.routing.allocation.disk.threshold_enabled：true

```

## 写性能优化
调整translog 的参数：如refresh_interval ,index.translog.durability: async  、index.translogthred.size

## jvm 的参数的调优
准则：内存与存储量之比
一、搜索类1:16
二、日志类：1：48

## 分片重新分片与恢复设置

``` bash
indices.recovery.max_size_per_sec: 0

```
设置数据恢复时限制的带宽，如入100mb，默认为0，即无限制。

``` bash
indices.recovery.concurrent_streams: 5
```
设置这个参数来限制从其它分片恢复数据时最大同时打开并发流的个数，默认为5

