from django import forms
from .models import Checkout

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['student', 'instrument', 'notes']
        # You can include additional widgets, labels, or help_text as needed
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'instrument': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    # If you want to add custom validation or logic, you can do so here.
