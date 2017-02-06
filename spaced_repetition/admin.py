from django.contrib import admin

from .models import Folder, Deck, Card


class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at', 'updated_at')

admin.site.register(Folder, FolderAdmin)


class DeckAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    'parent_directory',
                    'owner',
                    'created_at',
                    'updated_at'
                    )

admin.site.register(Deck, DeckAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display = (
                    'question',
                    'answer',
                    'deck',
                    'box',
                    'last_studied',
                    'owner',
                    'created_at',
                    'updated_at'
                   )

admin.site.register(Card, CardAdmin)
