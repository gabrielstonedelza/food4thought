from django import forms
from food4thought.models import Post,Comment,BecomeMember


class CommentsForm(forms.ModelForm):
    name = forms.CharField(label="",widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your name here"}))
    comment = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'what do you think?', 'id': 'commentform'}))

    class Meta:
        model = Comment
        fields = ['name','comment']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'post_content','audio_content']


class MemberForm(forms.ModelForm):
    class Meta:
        model = BecomeMember
        fields = ['name','email','phone','photo']