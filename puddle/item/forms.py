from django import forms 
from .models import Item

INPUT_CLASS = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image',)

        widgets = {
            'category':forms.Select(attrs={
                'class' : INPUT_CLASS
            }),
            'name':forms.TextInput(attrs={
                'class' : 'w-full py-4 px-6 rounded-xl border'
            }),
            'description':forms.Textarea(attrs={
                'class' : 'w-full py-4 px-6 rounded-xl border'
            }),
            'price':forms.TextInput(attrs={
                'class' : 'w-full py-4 px-6 rounded-xl border'
            }),
            'image':forms.FileInput(attrs={
                'class' : 'w-full py-4 px-6 rounded-xl border'
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','description','price','image','is_sold')

        widgets = {
            'name':forms.TextInput(attrs={
                'class' : 'w-full py-4 px-6 rounded-xl border'
            }),
            'description':forms.Textarea(attrs={
                'class' : 'w-full py-4 px-6 rounded-xl border'
            }),
            'price':forms.TextInput(attrs={
                'class' : 'w-full py-4 px-6 rounded-xl border'
            }),
            'image':forms.FileInput(attrs={
                'class' : 'w-full py-4 px-6 rounded-xl border'
            }),
        }