from django import forms

class CompanyForm(forms.Form):
    company_name=forms.CharField(max_length=20)