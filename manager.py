#-*- coding:utf-8 -*-

__author__ = 'yuzhongfu'
__mktime__ = '16/8/5'


# 程序启动时的全局初始化
from _init_environ.InitEnvironVariable import init_environ_variable
init_environ_variable()



from flask import Flask

from routeUrls import register_route


from flask.ext.login import LoginManager
login_manager = LoginManager()


app = Flask(
    __name__,
    template_folder='www/templates',  # 模板文件路径
    static_folder='www/static',       # 静态文件路径
)

app.secret_key = 'a2V*js%W$xd89saye3qhn&A32lk@'
app.debug = True
login_manager.init_app(app)

# 一个简单的测试API接口
@app.route('/ok')
def inex():
    return 'OK'

# 启动注册路由
register_route(app)


def start_process():
    from flask.ext.script import Manager
    manager = Manager(app)
    manager.run()

if __name__ == '__main__':

    start_process()


