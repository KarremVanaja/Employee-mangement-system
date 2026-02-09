from django.db import models

# Employee model represents Employee table in database
class Employee(models.Model):
    name = models.CharField(max_length=100)       # Employee name
    email = models.EmailField(unique=True)        # Unique email ID
    department = models.CharField(max_length=100) # Department name
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # Salary
    joined_date = models.DateField()               # Date of joining

    def __str__(self):
        # Returns readable name in admin panel
        return self.name
