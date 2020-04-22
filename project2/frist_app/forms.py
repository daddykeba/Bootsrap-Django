from django import forms
from django.core import validators
from frist_app.models import Topic

def check_for_z(value):
	if value[0].lower() != 'z':
		raise forms.ValidationError("Le nom doit commencer par un z")

class FormName(forms.Form):
	"""docstring for FormName"""

	name = forms.CharField(validators=[check_for_z])
	email = forms.EmailField()
	verify_email = forms.EmailField(label="Entrer encore votre email")
	text = forms.CharField(widget=forms.Textarea)
	botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

	def clean_botcatcher(self):
		botcatcher = self.cleaned_data['botcatcher']

		if len(botcatcher) > 0:
			raise forms.ValidationError("Gotcha Both")
		return botcatcher

	def clean(self):
		# all_clean_data = super(FormName).clean()
		email = self.cleaned_data['email']
		vmail = self.cleaned_data['verify_email']

		if email != vmail:
			raise forms.ValidationError("Les deux email sont differents")

class TopicForm(forms.ModelForm):
	"""docstring for UserForm"""
	class Meta:
		model = Topic
		fields = '__all__'
		
	
