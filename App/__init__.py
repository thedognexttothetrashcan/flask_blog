from flask import Flask,render_template,flash,request,session,abort
from .settings import configDict #导入配置的字典
from .extensions import init_app #初始化第三方扩展库
from .homeviews import home_register_blueprint #注册蓝本
from .adminviews import admin_register_blueprint


def create_app(configMame):
    app = Flask(__name__)
    app.config.from_object(configDict[configMame]) #加载配置类
    init_app(app)
    home_register_blueprint(app) #前台的蓝本的注册
    admin_register_blueprint(app) #后台蓝本的注册
    do_error(app)
    middleware(app)
    return app


#错误处理
def do_error(app):
    @app.errorhandler(404)
    def page_not_found(err):
        flash('您访问的页面不存在')
        return render_template('error.html',title='404 page not found')

    @app.errorhandler(500)
    def server_error(err):
        flash('您访问的太热情了 请稍候再次访问～')
        return render_template('error.html',title='500 server error')


#钩子函数 类似就是django的中间件  在请求和响应之间进行过滤
def middleware(app):
    @app.before_first_request
    def before_first_request():
        print('before_first_request')

    @app.before_request
    def before_request():
        # print(request.path)
        if request.path == '/admin/' and not session.get('aid'):
            abort(500) #跳到后台登录界面
        print('before_request')

    @app.after_request
    def after_request(res):
        print('after_request')
        return res

    @app.teardown_request
    def teardown_request(res):
        print('teardown_request')
        return res







