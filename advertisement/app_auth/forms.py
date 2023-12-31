from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()
class MyUserCreationForm(UserCreationForm):
    def __int__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control form-control-bg"
        self.fields["first_name"].widget.attrs["class"] = "form-control form-control-bg"
        self.fields["last_name"].widget.attrs["class"] = "form-control form-control-bg"
        self.fields["password1"].widget.attrs["class"] = "form-control form-control-bg"
        self.fields["password2"].widget.attrs["class"] = "form-control form-control-bg"


    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]
