# Generated by Django 4.1.7 on 2023-03-15 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import share.models
import taggit_autosuggest.managers
import uuid
import vu.abstract.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pygment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('code', models.CharField(max_length=16, verbose_name='Code')),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
            ],
            options={
                'verbose_name': 'Pygment type',
                'verbose_name_plural': 'Pygment types',
            },
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='Slug')),
                ('url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Url')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('password', models.CharField(blank=True, db_index=True, max_length=64)),
                ('disabled', models.BooleanField(db_index=True, default=False)),
                ('hidden', models.BooleanField(db_index=True, default=False)),
                ('personal', models.BooleanField(default=False, verbose_name='Personal')),
                ('json', models.JSONField(default=share.models.default_json, verbose_name='Json content')),
                ('expired_on', models.DateField(blank=True, null=True, verbose_name='Expired on')),
                ('view_count', models.IntegerField(default=0, editable=False)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_updated', models.DateTimeField(auto_now=True)),
                ('time_delete', models.DateField(blank=True, default=None, null=True)),
                ('tags', taggit_autosuggest.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='share.pygment', verbose_name='Pygment type')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', vu.abstract.models.UniqueFileField(upload_to='share/%Y/%m/%d', verbose_name='File')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('mime', models.CharField(blank=True, max_length=128, null=True)),
                ('json', models.JSONField(default=share.models.default_json, verbose_name='Json content')),
                ('processed', models.BooleanField(default=False, verbose_name='Processed')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comments')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('share', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_share', to='share.share')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
