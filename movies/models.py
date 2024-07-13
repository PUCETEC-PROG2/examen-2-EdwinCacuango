from django.db import models

# Create your models here.
class Movie (models.Model):
    id = models.IntegerField(null = False, unique=True, primary_key=True)
    title = models.CharField(max_length = 120, null = False)
    gender = models.CharField(max_length=30, null = False)
    director_name = models.CharField(null = False, max_length= 30)
    release_year = models.IntegerField(null=False)
    sinopsis = models.TextField(help_text='Ingresa un resumen de la película')
    
    def __str__(self) -> str:
        return super().__str__() 
    
    def get_year(self)->str:
        return self.release_year.year()