# Celery + peewee-async Demo

---

<h2 id="DevInfo">Demo 开发环境</h2>

* Author: sunhailin-Leo (Email: 379978424@qq.com)
* Python 版本: Python 3.7.2
* 系统环境: MacOS
* Demo 依赖:
    * celery: 4.2.0 
        * 注: Python 3.7 会有 async 关键字的问题: [Github Issue](https://github.com/celery/celery/pull/4852), by Celery
        * 解决方案: 
            ```bash
            pip3 install --upgrade https://github.com/celery/celery/tarball/master
            ```
    * peewee-async: 0.5.12 
        * 仅支持 Python3.5+ 的异步 ORM 框架，支持 MySQL 和 PostgreSQL，使用 aiomysql、aiopg 作为底层实现
    * peewee: 2.10.2 
        * peewee-async 目前只支持 peewee 3.X 一下的版本, 2.10.2为2.X的最高版本
    * ujson: 1.35 
        * 据说比 json 快...
    * requests: 2.21.0 
        * task 中所依赖的
    * aiofiles: 0.4.0 
        * 异步读取文件内容
* 项目文件介绍:
    * celery_app: 初始化 Celery 和 Celery 任务配置
    * config.json: 配置文件
    * db_models: peewee-async 的实体配置
    * execute_task: 执行任务的方法
    * load_config: 通过 config.json 异步加载配置

---

<h2 id="Info">Demo 简介</h2>

* 本 demo 主要使用 Celery + peewee-async 实现异步执行任务 + 异步写入数据库
* 由于 Celery 暂时不支持 AsyncIO，所以 demo 中的 task 实现是使用同步的方式实现的
* 关于 Celery 的配置 broker 和 backend 都使用了 redis (仅供参考)
* 数据库的表需要自己预先创建 (demo 中没有使用 peewee-async 的建表语句)

---

<h2 id="DemoRunTest">Demo 使用方式</h2>

* 1、修改数据库配置文件和 Celery 配置文件(在 config.json 文件中)

* 2、执行命令执行
```bash
# 在控制台根目录执行
python3.7 celery_app.py worker -l DEBUG

# 启动celery后运行execute_task.py
python3.7 execute_task.py
```