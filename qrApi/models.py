from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


# Create your models here.
class images(models.Model):
    URL=models.CharField(max_length=200,blank=True)
    Image=models.ImageField(blank=True, upload_to='images')

    def save(self, *args,**kwargs):
        qr_image=qrcode.make(self.URL)
        qr_offset= Image.new('RGB',(310,310), 'white')
        qr_offset.paste(qr_image)
        files_name =f'{self.URL}-{self.id}qr.png'
        stream = BytesIO()
        qr_offset.save(stream,'PNG')
        self.Image.save(files_name,File(stream),save=False)
        qr_offset.close()
        super().save(*args, **kwargs)



    def __str__(self):
        return self.URL
    