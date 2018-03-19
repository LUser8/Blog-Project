from django.urls import reverse
from django.db import models
# from djongo import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone


class PostManager(models.Manager):
    def active(self, *args, **kwargs):  # all
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


def upload_location(instance, filename):
    print(instance)
    return "{}/{}".format(instance, filename)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=120, blank=False, null=True)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    images = models.ImageField(upload_to=upload_location,
                               null=True,
                               blank=True,
                               width_field='width_field',
                               height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = PostManager()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-timestamp', '-updated']


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (instance.title, qs.first().id)
        return create_slug(instance, new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    instance.username = instance.user.username


pre_save.connect(pre_save_post_receiver, sender=Post)

