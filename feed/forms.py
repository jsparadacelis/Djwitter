from django import forms

class TweetForm(forms.Form):
    content = forms.CharField(label='Your tweet', max_length=100)