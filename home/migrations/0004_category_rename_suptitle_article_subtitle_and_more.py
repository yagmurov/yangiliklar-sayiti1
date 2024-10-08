# Generated by Django 4.2.15 on 2024-08-14 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_article_slug_article_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='article',
            old_name='suptitle',
            new_name='subtitle',
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['title', 'subtitle'], name='home_articl_title_2b6ae8_idx'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='home.category'),
        ),
    ]
