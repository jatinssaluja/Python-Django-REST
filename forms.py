from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    
    
    class Meta():
        
        model = Post
        fields = ('author','title','text')
        
        widgets = {
            
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'title':  forms.TextInput(attrs={'class':'form-control'}),
            'text':  forms.Textarea(attrs={'class':'form-control','rows':5})    
        }
        
        
class CommentForm(forms.ModelForm):
    
    class Meta():
        model = Comment
        fields = ('author','text')
        
        widgets = {
            
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'text':  forms.TextInput(attrs={'class':'form-control'})
            
        }