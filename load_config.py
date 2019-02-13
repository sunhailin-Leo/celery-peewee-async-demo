# -*- coding: utf-8 -*- #
"""
:author: sunhailin-Leo
Celery
"""
import ujson
import aiofiles


async def load_config(config_path: str = 'config.json') -> dict:
    """
    异步加载文件
    :param config_path: 配置文件目录
    :return: 配置详情
    """
    async with aiofiles.open(config_path, mode='r') as f:
        config = ujson.loads(await f.read())
        return config
