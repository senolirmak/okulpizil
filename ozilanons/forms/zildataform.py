from django import forms
from uretim.models import NormalOkul, AksamOkul


class ZilDataForm(forms.ModelForm):
    class Meta:
        model = NormalOkul
        fields = '__all__'
        exclude = ('published_date', 'id')


class AksamZilDataForm(forms.ModelForm):
    class Meta:
        model = AksamOkul
        fields = '__all__'
        exclude = ('published_date', 'id')
