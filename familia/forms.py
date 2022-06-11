from django import forms

class Persona1(forms.Form):
    nombre = forms.CharField(label="nombre", max_length=100)
    fecha_nacimiento = forms.DateField (label="fecha_nacimiento", input_formats=["%d/%m/%Y"])
    altura = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': "1.75 m"}))

