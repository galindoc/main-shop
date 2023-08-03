from django import forms


class ButtonForm(forms.ModelForm):
    class Meta:
        fields = ('text', 'link')
        widgets = {
            'content': forms.HiddenInput(),
            'content_left': forms.HiddenInput(),
            'content_right': forms.HiddenInput(),
        }


class ContentForm(forms.ModelForm):
    POSITION_CHOICES = (
        (1, 'Left'),
        (2, 'Right'),
    )
    class Meta:
        fields = '__all__'
        widgets = {
            'section': forms.HiddenInput(),
            'order': forms.HiddenInput(),
        }
    # Position field only can be 1 or 2
    position = forms.IntegerField(
        widget=forms.Select(
            choices=POSITION_CHOICES,
            attrs={'class': 'form-control'}
        )
    )
