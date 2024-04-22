from django import forms
class selection(forms.Form):
    select =forms.IntegerField(label="Enter range to generate number list",max_value=1000,min_value=1)
