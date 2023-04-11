from django import forms
from .models import Item

# crate form render as a templateb variable


class ItemForm(forms.ModelForm):  # inherit all the functionality of forms.ModelForm
    class Meta:  # an inner class to provide more information aboutthe form itself
        model = Item
        fields = ['name', 'complete']
