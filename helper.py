from config import *
import math

def decidePageNav(currentPage, totalItemNum):
    ### number of pagenav according to pagenavNum set in config.py###
    res = {"active": 0, "previousPage": 0, "nextPage": 0, "PageNavList": []}

    # need to implement
    totalPage = (int)(math.floor(totalItemNum / 10) + 1)

    bottomIdx = currentPage - (pagenavNum - 1) / 2
    topIdx = currentPage + (pagenavNum - 1) / 2

    if(bottomIdx < 1):
        bottomIdx = 1
    if(topIdx > totalItemNum):
        topIdx = totalItemNum

    activePageIdx = 0
    pageNavList = []

    count = 0
    i = bottomIdx
    while(i <= topIdx):
        if (currentPage == i):
            activePageIdx = count
        pageNavList.append(i)
        i += 1
        count += 1

    previousPageIdx = activePageIdx - 1
    nextPageIdx = activePageIdx + 1

    if(previousPageIdx < 0):
        previousPageIdx = -1
    if(nextPageIdx >= len(pageNavList)):
        nextPageIdx = -1

    res["active"] = activePageIdx
    res["previousPage"] = previousPageIdx
    res["nextPage"] = nextPageIdx
    res["PageNavList"] = pageNavList

    return res