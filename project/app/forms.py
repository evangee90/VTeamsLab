from django import forms

class registerform(forms.Form):
    n_ame = forms.CharField(max_length=30)
    e_mail = forms.EmailField(max_length=20)
    m_obile = forms.IntegerField()
    a_ddress = forms.CharField(max_length=50)
    #genders = (('Male' , 'Male'), ('Female','Female'),('Transgender','Transgender'))
    #g_ender = forms.ChoiceField(choices=genders,widget=forms.RadioSelect)
    p_wd=forms.CharField(max_length=20)


class loginform(forms.Form):
    e_mail=forms.EmailField(max_length=20)
    p_wd=forms.CharField(max_length=20)

class updateform(forms.Form):
    p_hoto = forms.ImageField()
    n_ame = forms.CharField(max_length=30)
    m_obile = forms.IntegerField()
    a_ddress = forms.CharField(max_length=50)
