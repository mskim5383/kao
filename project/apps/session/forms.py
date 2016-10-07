from models import UserProfile
from django.contrib.auth.models import User
from django.forms import ModelForm



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        repassword = kwargs.pop('repassword', '')
        super(UserForm, self).__init__(*args, **kwargs)
        self.repassword = repassword

    def save(self):
        data = self.clean()
        new_user = User.objects.create_user(username=data['username'],
                                            password=data['password'])
        return new_user

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        if not 'password' in cleaned_data:
            self.add_error('password', u'Please write your password')
            return cleaned_data
        password = cleaned_data['password']
        repassword = self.repassword
        if password != repassword:
            self.add_error('password', u'Please rewrite your password.')
            return cleaned_data
        if len(password) < 8:
            self.add_error('password', u'The password should be longer than 8 letters.')
            return cleaned_data
        return cleaned_data

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
