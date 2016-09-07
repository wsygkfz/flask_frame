# -*- coding:utf-8 -*-

# __author__ = 'yuzhongfu'
# __mktime__ = '16/8/30'

# 注册路由信息

import www.controller.api as api

import www.controller.website as web


def register_route(app):


    # 以下为提供的接口路由
    api.testApi.TestApi.register(app, route_prefix='/api')



    # 以下为提供的网站路由
    web.testWeb.TestWeb.register(app, route_prefix='/web')





def start():
    """"""


if __name__ == "__main__":
    start()
    

