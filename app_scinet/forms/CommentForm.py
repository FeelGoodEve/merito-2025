from django import forms

# Definiowanie formularza komentarza
class CommentForm(forms.Form):
    content = forms.CharField(
        label="Komentarz",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'class': 'mt-1 block w-full rounded-md border border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50',
            'placeholder': 'Napisz swój komentarz...'
        })
    )
