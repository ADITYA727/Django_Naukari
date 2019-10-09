# Generated by Django 2.2.5 on 2019-10-01 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20191001_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.CharField(choices=[('Student or Learning', 'Student or Learning'), ('Junior Developer', 'Junior Developer'), ('Senior Developer', 'Senior Developer'), ('Developer', 'Developer'), ('Manager', 'Manager'), ('Instructor or Teacher', 'Instructor or Teacher'), ('Intern', 'Intern'), ('Bussiness Man', 'Bussiness Man'), ('Digital Marketer', 'Digital Marketer'), ('Data Scientist', 'Data Scientist'), ('Other', 'Other')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=1, max_length=6),
        ),
    ]
