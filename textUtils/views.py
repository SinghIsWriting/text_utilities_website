from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
        return render(request,'index.html')

def contact(request):
        return render(request, 'contact.html')


def analyze(request):
	djtext = request.POST.get('text','default')
	removepunc1 = request.POST.get('removepun','off')
	caps = request.POST.get('caps','off')
	newlineremover = request.POST.get('newlineremover','off')
	extraspaceremover = request.POST.get('spaceremover','off')
	charcount = request.POST.get('charcount','off')

	o = djtext
	if removepunc1 == "on":
		analyzed = ""
		puntuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
		for char in djtext:
			if char not in puntuations:
				analyzed = analyzed + char
		params = {'purpose':'Removed Punctuations','analyzed_text':analyzed, 'main': o}
		djtext = analyzed
	if caps == "on":
		analyzed = ""
		for char in djtext:
			analyzed = analyzed + char.upper()
		params = {'purpose':'Converted to uppercase','analyzed_text':analyzed, 'main': o}
		djtext = analyzed
	if newlineremover == "on":
		analyzed = ""
		for char in djtext:
			if char != "\n" and char != "\r":
				analyzed = analyzed + char
		params = {'purpose':'Removed newlines','analyzed_text':analyzed, 'main': o}
		djtext = analyzed
	if extraspaceremover == "on":
		analyzed = ""
		for index, char in enumerate(djtext):
			if not(djtext[index] == " " and djtext[index+1] == " "):
				analyzed = analyzed + char
			else:
				pass
		params = {'purpose':'Removed Extra Spaces','analyzed_text':analyzed, 'main': o}
		djtext = analyzed
	if charcount == "on":
		count = 0
		for char in djtext:
			if char != " " and len(char) != 0:
				count = count + 1
		if (removepunc1 == "on" or caps == "on" or newlineremover == "on" or extraspaceremover == "on"):
			params = {'purpose':'Characters count','djt':djtext,'analyzed_text':"Total number of characters : "+str(count), 'main': o}
		else:
			params = {'purpose':'Removed Extra Spaces','analyzed_text':"Total number of characters : "+str(count), 'main': o}
		djtext = count
	if (removepunc1 != "on" and caps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
		return render(request, 'error.html')

	return render(request, 'analyze.html', params)

