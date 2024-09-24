from django import forms


class EntryForm(forms.Form):
    title = forms.CharField(
        label="Title", 
        max_length=100, 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Your title input here...'})
    )

    body = forms.CharField(
        label="Body",
        required=True, 
        widget=forms.Textarea(attrs={'placeholder': '# Title... Enter the body content here...'}), 
    )

