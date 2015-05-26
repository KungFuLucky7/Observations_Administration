from django.contrib import admin
from observations.models import Observation

class ObservationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['species']}),
        ('Common Name',      {'fields': ['common_name']}),
        ('Author', 	     {'fields': ['author']}),
        ('Published Date',   {'fields': ['pub_date']}),
        ('Observation Type', {'fields': ['observation_type']}),
        ('Location',         {'fields': ['location']}),
        ('GPS',              {'fields': ['gps']}),
        ('Image',            {'fields': ['image']}),
        ('Description',      {'fields': ['description'], 'classes': ['grp-collapse grp-open']}),
        ('Revision Notes',   {'fields': ['revision_notes'], 'classes': ['grp-collapse grp-closed']}),
        ('Edited by',        {'fields': ['edited_by']}),
        ('Edited on',        {'fields': ['edited_on']}),
        ('Curated',          {'fields': ['curated']}),
    ]
    readonly_fields=('pub_date', 'edited_by', 'edited_on')
    list_display = ('species', 'curated', 'edited_by', 'edited_on', 'author', 'common_name', 'location', 'pub_date', 'was_published_recently')
    list_filter = ('curated', 'pub_date', 'edited_on')
    search_fields = ('species', 'common_name', 'location', 'author')
    date_hierarchy = 'pub_date'
    ordering = ['species']

    def save_model(self, request, obj, form, change):
        obj.edited_by = request.user
        obj.save()

admin.site.register(Observation, ObservationAdmin)
