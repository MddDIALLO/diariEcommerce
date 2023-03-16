from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'joining_date', 'last_login_date', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('joining_date', 'last_login_date')
    ordering = ('-joining_date',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)