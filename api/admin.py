from django.contrib import admin
from api.models import Profile


class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'fullname', 'invite', 'type_account', 'phone', 'city', 'avatar', 'updated_by']


admin.site.register(Profile, ProfileAdmin)
