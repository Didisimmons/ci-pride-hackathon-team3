# Generated by Django 3.2 on 2022-06-18 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0006_alter_donations_charities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='charities',
            field=models.CharField(choices=[('CW', 'Consent Workshop'), ('OI', 'Outright International'), ('GG', 'Global Giving'), ('MR', 'Micro Rianbow')], max_length=2),
        ),
    ]