from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        'email', 'company_name', 'business_type', 'position_type',
        'phone_number', 'account_type', 'is_provider', 'is_distributor', 'is_active'
    )

    list_filter = (
        'is_active', 'is_staff', 'is_superuser',
        'business_type', 'position_type', 'account_type',
        'is_provider', 'is_distributor'
    )

    search_fields = (
        'email', 'company_name', 'contact_person',
        'phone_number', 'registration_number', 'tax_id'
    )

    ordering = ('-created_at',)

    fieldsets = (
        ('Login Info', {'fields': ('email', 'password')}),
        
        ('Business Info', {
            'fields': (
                'company_name', 'business_type', 'registration_number', 'tax_id',
                'contact_person', 'position_type', 'account_type'
            )
        }),

        ('Contact Info', {
            'fields': (
                'address', 'phone_number', 'alternative_phone', 'website'
            )
        }),

        ('Services & Notes', {
            'fields': ('services', 'notes')
        }),

        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'is_provider', 'is_distributor',
                'groups', 'user_permissions'
            )
        }),

        ('Important Dates', {
            'fields': ('last_login', 'created_at', 'updated_at')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2',
                'company_name', 'business_type', 'position_type', 'account_type',
                'is_active', 'is_staff', 'is_provider', 'is_distributor'
            )
        }),
    )

    readonly_fields = ('created_at', 'updated_at')
    
