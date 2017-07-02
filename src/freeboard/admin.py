from django.contrib import admin
from .models import FreeB, Comment

# Register your models here.
@admin.register(FreeB)
class AuthorAdmin(admin.ModelAdmin):
    pass
