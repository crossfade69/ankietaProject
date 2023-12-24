from django.db import models


class Poll(models.Model):
    is_active = models.BooleanField(default=False)
    access_code = models.TextField(max_length=255, blank=True, null=True)

    option_a = models.CharField(max_length=30, default='')
    option_b = models.CharField(max_length=30, default='')
    option_c = models.CharField(max_length=30, default='')
    option_d = models.CharField(max_length=30, default='')

    option_a_count = models.IntegerField(default=0, null=True)
    option_b_count = models.IntegerField(default=0, null=True)
    option_c_count = models.IntegerField(default=0, null=True)
    option_d_count = models.IntegerField(default=0, null=True)
