from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    # print(type(gmtime()))
    # print(type(strftime("%Y-%m-%d %H:%M %p", gmtime())))
    # print(strftime("%Y/%m/%d", gmtime()))

    context = {
        "time": strftime( "%Y-%m-%d %H:%M %p", gmtime() ),
        "name":"dodo",
    }
    return render(request,'index.html',context)

