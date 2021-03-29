from django.shortcuts import render, redirect
from django.views import View

from vstream.forms import VideoForm


class Index(View):
    def get(self, request):
        form = VideoForm()
        return render(request, 'vstream/index.html', {'form': form})

    def post(self, request):
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'vstream/index.html')
        return render(request, 'vstream/index.html', {'form': form})
