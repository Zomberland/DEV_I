from django.contrib import admin
from relacionamentos.models import Person
from relacionamentos.models import Article
from relacionamentos.models import Reporter

# Register your models here.
admin.site.register(Person)
admin.site.register(Article)
admin.site.register(Reporter)
