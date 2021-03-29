from django.urls import path

from vstream.views import Index, ListVideo, DetailVideo, stream_video

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('list/', ListVideo.as_view(), name='list-view'),
    path('video/<int:video_id>', DetailVideo.as_view()),
    path('stream/video/<int:video_id>', stream_video, name='detail-video-stream')
]