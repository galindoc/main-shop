from django import forms


class ContentForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        widgets = {
            'section': forms.HiddenInput(),
            'order': forms.HiddenInput(),
        }

    TEXT_ALIGNMENT_CHOICES = (
        ('left', 'Left'),
        ('center', 'Center'),
        ('right', 'Right'),
        ('bottom', 'Bottom'),
        ('top', 'Top'),
        ('over', 'Over'),
    )
    width = forms.IntegerField(
        min_value=20,
        max_value=100,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    text_alignment = forms.ChoiceField(
        choices=TEXT_ALIGNMENT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    # Default color is #000000
    background_color = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'type': 'color', 
                'value': '#88388a',
            }
        )
    )
