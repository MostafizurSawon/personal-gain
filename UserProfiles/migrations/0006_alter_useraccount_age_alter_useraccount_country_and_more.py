# Generated by Django 5.1 on 2024-09-24 14:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfiles', '0005_useraccount_country_alter_useraccount_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='country',
            field=models.CharField(blank=True, choices=[('BD', 'Bangladesh'), ('Other', 'Other')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='image',
            field=models.URLField(blank=True, default='https://img.freepik.com/premium-photo/poster-anime-character-with-fiery-background_943629-32000.jpg', null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='type',
            field=models.CharField(blank=True, choices=[('Super', 'Super'), ('Regular', 'Regular'), ('Below Average', 'Below Average')], default='Regular', max_length=20),
        ),
        migrations.CreateModel(
            name='UserSocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('x', models.URLField(blank=True, null=True)),
                ('portfolio', models.URLField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='social_account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
