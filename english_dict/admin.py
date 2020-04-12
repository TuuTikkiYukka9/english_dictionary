from django.contrib import admin
from english_dict import models
# Register your models here.

admin.site.register(models.Word)
admin.site.register(models.PartProperty)
admin.site.register(models.WordPartProperty)
admin.site.register(models.IrregularVerb)
