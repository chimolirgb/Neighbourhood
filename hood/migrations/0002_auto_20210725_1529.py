# Generated by Django 3.2.5 on 2021-07-25 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('description', models.CharField(default='Neighborhood description', max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='pub_date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=30)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='posts', to='hood.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile', to='hood.profile')),
            ],
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='hoods', to='hood.profile'),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='bsimage/')),
                ('description', models.CharField(max_length=300)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='businesses', to='hood.neighbourhood')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profiles', to='hood.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hood.neighbourhood'),
        ),
    ]
