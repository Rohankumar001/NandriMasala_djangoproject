from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile_regex = RegexValidator(regex=r'^[0-9]{10}$', message='Mobile number must be 10 digits long.')

    mobile = models.CharField(max_length=10, validators=[mobile_regex], null=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    qunatity=models.PositiveIntegerField(default=0)
    reorderlevel=models.PositiveIntegerField(default=5)
    avaliblity=models.BooleanField(default=True)
    description=models.CharField(max_length=40)
    
    
    def check_product_avalibality(self):
        if self.qunatity <=self.reorderlevel:
            if self.avaliblity:
                self.avaliblity=False
                return True
        elif not self.avaliblity:
            self.avaliblity=True
            return True
        return False
    

    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    id = models.BigAutoField(primary_key=True)
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile_regex = RegexValidator(regex=r'^[0-9]{10}$', message='Mobile number must be 10 digits long.')

    mobile = models.CharField(max_length=10, validators=[mobile_regex], null=True)

    # mobile = models.CharField(max_length=10,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)
    
    

class Feedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name


@receiver(post_save, sender=Product)
def udate_data (sender ,instance ,**kwargs):
    if instance.check_product_avalibality():
        instance.save(update_fields=['avaliblity'])


# class cart(models.Model):
#     productid=models.ForeignKey('Product',on_delete=pass)
#     userid=models.ForeignKey('user')
#     quantity=models.PositiveIntegerField()
#     date=models.DateField()

#     def __str__(self):
#         return  self.userid
