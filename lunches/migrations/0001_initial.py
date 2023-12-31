# Generated by Django 4.2.5 on 2023-09-22 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('redeemed', models.BooleanField(default=False)),
                ('note', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('org_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization', to='organization.organization')),
            ],
            options={
                'verbose_name_plural': 'Lunches',
            },
        ),
    ]
