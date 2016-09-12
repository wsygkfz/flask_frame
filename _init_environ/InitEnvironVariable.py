# -*- coding:utf-8 -*-

# __author__ = 'yuzhongfu'
# __mktime__ = '16/8/15'


from common.LogManager import get_logger
from common.NgMongo import NGMongoConnect

import conf.settings as settings
from conf.settings import LOGS,DBINFO


# 初始化日志

class InitEnvironVariable():

    def __init__(self,args):

        self.__log_name = args.get("log_name")
        self.__log_level = args.get("log_level")
        self.__log_path = args.get("log_path")
        self.__log_show_stream = args.get("show_stream")

        # 初始化日志
        self.__init_loggr()
        # 初始化数据连接
        self.__init_mongodb()


    def __init_loggr(self):
        settings.g_logger = get_logger(
            strFileName = self.__log_name or LOGS.LOG_NAME,
            debug = self.__log_level or LOGS.LOG_LEVEL,
            showStreamLog = self.__log_show_stream or LOGS.LOG_SHOW_STREAM,
            saveLogPath = self.__log_path or LOGS.LOG_PATH
        )

    def __init_mongodb(self):

        master_host = "mongodb://%s:%s@%s:%d/%s"%(
            DBINFO.USER,
            DBINFO.PASSWD,
            DBINFO.MASTER_IP,
            DBINFO.PORT,
            DBINFO.DB
        )
        slave_host = "mongodb://%s:%s@%s:%d/%s"%(
            DBINFO.USER,
            DBINFO.PASSWD,
            DBINFO.SLAVE_IP,
            DBINFO.PORT,
            DBINFO.DB
        )

        mongo_master = NGMongoConnect(master_host)
        settings.g_master_db = mongo_master.get_database(DBINFO.DB)

        mongo_slave = NGMongoConnect(slave_host)
        settings.g_slave_db = mongo_slave.get_database(DBINFO.DB)


def init_environ_variable(args={}):
    """"""

    InitEnvironVariable(args)


if __name__ == "__main__":
    init_environ_variable()
    

