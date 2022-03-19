from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        background_color = request.POST['Background_Color']
        text_color  = request.POST['text_Color']
        # print('The input color that user has given is : ',color_name)
        context = {'background_color': background_color,'text_color':text_color}
        return render(request,'home.html',context)
    return render(request, 'home.html')

