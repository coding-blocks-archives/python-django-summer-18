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

class Subject(models.Model):
	name = models.CharField(max_length = 100)
	HOD = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Student(models.Model):
	roll = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 100)
	subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null = True)
	marks = models.IntegerField(null = True)

	def __str__(self):
		return self.name



class Topping(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return self.name

class Pizza(models.Model):
	name = models.CharField(max_length = 100)
	price = models.IntegerField(validators=[MinValueValidator(200), MaxValueValidator(2000)])
	toppings = models.ManyToManyField(Topping)
	def __str__(self):
		return self.name



class Member(models.Model):
	name = models.CharField(max_length = 100)
	groups = models.ManyToManyField('Group', through = 'GroupMember')
	def __str__(self):
		return self.name

class Group(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return self.name


class GroupMember(models.Model):
	# Required Fields
	member = models.ForeignKey(Member, on_delete = models.CASCADE)
	group = models.ForeignKey(Group, on_delete = models.CASCADE)

	# Attribute Fields
	role = models.CharField(max_length = 100)
	
	def __str__(self):
		return "{} is in {} group with {} role".format(self.member.name, self.group.name, self.role)
	

class Publisher(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Book(models.Model):
	name = models.CharField(max_length = 100)
	rating = models.IntegerField(default = 3, validators=[MinValueValidator(0), MaxValueValidator(5)])
	# publisher = models.ForeignKey(Publisher, on_delete = models.CASCADE)
	
	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)