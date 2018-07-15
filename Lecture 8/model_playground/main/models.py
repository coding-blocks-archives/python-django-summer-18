from django.db import models
from django.core.validators import EmailValidator, MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify

# Create your models here.

def upload_to_func(instance, actual_filename):
	return 'dp/%Y/' + str(instance.name) + '.' + actual_filename.split('.')[-1]

class Person(models.Model):
	name = models.CharField(max_length = 100)
	age = models.IntegerField(blank = True, null = True, validators=[MaxValueValidator(150), MinValueValidator(0)])
	email = models.CharField(max_length = 256, validators = [EmailValidator], null = True)

	GENDERS = (
		('F', 'Female'),
		('M', 'Male')
	)

	slug = models.SlugField(blank = True, null = True)

	gender = models.CharField(max_length = 1, choices = GENDERS)

	attachment = models.FileField(blank = True, null = True)

	display_picture = models.ImageField(upload_to = upload_to_func,null = True)

	def save(self, *args, **kwargs):
		if self.slug == "" or not self.slug:
			self.slug = slugify(self.name)
		return super(Person, self).save(*args, **kwargs)


	def __str__(self):
		return self.name

class Student(models.Model):
	roll = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 100)
