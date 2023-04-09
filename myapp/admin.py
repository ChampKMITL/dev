from django.contrib import admin

#เอา model person มาให้ admin 
from myapp.models import Person
# Register your models here.

#ให้ admin จัดการ site Person 
admin.site.register(Person)