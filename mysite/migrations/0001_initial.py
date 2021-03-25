# Generated by Django 3.1.2 on 2021-03-18 20:22

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('blog_filter', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('blog_img', models.ImageField(upload_to='images/blog')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(default=' ')),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 3, 18, 20, 22, 16, 151620, tzinfo=utc))),
                ('resources', models.CharField(blank=True, max_length=100, verbose_name='Event Resources')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default=' ')),
                ('image', models.ImageField(upload_to='images/gallery')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('roll_number', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('member_name', models.CharField(max_length=25)),
                ('post', models.CharField(blank=True, help_text='Enter for past postholders also. ex, <batch> Convener for a past batch convener', max_length=50)),
                ('insta', models.URLField(blank=True, verbose_name='Instagram profile URL')),
                ('email', models.EmailField(default=' ', max_length=50)),
                ('batch', models.CharField(help_text='passing year', max_length=4, verbose_name='Batch')),
                ('curr_core', models.BooleanField(default=False, help_text='Is this member current core member?')),
                ('testimonial', models.TextField(blank=True, default=' ')),
                ('member_img', models.ImageField(upload_to='images/members')),
                ('active', models.BooleanField(default=True, verbose_name='member status')),
            ],
            options={
                'ordering': ['-batch', '-member_name'],
            },
        ),
        migrations.CreateModel(
            name='Udaan_event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_description', models.TextField()),
                ('event_img', models.ImageField(upload_to='images/udaan/events')),
            ],
        ),
        migrations.CreateModel(
            name='Udaan_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='images/udaan/carousel')),
                ('alt_text', models.CharField(max_length=50)),
                ('display_on_caurosel', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Udaan_static',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_description', models.TextField()),
                ('date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/event')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_posts', to='mysite.event')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30, verbose_name='author')),
                ('body', models.TextField(verbose_name='Post Comment')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='mysite.blog')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['-created_on'],
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='mysite.member'),
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_image', models.ImageField(upload_to='images/art')),
                ('title', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('art_type', models.CharField(choices=[('Sketches', 'Sketches'), ('Doodles', 'Doodles'), ('Anime', 'Anime'), ('Abstract', 'Abstract'), ('Portrait', 'Portrait'), ('Nature', 'Nature'), ('Digital', 'Digital'), ('Other', 'Other')], max_length=20, verbose_name='Type')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='art_posts', to='mysite.member')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
