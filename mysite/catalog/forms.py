from django import forms
from .models import Product, Version
from .const import BLACK_LIST_WORDS


def check_words_in_text(text: str, words: list):
    for word in words:
        if word in text:
            return True
    return False


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('slug', 'create_date', 'last_change_date', 'view_count', 'user_email')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        if check_words_in_text(cleaned_data, BLACK_LIST_WORDS):
            raise forms.ValidationError('Ошибка, нельзя использовать запрещенное слово')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        if check_words_in_text(cleaned_data, BLACK_LIST_WORDS):
            raise forms.ValidationError('Ошибка, нельзя использовать запрещенное слово')

        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'