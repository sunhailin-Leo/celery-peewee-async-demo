# -*- coding: utf-8 -*- #
"""
:author: sunhailin-Leo
"""
import asyncio
from peewee import Model, CharField
from peewee_async import Manager, MySQLDatabase

# 项目内部库
from load_config import load_config


# 加载数据库配置文件
def init_db() -> MySQLDatabase:
    db_config = asyncio.run(load_config())['DataBase']

    # 定义数据库对象
    db = MySQLDatabase(
        database=db_config['DB'],
        user=db_config['User'],
        password=db_config['Password'],
        host=db_config['Host'],
        port=db_config['Port']
    )
    return db


# 初始化数据
database = init_db()


# 实体类
class DataModel(Model):
    data = CharField(max_length=4096, null=False, db_column='data')

    class Meta:
        database = database
        primary_key = False
        db_table = "t_data"


# 创建异步实体管理
objects = Manager(database)

# 不开启同步任务
database.set_allow_sync(True)
