from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    

class MinimumRequirement(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='mininum_requirements')

    requirement_type = models.TextField(max_length=100)
    value = models.TextField()

    def __str__(self):
        return f"{self.requirement_type} for {self.country.name}"
    

class TopUniversityStat(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='top_university_stats')

    topuniversityreq = models.CharField(max_length=100)
    top_value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.topuniversityreq} for {self.country.name}"
    

class PopularUniversity(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='popular_universities')
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.name
    
    
    