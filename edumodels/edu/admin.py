from django.contrib import admin
from .models import EduModel
# from users.models import User


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('email',)
#     search_fields = ('email',)

admin.site.register(EduModel)
