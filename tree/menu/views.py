from django.shortcuts import render
from django.views import View


class MenuView(View):

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug', None)
        context = {'menu_name': slug, 'title': slug if slug else 'Главная'}
        return render(request, 'index.html', context)
