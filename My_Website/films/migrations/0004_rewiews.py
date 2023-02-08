# Generated by Django 4.1.2 on 2022-10-29 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_direction_genre_alter_film_options_film_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rewiews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text_rewiews', models.TextField(max_length=1500, verbose_name='Текст фильма')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]