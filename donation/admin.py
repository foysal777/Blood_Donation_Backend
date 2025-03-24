from django.contrib import admin
from .models import Donor

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'blood_group', 'phone', 'donation_place', 'date')  # ✅ `id` যুক্ত করা হলো
    search_fields = ('name', 'blood_group', 'phone')  
    list_filter = ('blood_group', 'date')  
