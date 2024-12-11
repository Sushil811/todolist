from django import forms
from crispy_forms.helper import FormHelper
from . models import Todo


class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = "__all__"