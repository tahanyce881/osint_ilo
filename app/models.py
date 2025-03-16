from django.db import models

class Param(models.Model):
    title = models.CharField(max_length=500,null=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        verbose_name= 'Param'
        verbose_name_plural= 'Params'

    def __str__(self):
        return self.title

class SubParam(models.Model):
    title = models.CharField(max_length=500,null=True)
    description = models.TextField(blank=True)
    param = models.ForeignKey(Param, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        verbose_name= 'Sub Param'
        verbose_name_plural= 'Sub Params'

    def __str__(self):
        return self.title

class ServerParam(models.Model):
    title = models.CharField(max_length=500,null=True)
    description = models.TextField(blank=True)
    subparam = models.ForeignKey(SubParam, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        verbose_name= 'Server Param'
        verbose_name_plural= 'Server Params'

    def __str__(self):
        return self.title