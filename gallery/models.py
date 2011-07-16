from django.db import models
from mezzanine.pages.models import Page
from filebrowser_safe.fields import FileBrowseField

class Gallery(Page):
    notes = models.TextField("Notes")

class GalleryImage(models.Model):
    gallery = models.ForeignKey("Gallery")
    image = FileBrowseField("Image", max_length=200, 
            extensions=['.jpg','.png','.gif'])
    text = models.TextField(blank=True)

    class Admin:
        pass

    def __unicode__(self):
        return u'%s' % self.text


