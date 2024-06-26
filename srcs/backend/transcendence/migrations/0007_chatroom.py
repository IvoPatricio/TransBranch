# Generated by Django 4.2.11 on 2024-04-25 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transcendence', '0006_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('was_blocked', models.BooleanField(default=False)),
                ('block_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chat_rooms_blocked', to='transcendence.user')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_rooms_as_user1', to='transcendence.user')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_rooms_as_user2', to='transcendence.user')),
            ],
        ),
    ]
