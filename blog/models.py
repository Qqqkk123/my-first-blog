from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    # def表明这是一个函数或者方法 ,这里是方法
    def publish(self):
        self.published_date =timezone.now()
        self.save()

    # 当你在str的两端使用两个下划线字符（_）的时候务必三思而后行。 这是Python编程里面的一种常见的约定写法，有时我们也叫这个做"dunder"("double-underscore"的缩写)。
    def __str__(self):
        return self.title