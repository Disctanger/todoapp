from bootstrap3_datetime.widgets import DateTimePicker

from django import forms


from .models import (List, Item)

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = [
            "title"
            ]

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False})
        
        fields = [
            "title",
            'due_Date',
                        ]

class ItemCompleteForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = []

class ItemDeleteForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = []

class ListDeleteForm(forms.ModelForm):
    class Meta:
        model = List
        fields = [
            ]

class ToDoForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    due_Date = forms.DateTimeField(
        widget=DateTimePicker(options={"format": 'YYYY-MM-DD HH:mm',
                                       "pickSeconds": False}))
    
    class Meta:
        model = Item
        widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                       "pickSeconds": False})
        
        fields = [
            'title',
            'due_Date'
            ]
