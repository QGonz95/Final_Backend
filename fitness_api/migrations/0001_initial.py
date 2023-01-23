# Generated by Django 4.1.4 on 2023-01-23 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='fitness_api.user')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('experience', models.IntegerField(blank=True, null=True)),
                ('injuries', models.TextField(blank=True, null=True)),
                ('progress_img', models.ImageField(upload_to='fitness_api/files/progress')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='your_goal', to='fitness_api.user')),
            ],
        ),
    ]
