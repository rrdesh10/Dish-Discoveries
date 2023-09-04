from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Item(models.Model):
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=500)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=700, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8GV0f6prb-DPesR3lFwG2UsJh94yNz7ijRQ&usqp=CAU")
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.item_name
    
    def get_absolute_url(self):
        return reverse('food:detail', kwargs={'pk': self.pk})
