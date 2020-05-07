from django import forms
from english_dict.models import PartProperty


class SelectWordForm(forms.Form):
    frequency = forms.BooleanField(label='Частотные', required=False)
    word_type = forms.ModelChoiceField(label='Тип слов', required=False, queryset=PartProperty.objects.all())


class TranslateForm(forms.Form):
    input_text = forms.CharField(widget=forms.Textarea, required=False)
