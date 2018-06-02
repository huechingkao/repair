# -*- coding: utf8 -*-
from django.db import models

class Content(models.Model):
    CHOICES = [
        (0, '待處理'),
        (1, '處理中'),
        (2, '已處理'),
    ]  
    # 報修主旨
    subject =  models.CharField(max_length=255, verbose_name='報修主旨')
    # 報修內容
    description = models.TextField(verbose_name='報修內容')
    # 報修人
    reporter = models.CharField(max_length=20, verbose_name='報修人')
    # 連絡電話
    phone = models.CharField(max_length=20, verbose_name='連絡電話')
    # 報修日期
    publication_date = models.DateTimeField(auto_now_add=True)
    # 處理人
    handler = models.CharField(max_length=20, verbose_name='處理人')
    # 處理狀況
    status = models.IntegerField(default=0, choices=CHOICES, verbose_name='處理狀況')
    # 處理說明
    comment = models.TextField(verbose_name='處理說明')
    # 處理日期
    handle_date = models.DateTimeField(null=True, blank=True, verbose_name='處理日期')
    # 照片
    picture = models.ImageField(blank=True,null=True, verbose_name='照片')
    picname = models.CharField(max_length=32,null=True,blank=True)    
    
    def __str__(self):
        return self.subject
