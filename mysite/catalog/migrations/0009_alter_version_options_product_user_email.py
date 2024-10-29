# Generated by Django 5.1.1 on 2024-10-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ('version_number',)},
        ),
        migrations.AddField(
            model_name='product',
            name='user_email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
