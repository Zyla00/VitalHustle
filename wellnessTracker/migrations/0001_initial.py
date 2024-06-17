# Generated by Django 4.2.13 on 2024-05-29 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scale', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], help_text='How user felt today')),
                ('emotions', multiselectfield.db.fields.MultiSelectField(choices=[('happy', 'Happy'), ('sad', 'Sad'), ('angry', 'Angry'), ('excited', 'Excited'), ('nervous', 'Nervous'), ('scared', 'Scared'), ('relaxed', 'Relaxed'), ('bored', 'Bored'), ('content', 'Content'), ('curious', 'Curious'), ('anxious', 'Anxious'), ('confused', 'Confused'), ('surprised', 'Surprised'), ('grateful', 'Grateful'), ('frustrated', 'Frustrated'), ('jealous', 'Jealous'), ('lonely', 'Lonely'), ('proud', 'Proud'), ('ashamed', 'Ashamed'), ('guilty', 'Guilty'), ('embarrassed', 'Embarrassed'), ('disappointed', 'Disappointed'), ('inspired', 'Inspired'), ('amused', 'Amused'), ('sympathetic', 'Sympathetic'), ('thoughtful', 'Thoughtful'), ('energetic', 'Energetic'), ('overwhelmed', 'Overwhelmed'), ('hopeful', 'Hopeful')], help_text='Which emotions did user felt', max_length=100)),
                ('note', models.TextField(help_text='Custom user note')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Time when the interface was last updated')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Time when the interface was last updated')),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wellnessTracker.mood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]