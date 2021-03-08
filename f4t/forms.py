from django import forms
from food4thought.models import Thought, FeedBack, BecomeMember, Testimony


class FeedBackForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "enter your name here"}))
    message = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'what do you think?', 'id': 'messageform'}))

    class Meta:
        model = FeedBack
        fields = ['name', 'message']


class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['title', 'author', 'bible_quotations', 'audio_content']


class MemberForm(forms.ModelForm):
    class Meta:
        model = BecomeMember
        fields = ['name', 'email']


class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['name', 'testimony']