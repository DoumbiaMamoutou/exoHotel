from django.db import models
from tinymce import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):
    """Model definition for Categorie."""
    nom = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom
    
class Tag(models.Model):
    """Model definition for Tag."""
    nom = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return self.nom


class Article(models.Model):
    """Model definition for Article."""
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='article_categorie')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='article_tag')
    titre = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/article/image')
    contenu = HTMLField('Content', default="null")
    image_single = models.ImageField(upload_to='blog/article/single')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.titre
    
class Commentaire(models.Model):
    """Model definition for Commentaire."""
    author = models.OneToOneField(User, on_delete=models.CASCADE,related_name='author')
    image = models.ImageField(upload_to='blog/commentaire/user')
    message = models.TextField()
    website = models.URLField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Commentaire."""

        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        """Unicode representation of Commentaire."""
        return self.author.username
    
class Nexsletter(models.Model):
    """Model definition for Nexsletter."""
    email = models.EmailField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Nexsletter."""

        verbose_name = 'Nexsletter'
        verbose_name_plural = 'Nexsletters'
        
class Instagram(models.Model):
    """Model definition for Instagram."""
    image = models.ImageField(upload_to='blog/instagram')
    # TODO: Define fields here

    class Meta:
        """Meta definition for Instagram."""

        verbose_name = 'Instagram'
        verbose_name_plural = 'Instagrams'

    def __str__(self):
        """Unicode representation of Instagram."""
        pass


