from django.http import request
from django.shortcuts import render
from django.views.generic.base import View


class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'Jorge Orellana',
            'years': 30,
            'codes': ['Python', 'JavaScript', 'Java', 'C#']
        }
        return render(request, 'hello_world.html', context=data)
