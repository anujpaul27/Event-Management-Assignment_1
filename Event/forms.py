from django import forms 
from .models import *


class EventForm (forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full p-3 text-white-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:text-white',
                'placeholder': 'Name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'block w-full p-3 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:text-white',
                'rows': 5,
                'placeholder': 'Write a description of the event...'
            }),

            'date': forms.DateInput(attrs={
                'class': 'block w-full p-3 text-white-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:text-white',
                'placeholder': 'Date Y-M-D'
            }),
            'time': forms.TimeInput(attrs={
                'class': 'block w-full p-3 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:text-white',
                'placeholder': 'time  H:M:S' 
            }),
            'location': forms.TextInput(attrs={
                'class': 'block w-full p-3 text-white-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:text-white',
                'placeholder': 'Location'
            }),
            
            'category': forms.Select(attrs={
                'class': 'block w-full p-3 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:text-white',
                'placeholder': 'Select Category'
            }),

        }


class CatagoriForm (forms.ModelForm):
    class Meta: 
        model = Category
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full p-3 text-white-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:text-white',
                'placeholder': 'Name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'block w-full p-3 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:text-white',
                'rows': 5,
                'placeholder': 'Write a description of the event...'
            }),            
            
        }
    
class ParticipantForm (forms.ModelForm):
    class Meta:
        model = Participant
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full p-3 text-white bg-gray-800 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter participant name',                

            }),
            'email': forms.EmailInput(attrs={
                'class': 'block w-full p-3 text-white-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:text-white',
                'placeholder': 'Email'
            }),
            'events': forms.CheckboxSelectMultiple(attrs={
                'class': 'text-white'
            })
        }
