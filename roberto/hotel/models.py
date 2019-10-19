from django.db import models

# Create your models here.

class Room(models.Model):
    """Model definition for Room."""
    titre = models.CharField(max_length=50)
    prix = models.IntegerField()
    image = models.ImageField(upload_to='hotel/room')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Room."""

        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        """Unicode representation of Room."""
        return self.titre
    
class ImageInterieur(models.Model):
    """Model definition for ImageInterieur."""
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='imageinterieur')
    image = models.ImageField(upload_to='hotel/interieur')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for ImageInterieur."""

        verbose_name = 'ImageInterieur'
        verbose_name_plural = 'ImageInterieurs'

    def __str__(self):
        """Unicode representation of ImageInterieur."""
        return self.room.titre
    
class Info(models.Model):
    """Model definition for Info."""
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='info')
    titre = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Info."""

        verbose_name = 'Info'
        verbose_name_plural = 'Infos'

    def __str__(self):
        """Unicode representation of Info."""
        return self.titre
    
class RoomService(models.Model):
    """Model definition for RoomService."""
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='service')
    image = models.ImageField(upload_to='hotel/service')
    description = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for RoomService."""

        verbose_name = 'RoomService'
        verbose_name_plural = 'RoomServices'

    def __str__(self):
        """Unicode representation of RoomService."""
        return self.room.titre
    
class Description(models.Model):
    """Model definition for Description."""
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_description')
    texte = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Description."""

        verbose_name = 'Description'
        verbose_name_plural = 'Descriptions'

    def __str__(self):
        """Unicode representation of Description."""
        return self.room.titre
    

class Reservation(models.Model):
    """Model definition for Reservation."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Reservation."""

        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        """Unicode representation of Reservation."""
        pass




