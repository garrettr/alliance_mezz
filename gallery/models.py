from django.db import models
from mezzanine.pages.models import Page

# All members of Page will be inherited by Gallery
class Gallery(Page):
    notes = models.TextField("Notes")

class GalleryImage(models.Model):
    gallery = models.ForeignKey("Gallery")
    image = models.ImageField(upload_to="galleries")
