from django import forms
from .models import Airport
from django.core.exceptions import ValidationError

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['code', 'parent_code', 'parent_position', 'duration']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_code': forms.Select(attrs={'class': 'form-control'}),
            'parent_position': forms.Select(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        parent = cleaned_data.get('parent_code')
        position = cleaned_data.get('parent_position')

        if parent and position:
            # Prevent duplicate child with same parent and position
            if Airport.objects.filter(parent_code=parent, parent_position=position).exists():
                raise ValidationError(f"An Airport with parent '{parent}' and position '{position}' already exists.")


class FindLastChildForm(forms.Form):
    starting_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    direction = forms.ChoiceField(
        choices=Airport.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class LongestDurationForm(forms.Form):
    start_code = forms.CharField(label="Start Airport Code", max_length=255)
    end_code = forms.CharField(label="End Airport Code", max_length=255)

class ShortestDurationForm(forms.Form):
    start_code = forms.CharField(label="Start Airport Code", max_length=255)
    end_code = forms.CharField(label="End Airport Code", max_length=255)
