# Generated by Django 4.2.4 on 2023-09-02 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.google.com/imgres?imgurl=https%3A%2F%2Fkwalityindiancuisine.com%2Fassets%2Fimg%2Ffood_images%2Fplaceholder.png&tbnid=wNI3LelixCTbuM&vet=12ahUKEwiZtI7OvIuBAxU3yaACHUonDjMQMygXegUIARCMAQ..i&imgrefurl=https%3A%2F%2Fkwalityindiancuisine.com%2Fshop%3Fcat%3D100&docid=Zx7PS2zVC-jOaM&w=1031&h=580&q=food%20placeholder%20image&ved=2ahUKEwiZtI7OvIuBAxU3yaACHUonDjMQMygXegUIARCMAQ', max_length=700),
        ),
    ]