# Generated by Django 4.0.7 on 2022-08-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopicQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_id', models.CharField(max_length=75, verbose_name='ID da instância')),
                ('filter_id', models.CharField(max_length=75, verbose_name='ID do filtro')),
                ('topic_id', models.CharField(max_length=75, verbose_name='ID do tópico')),
                ('query_url', models.URLField(verbose_name='URL para estratégia de busca')),
            ],
            options={
                'verbose_name': 'Tópico / Query',
                'verbose_name_plural': 'Tópicos / Queries',
            },
        ),
    ]
