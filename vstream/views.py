import mimetypes
import os
from wsgiref.util import FileWrapper

from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from vstream.forms import VideoForm
from vstream.models import Video
from vstream.utils import range_re, RangeFileWrapper


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


class ListVideo(ListView):
    model = Video
    template_name = 'vstream/list-video.html'


def stream_video(request, video_id):
    range_header = request.META.get('HTTP_RANGE', '').strip()
    range_match = range_re.match(range_header)
    video = Video.objects.get(pk=video_id)
    size = os.path.getsize(video.video.path)
    content_type, encoding = mimetypes.guess_type(video.video.path)
    content_type = content_type or 'application/octet-stream'
    if range_match:
        first_byte, last_byte = range_match.groups()
        first_byte = int(first_byte) if first_byte else 0
        last_byte = int(last_byte) if last_byte else size - 1
        if last_byte >= size:
            last_byte = size - 1
        length = last_byte - first_byte + 1
        resp = StreamingHttpResponse(RangeFileWrapper(open(video.video.path, 'rb'), offset=first_byte, length=length),
                                     status=206, content_type=content_type)
        resp['Content-Length'] = str(length)
        resp['Content-Range'] = 'bytes %s-%s/%s' % (first_byte, last_byte, size)
    else:
        resp = StreamingHttpResponse(FileWrapper(open(video.video.path, 'rb')), content_type=content_type)
        resp['Content-Length'] = str(size)
    resp['Accept-Ranges'] = 'bytes'
    return resp


class DetailVideo(View):
    def get(self, request, video_id):
        return render(request, 'vstream/detail-video.html', {'video_id': video_id})
