from django import forms
from . models import Student


GENDER_CHOICE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
class StudentForm(forms.ModelForm):
    name = forms.CharField(label='Student Name', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    clas = forms.IntegerField(label='Class', min_value=1, max_value=12, required=True, widget=forms.NumberInput(attrs={'class':'form-control'}))
    dob = forms.DateField(label='Date of Birth', required=True, widget=forms.DateInput(attrs={'class':'form-control', 'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICE, required=True, widget=forms.RadioSelect())
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(label='Phone No',required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Student
        fields = ['name', 'clas', 'dob', 'gender', 'email', 'phone', 'address', 'state', 'image']
        labels = {'address': 'Address', 'state': 'State', 'image': 'Image'}
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 10}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }