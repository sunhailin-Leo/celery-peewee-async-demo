# Celery + peewee-async Demo

---

<h3 id="DevInfo">Demo开发环境</h3>

* Author: sunhailin-Leo (Email: 379978424@qq.com)
* Python版本: Python 3.7.2
* IDE版本: Pycharm 3.2
* 系统环境: MacOS
* Demo依赖:
    * celery: 4.2.0 (4.2.1在Python3.7下使用redis有问题)
    * peewee-async: 0.5.12 (仅支持Python3.5+的异步ORM框架，支持MySQL和PostgreSQL，使用aiomysql, aiopg作为底层实现)
    * peewee: 2.10.2 (peewee-async目前只支持peewee 3.X一下的版本, 2.10.2为2.X的最高版本)
    * ujson: 1.35 (据说比json快...)
    * requests: 2.21.0 (task中所依赖的)
    * aiofiles: 0.4.0 (异步读取文件内容)
* 项目文件介绍:
    * celery_app: 初始化celery和celery任务配置
    * config.json: 配置文件
    * db_models: peewee-async的实体配置
    * execute_task: 执行任务的方法
    * load_config: 通过config.json异步加载配置

---

<h3 id="Info">Demo简介</h3>

* 本demo主要使用celery + peewee-async实现异步执行任务 + 异步写入数据库
* 由于celery暂时不支持AsyncIO，所以demo中的task实现是使用同步的方式实现的
* 关于Celery的配置broker和backend都使用了redis(仅供参考)
* 数据库的表需要自己预先创建(demo中没有使用peewee-async的建表语句)

---

<h3 id="DemoRunTest">Demo使用方式</h3>

* 1、修改数据库配置文件和Celery配置文件(在config.json文件中)

* 2、执行命令执行
```bash
# 在控制台根目录执行
python3.7 celery_app.py worker -l DEBUG

# 启动celery后运行execute_task.py
python3.7 execute_task.py
```