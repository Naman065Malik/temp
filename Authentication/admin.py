from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('username','email', 'password')}),
        ('Profile', {'fields': ("first_name","last_name","Birthday","bio","url","image")}),
        ('Personal Info',{'fields': ("Occupation","School_College","location","Phone","Gender","status","Languages","Programming_Languages","Social_Url")}),
        ('BIG', {'fields': ('About_Me','Education_and_Work', 'Intrest')}),
        ('Permissions', {'fields': ('is_active','is_admin')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)

