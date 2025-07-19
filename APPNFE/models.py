from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone



class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
         
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    
class Post(models.Model):
    STATUS_CHOICES=(   
    ('P','publish'),
    ('D','draft')
    )
    
    title=models.CharField(max_length=250)
    franceTitle=models.CharField(max_length=250)
    symbol = models.CharField(max_length=10)  # e.g., BTC, ETH
    slug=models.CharField(unique=True,max_length=250)
    des=models.TextField()
    franceDES=models.TextField()
    price = models.PositiveIntegerField()
    francePrice=models.PositiveIntegerField()
    current_price = models.DecimalField(max_digits=20, decimal_places=2)
    volume_24h = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="24h Trading Volume")
    ma_200 = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="200-Day MA")
    support_level = models.DecimalField(max_digits=20, decimal_places=2)
    resistance_level = models.DecimalField(max_digits=20, decimal_places=2)
    price_change_24h = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="24h Price Change (%)")
    img=models.ImageField(upload_to='image/')
    chart=models.URLField()
    star = models.BooleanField(default=False)
    publish=models.DateTimeField(default=timezone.now)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES)

    def __str__(self):
        return self.title


    
    

        
class  Like(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"