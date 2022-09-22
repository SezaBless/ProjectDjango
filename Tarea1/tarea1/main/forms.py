from django import forms
from .models import Blog, ContactProfile, Testimonial

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#se ´pudo haber llegado a modificar pero no se realizo ningun cambio 
"""
class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..',
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': '*Message..',
			'rows': 6,
			}))

class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'message',)
		
"""
#se agrega para el login
class CreateUserForm(UserCreationForm):
	class meta :
		model = User 
		fields =["username", "email", "pasword1", "pasword2"]

#se agrega para la creacion de blog 
class BlogForm(forms.ModelForm):
	author = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
			'placeholder':'Author name...',
		}))
	name = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
			'placeholder':'Full name...',
		}))
	description = forms.CharField(max_length=500, required=True,
		widget=forms.TextInput(attrs={
			'placeholder':'description...',
		}))

	image = forms.ImageField()

	body = forms.CharField(max_length=2000, required=True,
		widget=forms.TextInput(attrs={
			'placeholder':'info...',
		}))

	class Meta: 
		model = Blog
		fields =['author', 'name', 'description', 'body', 'image']
#se agrega para los comentarios
class TestimonialForm(forms.ModelForm):

	thumbnail = forms.ImageField()
	name = forms.CharField(max_length=200, required=True,
			widget=forms.TextInput(attrs={
				'placeholder':'Author name...',
			}))
	
	quote = forms.CharField(max_length=500, required=True,
			widget=forms.TextInput(attrs={
				'placeholder':'comment...',
			}))	
  
	class Meta: 
		model = Testimonial
		fields =['thumbnail', 'name', 'role', 'quote']
		