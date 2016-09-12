# -*- coding:utf-8 -*-

# __author__ = 'yuzhongfu'
# __mktime__ = '16/8/5'

import os
import logging

# 入口程序运行的目录
g_cur_process_run_path = os.getcwd()

g_root_path = os.path.dirname(os.path.realpath(__file__))
# 代码存放的根目录
g_root_path = os.path.dirname(g_root_path)

# 日志相关配置
# 日志句柄
g_logger = None
class LOGS():

    # 日志文件名
    LOG_NAME = "api_web.log"
    # 定义的日志级别
    LOG_LEVEL = logging.ERROR
    # 是否显示日志到屏幕
    LOG_SHOW_STREAM = True
    # 日志保存的目录
    LOG_PATH = g_cur_process_run_path


# 主从数据连接句柄
g_master_db = None
g_slave_db = None
class DBINFO:

    # # 国外数据库主库IP
    # MASTER_IP = ""
    # # 国外数据库从库IP
    # SLAVE_IP = ""
    #
    # PORT = 47077
    #
    # USER = ""
    # PASSWD = ""

    # # local 只为测试使用
    MASTER_IP = "127.0.0.1"
    SLAVE_IP = "127.0.0.1"
    PORT = 27017
    USER = ""
    PASSWD = ""

    DB = "mallcenter"

# 缓存redis
g_redis = None
class REDIS:

    # redis的相关机器信息
    CACHE_MACHINE = "127.0.0.1"
    CACHE_PORT = 6381
    CACHE_DB = 6

    # 分别缓存的单位时间（秒）
    CACHE_TIMEOUT_10S  = 10
    CACHE_TIMEOUT_30S  = 30
    CACHE_TIMEOUT_1M  = 60
    CACHE_TIMEOUT_5M  = 5 * 60
    CACHE_TIMEOUT_10M = 10 * 60
    CACHE_TIMEOUT_30M = 30 * 60
    CACHE_TIMEOUT_1H  = 60 * 60
    CACHE_TIMEOUT_2H  = 2 * 60 * 60
    CACHE_TIMEOUT_5H  = 5 * 60 * 60
    CACHE_TIMEOUT_1D  = 24 * 60 * 60
    CACHE_TIMEOUT_1W  = 7 * 24 * 60 * 60



def start():
    """"""


if __name__ == "__main__":
    start()

