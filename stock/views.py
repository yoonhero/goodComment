from django.shortcuts import render
from django.http import HttpResponse
import requests
import pyglet
from playsound import playsound
from .models import ToDoList, Item, Comment
def icon(request):
    return render(request, 'favicon.png')
def robot(request):
    return render(request, 'robots.txt')
def sitemap(request):
    return render(request, 'sitemap.xml')
# Create your views here.
def home(request):
    num = Comment.objects.all().count()
    h = Comment.objects.all().order_by('-id')[:num]
    
    return render(request, 'home.html', {'num':num, 'posts':h})
def confirm(request):
    if request.POST['num1'] == "":
    
        num = Comment.objects.all().count()
        h = Comment.objects.all().order_by('-id')[:num]
        return render(request, 'home.html', {'num':num, 'posts': h})

    val1 = request.POST['num1']
    def classify(text):
        key = "dd3af340-bc38-11ea-9a09-91ae421c43a0ae2e7ced-d140-40eb-84fc-7d9b297c0473"
        url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

        response = requests.get(url, params={ "data" : text })

        if response.ok:
            responseData = response.json()
            topMatch = responseData[0]
            return topMatch
        else:
            response.raise_for_status()

    if val1 == "":
        pass
    else:
        demo = classify(val1)

        label = demo["class_name"]
        confidence = demo["confidence"]

# CHANGE THIS to something you want your machine learning model to classify
    
    if label == "good":
        #playsound('/Users/yoonseonghyeon/Desktop/programming/python/good.wav')
        #num += 1
        condition = "좋은댓글"
        val1 = val1
        con = "O"
    #good_song.play()
    #pyglet.app.run()
    elif label == "bad":
        #playsound('/Users/yoonseonghyeon/Desktop/programming/python/bad.wav')
        #num -= 1
        condition = "나쁜댓글"
        val1 = ""
        con = "X"

    #bad_song.play()
    #pyglet.app.run()

# CHANGE THIS to do something different with the result
    res = "결과: %d%% 확률로 %s입니다" % (confidence, condition)
    """if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.object.all()
            messages.success(request, ("Item has been added to list!"))
            return render(request, "home.html", {"all_items": all_items})
        else:
            all_items = List.objects.all()
            return render(request, 'home.html', {'all_item': all_items})"""


    
    t = Comment(text = val1)
    if val1 == "":
        pass
    else:
        t.save()
    
    num = Comment.objects.all().count()
    h = Comment.objects.all().order_by('-id')[:num]
    return render(request, 'home.html', {'result':res, 'num':num, 'comment':val1, 'posts': h, 'condition':con})