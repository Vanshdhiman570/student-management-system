from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    # name = forms.CharField(max_length=50)
    # roll_no = forms.IntegerField()
    # email = forms.EmailField()
    # course = forms.CharField()

    class Meta:
        model = Student
        fields = '__all__'
        