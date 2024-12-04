from django import forms
from .models import Contact




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone','message']
        widgets = {
            'message': forms.Textarea(attrs={'rows':5,'cols': 20}),
        }

def clean_message(self):
    message = self.cleaned_data['message']
    if len(message) < 100:
        raise forms.ValidationsError("Message must be at least 100 characters")
    return message