# Generated by Django 4.2.11 on 2024-04-12 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communiche', '0019_auto_20240412_0839'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityTemplates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community', to='communiche.community')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='template', to='communiche.template')),
            ],
        ),
    ]