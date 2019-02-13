# -*- coding: utf-8 -*- #
"""
:author sunhailin-Leo
执行任务
"""

# 项目内部库
from celery_app import spider


def start_spider():
    # 执行Celery任务
    task = spider.apply_async()
    print(task)


if __name__ == '__main__':
    start_spider()
