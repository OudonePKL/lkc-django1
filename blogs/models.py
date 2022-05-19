
from django.db import models

# Create your models here.

# For update background image
class BackGImage(models.Model):
    imageBG = models.ImageField(upload_to = "imageBG", blank = True)

#For information of techers first line.
class Teachers1(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    image = models.ImageField(upload_to = "teacherImages1", blank = True)

    def __str__(self):
        return self.firstName + ", " + self.lastName

#For information of techers second line.
class Teachers2(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    image = models.ImageField(upload_to = "teacherImages2", blank = True)

    def __str__(self):
        return self.firstName + ", " + self.lastName

# For LKC's informations
class LKCDatas(models.Model):
    imageLogo = models.ImageField(upload_to = "lkcLogo", blank = True)
    name = models.TextField(max_length=255)
    title1 = models.TextField(max_length=255)
    title2 = models.TextField(max_length=255)
    phoneNumber = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    
# For about us's informations
class AboutUs(models.Model):
    imageAboutUs = models.ImageField(upload_to = "aboutUs", blank = True)
    title = models.TextField(max_length=255)
    desc = models.TextField(max_length=599)

    def __str__(self):
        return self.title

# For about LKC's activity
class LKCActivity(models.Model):
    imageAboutUs = models.ImageField(upload_to = "aboutUs", blank = True)