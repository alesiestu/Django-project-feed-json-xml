from django.contrib import admin
from conto.models import Bill




class lista(admin.ModelAdmin):
     list_display = ('created_date', 'value' , 'info')
     list_per_page = 25
     actions = None   
     list_display_links = None 
      


admin.site.register(Bill, lista)









# Register your models here.
