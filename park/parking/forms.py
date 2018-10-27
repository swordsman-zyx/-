from django import forms

class ParkingForm(forms.Form):
    parking_name=forms.CharField(max_length=40,required=False)