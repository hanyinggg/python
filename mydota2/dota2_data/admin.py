from django.contrib import admin
from .models import Heros, Skills, Items

class SkillInline(admin.TabularInline):
    model = Skills
    extra = 1

class HeroAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,       {'fields': ['name']}),
        ('img', {'fields':['img']}),
        ('Attr', {'fields': ['attr']}),
        ('Background', {'fields':['background'],}),
        ('Talent', {'fields':['talent']})]
    inlines = [SkillInline]
    search_fields = ['name']


admin.site.register(Heros, HeroAdmin)

admin.site.register(Skills)
admin.site.register(Items)



# Register your models here.
