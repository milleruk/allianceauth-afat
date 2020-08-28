# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _


class AFatLinkForm(forms.Form):
    name = forms.CharField(label=_("Fleet Name"), max_length=50)
    type = forms.IntegerField(label=_("Type"), required=False)


class AFatFlatListForm(forms.Form):
    flatlist = forms.CharField(widget=forms.Textarea)


class AFatManualFatForm(forms.Form):
    character = forms.CharField(label=_("Character Name"), max_length=50)
    system = forms.CharField(label=_("System"), max_length=50)
    shiptype = forms.CharField(label=_("Ship Type"), max_length=100)


class AFatClickFatForm(forms.Form):
    name = forms.CharField(label=_("Fleet Name"), max_length=50)
    duration = forms.IntegerField(label=_("Duration"), min_value=1)
    type = forms.IntegerField(label=_("Type"), required=False)