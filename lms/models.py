from django.db import models


class City(models.Model):
    '''City model'''

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class District(models.Model):
    '''District model'''

    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class School(models.Model):
    '''School model'''

    name = models.CharField(max_length=100)
    number = models.IntegerField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Grade(models.Model):
    '''Grade model'''

    number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.number)


class Student(models.Model):
    '''Student model'''

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='students')
    tg_username = models.CharField(max_length=100, unique=True)
    tg_id = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

