import web
from webLayout import *
from database import *
from helper import *

urls = (
    '/', 'index',
    '/events', 'events',
    '/contact', 'contact',
    '/previousEvents(.*)', 'previousEvents',
    '/join', 'join',
    '/team', 'team'
)

class index:
    def GET(self):
        return render.index(headerhtml, footerhtml)

class events:
    def GET(self):
        eventsData = getRecentEvents()

        eventListHtml = ""

        for event in eventsData["eventList"]:
            eventBadge = ""
            eventStatus = ""
            if event[4] == 1:
                eventBadge = "badge-success"
                eventStatus = "Done"

            eventTitle = ""
            if event[5] != "":
                eventTitle = '<a href="%s">%s</a>' % (event[5], event[1])
            else:
                eventTitle = event[1]

            tmpEventHtml = """
            <div class="row" style="margin-top: 10px">
            <div class="col-3">
              <span class="badge %s">%s</span>
            </div>
            <div class="col-3">
              %s
            </div>
            <div class="col-3">
              %s
            </div>
            <div class="col-3">
              %s
            </div>
          </div>
            """ % (eventBadge, eventStatus, eventTitle, str(event[2])[:-9], event[3])

            eventListHtml += tmpEventHtml

        return render.Event(headerhtml, eventListHtml, footerhtml)

class contact:
    def GET(self):
        return render.Contact(headerhtml, footerhtml)

class previousEvents:
    def GET(self, name):
        input = web.input()

        page = 1
        try:
            page = int(input.page)
        except:
            page = 1

        # data returned from database
        resData = getPreviousEvents(page)
        if resData["status"] == True:
            # html for each event
            resultHtml = organizeContent(resData["data"]["showList"])

            # html for pageNav at the bottom
            pageNavConfig = decidePageNav(resData["page"], int(math.floor(resData["total"] / eventNumPerPage + 1)))

            # TODO: implement pageNav in html
            print(pageNavConfig)

            resultHtml += '''
            <nav aria-label="Page navigation example">
              <ul class="pagination justify-content-center">
              '''

            # take care of previous page
            if(pageNavConfig["previousPage"] == -1):
                resultHtml += '''
                <li class="page-item disabled">
                  <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
                </li>
                '''
            else:
                resultHtml += '''
                <li class="page-item disabled">
                  <a class="page-link" href="previousEvents?page=%s">Previous</a>
                </li>
                ''' % (str(pageNavConfig["PageNavList"][pageNavConfig["previousPage"]]))

            # take care of each page
            for subIdx in pageNavConfig["PageNavList"]:
                if(subIdx == pageNavConfig["PageNavList"][pageNavConfig["active"]]):
                    resultHtml += '''
                    <li class="page-item active"><a class="page-link" href="previousEvents?page=%s">%s</a></li>
                    ''' % (str(subIdx), str(subIdx))

                else:
                    resultHtml += '''
                    <li class="page-item"><a class="page-link" href="previousEvents?page=%s">%s</a></li>
                    ''' % (str(subIdx), str(subIdx))

            # take care of next page
            if (pageNavConfig["nextPage"] == -1):
                resultHtml += '''
                    <li class="page-item disabled">
                      <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Next</a>
                    </li>
                    '''
            else:
                resultHtml += '''
                    <li class="page-item">
                      <a class="page-link" href="previousEvents?page=%s">Next</a>
                    </li>
                    ''' % (str(pageNavConfig["PageNavList"][pageNavConfig["nextPage"]]))

            resultHtml += '''
                </ul>
            </nav>
            '''

            return render.previousEvents(headerhtml, footerhtml, resultHtml)
        else:
            # resData = getPreviousEvents(1)
            raise web.redirect(websiteURL + '/previousEvents')

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
