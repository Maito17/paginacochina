from django import forms
from apps.interactions.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tu comentario...'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
