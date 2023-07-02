# Generated by Django 4.2.2 on 2023-06-29 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_pastry_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pastry',
            name='ingredients',
            field=models.ManyToManyField(to='product.ingredients'),
        ),
    ]
