# -*- coding:utf-8 -*-

# __author__ = 'yuzhongfu'
# __mktime__ = '16/8/5'


import time,json
import traceback

from flask import request, make_response

from flask.ext.classy import FlaskView
from conf.settings import g_logger,g_redis


class BaseRequest(FlaskView):

    route_base = ''

    def __init__(self):
        pass

    def before_request(self,name):
        # 程序运行的初始时间
        self._request_start_time = time.time()
        # 语言
        self._language = request.args.get('language', 'en')
        # ip
        self._ip = request.remote_addr

        # 是否callback
        self._callback = request.args.get('callback')


    def _render(self,data,code=1000, status_code=200):
        ''' 按格式输出数据 '''
        #执行时间
        exec_time = time.time() - self._request_start_time

        # 返回的数据的结构
        data = {'code':int(code), 'time':exec_time, 'data':data}
        json_data = json.dumps(data)
        # 针对 jsonp
        if self._callback:
            json_data = "%s(%s)"%(self._callback,json_data)
        response = make_response(json_data)

        return response, status_code


    @staticmethod
    def cacheRedis(cache_time):
        def wrapsFun(func):
            def __wrapsFun(*args, **kwargs):
                #每一个请求的URL参数组成的键值
                redis_key = args[0]._getRedisKey()
                # 先从redis获取对应的结果,有值直接返回
                try:
                    redis_content = g_redis.get(redis_key)
                    if redis_content:
                        return json.loads(redis_content)
                except:
                    g_logger.error(traceback.format_exc())
                # 如果redis没有值，按对应的请求获取结果
                redis_content = func(*args, **kwargs)
                try:
                    # 保存结果到redis中
                    g_redis.setex(redis_key, json.dumps(redis_content), cache_time)
                except:
                    g_logger.error(traceback.format_exc())
                return redis_content

            return __wrapsFun

        return wrapsFun
