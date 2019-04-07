import web
from webLayout import *
from database import *

urls = (
    '/', 'index',
    '/events', 'events',
    '/contact', 'contact',
    '/previousEvents', 'previousEvents',
    '/join', 'join',
    '/team', 'team'
)

class index:
    def GET(self):
        return render.index(headerhtml, footerhtml)

class events:
    def GET(self):
        return render.Event(headerhtml, footerhtml)

class contact:
    def GET(self):
        return render.Contact(headerhtml, footerhtml)

class previousEvents:
    def GET(self):
        return render.previousEvents(headerhtml, footerhtml)

class join:
    def GET(self):
        return render.Join(headerhtml, footerhtml)

class team:
    def GET(self):
        return render.Team(headerhtml, footerhtml)

render = web.template.render('templates/')
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
