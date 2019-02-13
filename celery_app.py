# -*- coding: utf-8 -*- #
"""
:author: sunhailin-Leo
Celery
"""
# urllib
from urllib.parse import quote_plus

# 第三方库
import ujson
import asyncio
import requests
from celery import Celery
# from aiohttp import ClientSession, TCPConnector

# 项目内部库
from db_models import DataModel
from load_config import load_config


def init_celery() -> Celery:
    celery_config = asyncio.run(load_config())['CeleryRedis']

    # 配置uri
    broker_uri = backend_uri = "redis://{User}:{Password}@{Host}:{Port}/{DB}".format(
        User=celery_config['User'],
        Password=quote_plus(celery_config['Password']),
        Host=celery_config['Host'],
        Port=celery_config['Port'],
        DB=celery_config['DB']
    )

    # 配置Celery
    celery_obj = Celery('celery_app', broker=broker_uri, backend=backend_uri)

    return celery_obj


# 获取Celery对象
celery = init_celery()


# Demo任务
@celery.task(bind=True)
def spider(self):
    try:
        # 同步爬虫
        response = requests.get('https://movie.douban.com/j/new_search_subjects?start=0')
        json_res = response.json()
        dumps_res = ujson.dumps(json_res, ensure_ascii=False)

        # 写进数据库
        data = {"data": dumps_res}
        DataModel.create(**data)

        # Celery返回值
        return json_res

        # 异步爬虫
        # async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        #     async with session.get('') as response:
        #         json_res = await response.json()
        #         print(json_res)
        #         dumps_res = ujson.dumps(json_res, indent=4, ensure_ascii=False)
        #         print(dumps_res)
        #
        #         # 写进数据库
        #         data = {"data": dumps_res}
        #         await DataModel.create(**data)
        #
        #         # 返回值
        #         return json_res
    except Exception as err:
        self.retry(exc=err, countdown=5, max_retries=3)
    finally:
        pass


if __name__ == '__main__':
    celery.start()
