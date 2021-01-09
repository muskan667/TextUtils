from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):

    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcounter= request.POST.get('charcounter','off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed =analyzed + char.upper()
        params = {'purpose': 'changed to upper case', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover =="on":
        analyzed = ""
        for char in djtext:
            if (char !="\n" and char !="\r"):
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover =="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if (djtext[index] == " " and djtext[index+1] == " "):
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if  charcounter =="on":
        analyzed = len(djtext)
        params = {'purpose': 'Extra space remover Remover', 'analyzed_text': analyzed }
        djtext = analyzed

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charcounter!="on"):
        return HttpResponse("error")

    return render(request, 'analyze.html', params)

