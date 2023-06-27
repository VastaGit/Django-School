from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, phone_number,password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not phone_number:
            raise ValueError('The given phone_number must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number,password, **extra_fields)

    def create_superuser(self, phone_number,password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number,password, **extra_fields)

class Teacher(AbstractUser):
    username = None
    email = None
    phone_number = models.CharField(max_length=20, unique=True)
    subject_name = models.CharField(max_length=100)
    teaches = models.ManyToManyField('Class', through='Teaches')
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS=[]

    objects = CustomUserManager()
class Student(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    photo = models.ImageField(upload_to='student_photos', blank=True, null=True)
    studies = models.ManyToManyField('Class', through='Studies')

class Class(models.Model):
    name = models.IntegerField()

class Teaches(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teachers')
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

class Studies(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students')
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

class School(models.Model):
    title = models.CharField(max_length=150)
    classes = models.IntegerField(default=0)
