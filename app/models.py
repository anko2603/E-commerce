from django.db import models

# Create your models here.
from django.db import models
# Create your models here.

CATEGORY_CHOICES=(
    ('FE','Fire Extinguishers'),
    ('FA','Fire Alarms system'),
    ('DR','Detector'),
    ('SN','Sprinkler'),  
    ('HY','Hydrant'),
    ('BN','Branch-Nozzles'),
    ('WM','Watermist/Cafe System'),   
 )

class Product(models.Model):
    title = models.CharField(max_length=1000)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    descripition = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

    
    
