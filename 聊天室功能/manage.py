import os

import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.options import define, options, parse_command_line
from tornado.web import url

# 定义端口，是否调试模式
define('port', default=8000, type=int)
define('debug', default=True, type=bool)

# 项目根路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 登录页面
class LoginHandler(tornado.web.RequestHandler):
    # 表示进入登录页面
    def get(self):
        # render 渲染
        self.render('login.html')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')

        if username == 'lala' or username == 'nana':
            self.set_secure_cookie('username', username, expires_days=1)
            self.redirect(self.reverse_url('chat'))
        else:
            self.redirect(self.reverse_url('login'))



# 聊天页面
class ChatHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_secure_cookie('username')
        self.render('chatroom.html', username=username)


class ChatRoomHandler(tornado.websocket.WebSocketHandler):
    online_users = []

    # 连接： 当用户连接时自动调用
    def open(self, *args, **kwargs):
        self.online_users.append(self)

    # 接收到用户发送过来的消息
    def on_message(self, message):
        username = self.get_secure_cookie('username')
        for user in self.online_users:
            user.write_message('【%s】：%s' % (username, message))

    # 关闭：当用户退出聊天室时自动调用
    def on_close(self):
        self.online_users.remove(self)



def make_app():
    return tornado.web.Application(
        handlers=[
            url(r'/', LoginHandler, name='login'),
            url(r'/chat/', ChatHandler, name='chat'),
            url(r'/chatroom/', ChatRoomHandler, name='chatroom')
        ],
        debug=options.debug,
        template_path=os.path.join(BASE_DIR, 'templates'),
        cookie_secret='abc1234'
    )


if __name__ == '__main__':
    parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()