# I have created this File -----Wahaj Raza
from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    return render(request,"index.html")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    punc = request.POST.get('removepunc', 'off')
    upper = request.POST.get("fullcaps","off")
    removespace = request.POST.get("removespace","off")
    charcount = request.POST.get("charcount","off")
    if punc == "on":
        punctuations = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params={"purpose":"Removed Punctuations","analyzed_text":analyzed}
        djtext = analyzed
    if upper == "on":
        analyzed = djtext.upper()
        params = {"purpose":"Upper Case","analyzed_text":analyzed}
        djtext = analyzed
    if removespace == "on":
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed+=char
        params = {"purpose": "Space Removed", "analyzed_text": analyzed}
        djtext = analyzed
    if charcount == "on":
        analyzed = f"No of Character {len(djtext)}"
        params = {"purpose": "Space Removed", "analyzed_text": analyzed}
        djtext = analyzed
    if charcount != "on" and removespace != "on" and punc !="on" and upper !="on":
        return HttpResponse("Error")
    return render(request, "analyze.html", params)