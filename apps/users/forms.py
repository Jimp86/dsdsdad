from django.contrib.auth.forms import AuthenticationForm

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widger.attrs['class']='form-control'
        self.fields['username'].widger.attrs['placeholder']='User'
        self.fields['password'].widger.attrs['class'] = 'form-control'
        self.fields['password'].widger.attrs['placeholder'] = 'password'