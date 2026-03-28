from django import forms
from .models import Game

class GameUploadForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'title',
            'description',
            'category',
            'thumbnail',
            'download_url',
            'download_url_android',
        ]
