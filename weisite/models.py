from django.db import models

# Create your models here.
class weixin_article(models.Model):
    post_user = models.CharField(max_length=100)
    post_link = models.CharField(max_length=100)
    post_date = models.CharField(max_length=100)
    
    def __unicode():
        return u'%s' % (code)