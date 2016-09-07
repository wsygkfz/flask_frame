# -*- coding:utf-8 -*-

# __author__ = 'yuzhongfu'
# __mktime__ = '16/8/5'

import traceback
from conf.settings import REDIS,g_logger

from flask.ext.classy import route,FlaskView

from www.controller.baseRequest import BaseRequest


class TestWeb(BaseRequest):
    @route('/test', endpoint='test_web')
    def get(self):
        try:
            data = self.__getData()
            code = 200
        except:
            g_logger.error(traceback.format_exc())
            data = []
            code = 500

        return self.render(data,code)

    #@BaseRequest.cacheRedis(REDIS.CACHE_TIMEOUT_1M)
    def __getData(self):
        return "web test is OK !"

