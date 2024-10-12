from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    # Check email
    def email_validator(self,email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('Please provide a valid email address.'))
        
    # Create User
    def create_user(self,username,first_name,last_name,email,password,**extra_fields):

        # Checks on user fields
        if not username:
            raise ValueError(_('Please provide a username.'))
        
        if not first_name:
            raise ValueError(_('Please provide a first name.'))
        
        if not last_name:
            raise ValueError(_('Please provide a last name.'))
        
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('Base User Account: Please provide a valid email address'))
        
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user
    

    # Create Super User
    def create_superuser(self,username,first_name,last_name,email,password,**extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff=True."))
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is_superuser=True."))
        
        if not password:
            raise ValueError(_("Superusers must have a password."))
        
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('Admin Account: Please provide a valid email address'))
        
        user = self.create_user(username, first_name, last_name, email, password,**extra_fields)
        user.save(using=self._db)
        return user
        




        

