from django import forms



class EntryForm(forms.Form):
    title = forms.CharField(
        label="Title", 
        max_length=100, 
        required=True,
        )
    body = forms.CharField(
        label="Body", 
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}), 
        required=True,
        )

