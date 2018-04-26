from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from TenderServer import app

if __name__ == '__main__':
    container = WSGIContainer(app)
    http_server = HTTPServer(container)
    http_server.listen(9000)
    IOLoop.instance().start()
