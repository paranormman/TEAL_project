from django import forms



class csvwithouttime(forms.Form):
    file=forms.FileField()
    sampfreq = forms.NumberInput()

    # def __str__(self):
    #     return self.name + ":"+ str(self.filepath)

