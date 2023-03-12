from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Email must be filled!'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active = True

        # Untuk field password disimpan di database setelah 
        # dilakukan proses enkripsi (metode enkripsi bebas) 
        user.set_password(password)
        user.save(using=self.db)
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_deleted', False)
        return self._create_user(email, password, **extra_fields)



class User(AbstractBaseUser):
    '''
    Field user: email, password, first_name, last_name, sex, 
    date_of_birth, address (untuk last_name dan address bersifat opsional)
        
    Semua user tidak memiliki role yang berbeda-beda 
    (tidak ada superuser, admin dsb)
    
    Field yang digunakan untuk login adalah email dan password
    '''
    class SexChoices(models.TextChoices):
        MAN = 'L', _('Laki-Laki')
        WOMAN = 'P', _('Perempuan')
        OTHERS = '-', _('Lainnya')

    email = models.EmailField(unique=True)
    # password field already provided by abstract base user

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    address = models.TextField(max_length=100, null=True)
    sex = models.CharField(max_length=20, choices=SexChoices.choices)
    date_of_birth = models.DateField()

    is_deleted = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'