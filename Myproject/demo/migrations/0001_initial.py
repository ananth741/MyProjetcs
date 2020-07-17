# Generated by Django 3.0.8 on 2020-07-14 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=15)),
                ('Location', models.CharField(max_length=300)),
                ('City', models.CharField(max_length=100)),
                ('Occation', models.CharField(max_length=200)),
                ('Event_Style', models.CharField(max_length=200)),
                ('Event_Date', models.DateField()),
                ('Event_Choice', models.CharField(max_length=300)),
                ('Menu_Id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Menu_Name', models.CharField(max_length=100)),
                ('Category', models.CharField(max_length=200)),
                ('Type', models.CharField(max_length=100)),
                ('Time', models.CharField(max_length=100)),
                ('Veg_Nonveg', models.CharField(max_length=200)),
                ('Starters', models.CharField(max_length=4000)),
                ('Main_Menu', models.CharField(max_length=4000)),
                ('Dessert', models.CharField(max_length=4000)),
            ],
        ),
    ]
