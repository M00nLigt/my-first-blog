from django import forms

# class UserForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField()
class UserForm(forms.Form):
     name = forms.CharField(label="Имя")
     lastname = forms.CharField(label="Фамилия")
     patronymic = forms.CharField(label="Отчество")
     field_order = ["lastname", "name"]

     required_css_class = "field"
