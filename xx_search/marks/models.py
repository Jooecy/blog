from django.db import models
from django.contrib.auth.models import User

class Marks(models.Model):
    title = models.CharField('标题', max_length=50)
    url = models.URLField('url')
    describe = models.TextField('描述')
    mark_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = '收藏者' )

    def __str__(self):
        return self.title


