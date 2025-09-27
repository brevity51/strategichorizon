from django.contrib import admin
from .models import Subscriber

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelModel):
    list_display = ('email', 'first_name', 'last_name', 'company', 'subscribed_at')
    list_filter = ('subscribed_at',)
    search_fields = ('email', 'first_name', 'last_name', 'company')
    ordering = ('-subscribed_at',)