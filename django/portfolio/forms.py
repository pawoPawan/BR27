from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'phone_number', 'occupation', 'hobbies', 'achievements', 'profile_picture']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'hobbies': forms.Textarea(attrs={'rows': 3}),
            'achievements': forms.Textarea(attrs={'rows': 3}),
        } 