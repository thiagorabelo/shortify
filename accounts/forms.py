from django.contrib.auth.forms import UserCreationForm as UserCreationFormBase


class UserCreationForm(UserCreationFormBase):
    class Meta(UserCreationFormBase.Meta):
        fields = ("first_name", "last_name", "username", "email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["username"].required = True
        self.fields["email"].required = True
