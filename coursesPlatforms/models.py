from django.db import models
# What we are building

# Courses:

# Title
# Description
# Thumbnail/Image
# Access:
# Anyone
# Email required
# Purchase required
# User required (n/a)
# Status:
# Published
# Coming Soon
# Draft
# Lessons
# Title
# Description
# Video
# Status: Published, Coming Soon, Draft
# Email verification for short-lived access

# Views:
# Collect user email
# Verify user email
# Activate session
# Models:
# Email
# EmailVerificationToken

class AccessRequirement(models.TextChoices):    #ین یه کلاس کمکیه که با TextChoices ساخته شده و در واقع یه enum (لیست انتخابی) برای وضعیت انتشار دوره است.
    ANY = "any" , "Anyone"
    EMAIL_REQUIRED = "email_required" , "Email_required "

def handle_upload(instance , filename):
        return f"{filename}"

class PublishStatus(models.TextChoices):    #ین یه کلاس کمکیه که با TextChoices ساخته شده و در واقع یه enum (لیست انتخابی) برای وضعیت انتشار دوره است.
    PUBLISHED = "publish" , "Published"
    COMING_SOON = "soon" , "Coming Soon"
    DRAFT = "draft" , "Draft"    
class Course (models.Model):  #معرفی دوره آموزشی
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    access = status = models.CharField(max_length=10 , choices=AccessRequirement.choices,default= AccessRequirement.DRAFT)
    image = models.ImageField(upload_to=handle_upload , blank=True, null=True)
    status = models.CharField(max_length=10 , choices=PublishStatus.choices,default= PublishStatus.DRAFT)
    
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED