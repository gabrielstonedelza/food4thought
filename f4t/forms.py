from django import forms
from food4thought.models import Thought,Comment,BecomeMember


class CommentsForm(forms.ModelForm):
    name = forms.CharField(label="",widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your name here"}))
    comment = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'what do you think?', 'id': 'commentform'}))

    class Meta:
        model = Comment
        fields = ['name','comment']

class ThoughtForm(forms.ModelForm):

    class Meta:
        model = Thought
        fields = ['title',  'author','bible_quotations','audio_content']


class MemberForm(forms.ModelForm):
    class Meta:
        model = BecomeMember
        fields = ['name','email']