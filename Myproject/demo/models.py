from django.db import models

# Create your models here.


class Events(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Location = models.CharField(max_length=300)
    City = models.CharField(max_length=100)
    Occation = models.CharField(max_length=200)
    Event_Style = models.CharField(max_length=200)
    Event_Date = models.DateField()
    Event_Choice = models.CharField(max_length=300)
    Menu_Id = models.IntegerField()
    Created_date = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.First_Name} {self.Last_Name}"


class Menus(models.Model):
    Menu_Name = models.CharField(max_length=100)
    Category = models.CharField(max_length=200)
    Type = models.CharField(max_length=100)
    Time = models.CharField(max_length=100)
    Veg_Nonveg = models.CharField(max_length=200)
    Starters = models.CharField(max_length=4000)
    Main_Menu = models.CharField(max_length=4000)
    Dessert = models.CharField(max_length=4000)
    Created_date = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.Menu_Name} "


class MenuList(models.Model):
    Name = models.CharField(max_length=200)
    Category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Name} - {self.Category}"


class Message(models.Model):
    Date = models.DateField()
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    Liked = models.BooleanField()
    Msg_text = models.CharField(max_length=4000)
    User_id = models.CharField(max_length=100)