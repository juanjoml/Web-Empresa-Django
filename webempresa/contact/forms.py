from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre", 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Escribe tu nombre', 'class': 'form-control'}),
        min_length=3, 
        max_length=100)
    email = forms.EmailField(
        label="Email", 
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Escribe tu email', 'class': 'form-control'}),
        min_length=3, 
        max_length=100)
    content = forms.CharField(
        label="Contenido", 
        required=True, 
        widget=forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje', 'class': 'form-control', 'rows': 3}),
        min_length=10, 
        max_length=1000)
