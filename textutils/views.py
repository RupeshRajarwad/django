# i have created this file - Rupesh
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    param={'name':'Rupesh','place':'mars'}

    return render(request,'index.html',param)
    #return HttpResponse("Home")

def analyze(request):
    djtext=request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newline','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    print(removepunc)
    #analyzed=djtext
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed=""
    if removepunc=="on":

        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params = {'purpose': 'Remove punctuation', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)
    elif(fullcaps=="on"):
        analyzed =""
        for char in djtext:
            analyzed=analyzed+char.upper()
        param={'purpose':'chaged to Uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',param)

    elif (newlineremover=="on"):
        analyzed =""
        for char in djtext:
            if char!="\n":
                analyzed=analyzed+char
        param = {'purpose': 'Removed newlines', 'analyzed_text': analyzed}
        return render(request,'analyze.html',param)

    elif(extraspaceremover=='on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]==" "and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char
        param = {'purpose': 'Removed Extraspaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)







    else:
        return  HttpResponse("Error")


def ex1(request):
    s=''' <h2> Navigation bar </h2>
    
    
    '''
    return HttpResponse(s)









