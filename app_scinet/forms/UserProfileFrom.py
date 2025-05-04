from django import forms
from app_scinet.models.UserProfileModel import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'phone_number', 'birth_date', 'location']
        labels = {
            'avatar': 'Avatar',
            'bio': 'Bio',
            'phone_number': 'Numer telefonu',
            'birth_date': 'Data urodzenia',
            'location': 'Lokalizacja',
        }
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Specjalne style dla pola "avatar"
        self.fields['avatar'].widget.attrs.update({
            'accept': 'image/*',
            'class': 'block w-full text-sm file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm '
                     'file:font-semibold file:bg-blue-600 file:text-white hover:file:bg-blue-500'
        })

        # Style dla pozostałych pól
        for name, field in self.fields.items():
            if name != 'avatar':
                field.widget.attrs.update({
                    'class': 'mt-1 block w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm '
                             'focus:ring-blue-500 focus:border-blue-500'
                })
