from django import forms



class csvwithouttime(forms.Form):
    file=forms.FileField()
    sampfreq = forms.NumberInput()


