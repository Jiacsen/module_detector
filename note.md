# 格式化commit message
## 学习型 Commit 模板
```
格式：(推进完成任务时)
$ <任务名>-<子任务>-v<版本号>
$ <操作关键词>：<做了什么>

$ <总结>：<理解了什么/有什么问题>（可选）
```
示例：
```
task2-subtask2-v1
重构：拆分数据读取函数，模块化处理逻辑

初步理解了如何用函数封装提高代码复用性
```

不过如果是修改bug/readme/注释等呢？目前还没有特别好的模板
## 一些git指令
### 分支
#### 创建分支
```
命令格式：
$ git checkout -b <branch-new> <branch-now>
例子：
$ git checkout -b myfeature develop
表示在develop分支上创建一个名为myfeature的分支
并切换到该分支。等价于以下两条命令：
$ git branch myfeature develop
$ git checkout myfeature
```
按命令格式编写，与当前所在分支无关。

#### 合并分支
```
首先切换到“主分支”
$ git checkout <main-branch>
然后使用命令合并“子分支"
$ git merge --no-ff <sub-branch>
--no-ff参数表示禁止Fast-forward合并，即合并后会生成一个新的commit。
```
注意：合并分支操作与当前所处分支有关。

https://nvie.com/posts/a-successful-git-branching-model/



