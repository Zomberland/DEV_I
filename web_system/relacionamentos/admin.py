from django.contrib import admin
from relacionamentos.models import Person
from relacionamentos.models import Article
from relacionamentos.models import Reporter
from relacionamentos.models import Paper
from relacionamentos.models import Publication
from relacionamentos.models import Magazine

# Register your models here.
admin.site.register(Person)
admin.site.register(Article)
admin.site.register(Reporter)
admin.site.register(Paper)
admin.site.register(Publication)
admin.site.register(Magazine)
