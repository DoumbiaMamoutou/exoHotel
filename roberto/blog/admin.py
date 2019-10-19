# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategorieAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'nom', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'status',
        'date_add',
        'date_upd',
    )


class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'status',
        'date_add',
        'date_upd',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'categorie',
        'titre',
        'description',
        'image',
        'image_single',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'categorie',
        'status',
        'date_add',
        'date_upd',
        'id',
        'categorie',
        'titre',
        'description',
        'image',
        'contenu',
        'image_single',
        'status',
        'date_add',
        'date_upd',
    )
    raw_id_fields = ('tag',)


class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'article',
        'nom',
        'image',
        'message',
        'website',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('id', 'email', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'email',
        'status',
        'date_add',
        'date_upd',
    )


class InstagramAdmin(admin.ModelAdmin):

    list_display = ('id', 'image')
    list_filter = ('id', 'image')


class SocialAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'lien', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'lien',
        'status',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Tag, TagAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.Newsletter, NewsletterAdmin)
_register(models.Instagram, InstagramAdmin)
_register(models.Social, SocialAdmin)
