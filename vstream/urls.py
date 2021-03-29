from django.urls import path

from vstream.views import Index, ListVideo, DetailVideo, stream_video, DetailVideoApi

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('list/', ListVideo.as_view(), name='list-view'),
    path('video/<int:video_id>', DetailVideo.as_view(), name='detail-video'),
    path('api/video/<int:video_id>', DetailVideoApi.as_view(), name='api-detail-video'),
    path('stream/video/<int:video_id>', stream_video, name='detail-video-stream')  # Duplicate function
]
