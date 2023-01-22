from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# from Post.models import Post

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=25, null=True,blank=True)
    last_name = models.CharField(max_length=25,null=True,blank=True)
    bio = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="profile_picture", null=True, default="default.png")
    # favourite = models.ManyToManyField(Post, blank=True)
    

    # New
    About_Me = models.TextField(max_length=10000, null=True, blank=True)
    Education_and_Work = models.TextField(max_length=10000, null=True, blank=True)
    Intrest = models.TextField(max_length=10000, null=True, blank=True)

    # Personal Info
    Occupation =  models.CharField(max_length=200, null=True, blank=True)
    School_College =  models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    Birthday = models.DateField(null=True,blank=True)
    Phone = models.IntegerField(default=0)

    Gender = (
        ('X', 'Not Necessary'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        
    )
    
    Gender = models.CharField(max_length=10, choices = Gender, default = 'X')
    Relation = (
        ('S', 'Single'),
        ('A', 'Married'),
        ('R', 'In A RelationShip'),
        ('N', 'Not Necessary'),
        
    )
    status = models.CharField(max_length=30, choices = Relation, default = 'N')
    Social_Url = models.URLField(max_length=200, null=True, blank=True)
    Personal_Site_or_PortfolioLink = models.URLField(max_length=200, null=True, blank=True)
    Languages = models.CharField(max_length=100, null=True, blank=True)
    Programming_Languages = models.CharField(max_length=100, null=True, blank=True)

    # Permissions
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

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

