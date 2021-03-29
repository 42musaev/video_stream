from django import forms
from vstream.models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('name', 'video',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control'})
        }
