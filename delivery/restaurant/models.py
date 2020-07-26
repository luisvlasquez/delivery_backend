from django.db import models

# Create your models here.

class Restaurant(models.Model):
    """
        Model restaurant 
    """
    name = models.CharField('Nombre del restaurante', max_length=50)
    image = models.ImageField('Imagen del restaurante', upload_to ='Restaurant/')
    address = models.CharField('Direccion', max_length=50)
    phone = models.CharField('Telefono del restaurant', max_length=15)
    qualification = models.FloatField(null=True)



class TypeMenu(models.Model):
    """ 
        Model type menu in restaurant 
    """
    name = models.CharField('Nombre del tipo de menu',max_length=50)  
    restaurant_id = models.OneToOneField(Restaurant, on_delete=models.CASCADE)

class Menu(models.Model):
    name = models.CharField('Nombre del menu',max_length=50)
    type_menu_id = models.ForeignKey(TypeMenu, on_delete=models.CASCADE)
    

class Product(models.Model):
    name = models.CharField('Nombre del producto', max_length=50)
    price = models.DecimalField('Precio',decimal_places=0,max_digits=6)
    image = models.ImageField('Imagen del producto', upload_to='Product/')
    discount =  models.FloatField(null=True)
    description = models.CharField('Descripcion', max_length=50)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)