from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User  
        fields = ['username', 'first_name']
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "帳號"
        self.fields['first_name'].label = "姓名"        
        
class PasswordForm(ModelForm):
    class Meta:
        model = User  
        fields = ['password']
        
    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = "密碼"