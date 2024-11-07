from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birth_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} {self.surname}"



class Profile(models.Model):
    phone_number = models.PositiveIntegerField(default=9, unique=True)

    student = models.OneToOneField('university.Student',
                                   related_name='profile',
                                   on_delete=models.CASCADE)
    

class Adress(models.Model):
    location = models.TextField()

    profile = models.ForeignKey('university.Profile',
                                   related_name='adress',
                                   on_delete=models.CASCADE)


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"
    

class Subject(models.Model):
    title = models.CharField(max_length=255)

    course = models.ManyToManyField('university.Course',
                                    related_name='subject')

    


class Profesor(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    course = models.ManyToManyField('university.Course',
                                    related_name='profesor')

    def __str__(self):
        return f"{self.name} {self.surname}"


class UniversityClass(models.Model):
    course = models.ForeignKey('university.Course',
                               related_name='course_class',
                               on_delete=models.CASCADE)
    
    students = models.ManyToManyField('university.Student',
                                      related_name='university_class')
    
