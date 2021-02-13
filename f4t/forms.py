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
    title = forms.CharField(label="",widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter thought title"}))
    subtitle = forms.CharField(label="",widget=forms.TextInput(attrs={"class": "form-control", "placeholder": " subtitle"}))
    post_content = forms.CharField(label="", widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "blog content", "id": "my_blog_content"}))
    audio_content = forms.FileField(label="",widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "choose audio content"}))

    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'post_content','audio_content']


class MemberForm(forms.ModelForm):
    # name = forms.CharField(label="",widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your name here"}))

    # title = forms.EmailField(label="",widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "enter your email"}))

    # phone = forms.CharField(label="",widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter mobile number"}))

    # photo = forms.FileField(label="",widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "provide a photo"}))

    class Meta:
        model = BecomeMember
        fields = ['name','email','phone','photo']