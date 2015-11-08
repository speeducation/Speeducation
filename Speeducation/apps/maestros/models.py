from django.db import models
#from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from .choices import choices

"""class MyUserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_super_user):
        if not email:
            raise ValueError('Usuarios deben tener email')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            is_active = True,
            is_staff = is_staff,
            is_super_user = is_super_user,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(self, username, email, password = None):
        return self._create_user(username, email, password, False, False)

    def create_superuser(self, username, email, password):
        return self._create_user(username, email, password, True, True)"""

# Create your models here.
class Maestro(models.Model):
    username = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    sexo = models.CharField(max_length=50, choices=choices.GENDER_CHOICES, default=choices.GENDER_CHOICES)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    #objects = MyUserManager()

    #is_active = models.BooleanField(default=True)
    #is_staff = models.BooleanField(default=True)

    #USERNAME_FIELD  = 'username'
    #REQUIRED_FIELD  = ['email']

    """def get_full_name(self):
        fullname = self.nombre + " " + self.apellidos
        return self.fullname

    def get_short_name(self):
        return self.username"""

    def __str__(self):
        return self.username