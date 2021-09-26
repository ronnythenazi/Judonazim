from django.shortcuts import render
from . import storedata

def fhomepage(request):

    #this line of codes create dirs and files in staticfile
    #in addition, it also example of sending data
    #from python code to html files#
    #result = storedata.fpublish_opinion()
    #mylist = {"output":result}
    #return render(request, 'debug.html',mylist)



    return render(request, 'writeOpinion.html')
    #return render(request, 'index.html')
    #return render(request, 'texteditor.html')
    #return render(request, 'static/plugins/mdb/src/index.html')
def ftxteditor(request):
    return render(request, 'texteditor.html')
    #return render(request, 'menuicon.html')
