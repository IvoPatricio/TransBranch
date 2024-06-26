# Generated by Django 4.2.11 on 2024-04-25 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transcendence', '0005_tournamentuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('was_accepted', models.BooleanField(default=False)),
                ('was_canceled', models.BooleanField(default=False)),
                ('was_refused', models.BooleanField(default=False)),
                ('has_finished', models.BooleanField(default=False)),
                ('score', models.IntegerField(default=0)),
                ('tournament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches', to='transcendence.tournament')),
                ('user1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches_as_user1', to='transcendence.user')),
                ('user2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches_as_user2', to='transcendence.user')),
            ],
        ),
    ]
