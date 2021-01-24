from django import forms
from ozilanons.models import DuyuruData


class DuyuruDataForm(forms.ModelForm):
    class Meta:
        model = DuyuruData
        metin = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))
        # fields = ('metin', 'guncellendi','zilaktif', 'mp3yolu')
        fields = ('metin',)
        exclude = ('duyurutarihi', 'id')


class ZilDurumForm(forms.ModelForm):
    class Meta:
        model = DuyuruData
        zilaktif = forms.CharField(widget=forms.CheckboxInput)
        fields = ('zilaktif',)
        exclude = ('duyurutarihi', 'id')
