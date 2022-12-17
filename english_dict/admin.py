from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from english_dict import models
import csv
# Register your models here.

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class PartPropertyAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('import-csv/', self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]

            file = csv_file.read().decode('utf-8', errors='ignore').splitlines()
            reader = csv.reader(file, delimiter=';')

            for row in reader:
                created = models.PartProperty.objects.update_or_create(
                    prop_id = row[0],
                    name = row[1],
                    description = row[2],
                )
                
        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_form.html", data)

    

admin.site.register(models.Word)
admin.site.register(models.WordPartProperty)
admin.site.register(models.IrregularVerb)
admin.site.register(models.WordStatuses)
admin.site.register(models.WordsWordStatuses)
admin.site.register(models.PartProperty, PartPropertyAdmin)
