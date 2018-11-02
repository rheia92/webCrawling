from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        fields = ('searchTag')
#https://medium.com/@peteryun/python-django%EB%A1%9C-%EC%9B%B9-%EC%84%9C%EB%B9%84%EC%8A%A4-%EA%B0%9C%EB%B0%9C%ED%95%98%EA%B8%B0-11-form%EA%B3%BC-post-%EC%B2%98%EB%A6%AC-320959cb524c