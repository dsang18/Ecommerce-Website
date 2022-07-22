from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    price = models.IntegerField(default=0)
    images = models.ImageField(upload_to="ecommerce_app/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    query = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=5000)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    zipcode = models.CharField(max_length=10)
    amount = models.IntegerField()

    def __str__(self):
        return self.name + str(self.order_id)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0)
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return str(self.order_id)



