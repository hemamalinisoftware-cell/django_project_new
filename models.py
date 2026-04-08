from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Employee(models.Model):
    eid = models.CharField(primary_key=True, max_length=50)
    ename = models.CharField(max_length=100)
    ecity = models.CharField(max_length=100, blank=True, null=True)
    edept = models.CharField(max_length=100, blank=True, null=True)
    esal = models.IntegerField()
    epassword = models.CharField(max_length=256)
    erole = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    
    # Use JSONField instead of ArrayField for SQLite
    education = models.JSONField(blank=True, default=list)
    skills = models.JSONField(blank=True, default=list)

    def set_password(self, raw_password):
        self.epassword = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.epassword)
    
    def __str__(self):
        return self.ename