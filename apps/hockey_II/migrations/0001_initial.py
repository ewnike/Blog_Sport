# Generated by Django 2.2 on 2020-01-19 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BetSlip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_line_away', models.IntegerField()),
                ('money_line_home', models.IntegerField()),
                ('point_spread_away_line', models.IntegerField()),
                ('point_spread_home_line', models.IntegerField()),
                ('over_line', models.IntegerField()),
                ('under_line', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('remaining_amnt', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleNHL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id_key', models.CharField(max_length=255)),
                ('away_rot', models.IntegerField()),
                ('away_team', models.CharField(max_length=25)),
                ('home_rot', models.IntegerField()),
                ('home_team', models.CharField(max_length=25)),
                ('match_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='OddsNHL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_id', models.CharField(max_length=255)),
                ('money_line_away', models.IntegerField()),
                ('money_line_home', models.IntegerField()),
                ('odd_type', models.CharField(max_length=25)),
                ('over_line', models.IntegerField()),
                ('total_number', models.DecimalField(decimal_places=3, max_digits=5)),
                ('under_line', models.IntegerField()),
                ('point_spread_away', models.DecimalField(decimal_places=3, max_digits=5)),
                ('point_spread_home', models.DecimalField(decimal_places=3, max_digits=5)),
                ('point_spread_away_line', models.IntegerField()),
                ('point_spread_home_line', models.IntegerField()),
                ('draw_line', models.IntegerField()),
                ('site_id', models.IntegerField()),
                ('last_updated', models.DateTimeField()),
                ('schedule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='odds', to='hockey_II.ScheduleNHL')),
            ],
        ),
        migrations.CreateModel(
            name='BetTaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_line_away', models.IntegerField()),
                ('money_line_home', models.IntegerField()),
                ('point_spread_away_line', models.IntegerField()),
                ('point_spread_home_line', models.IntegerField()),
                ('over_line', models.IntegerField()),
                ('under_line', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('betslip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='betslip_bettakers', to='hockey_II.BetSlip')),
                ('event_odds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bettaker_event_odds', to='hockey_II.OddsNHL')),
                ('schedule_event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bettaker_event', to='hockey_II.ScheduleNHL')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bettakers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='betslip',
            name='event_odds',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_odds', to='hockey_II.OddsNHL'),
        ),
        migrations.AddField(
            model_name='betslip',
            name='schedule_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='hockey_II.ScheduleNHL'),
        ),
        migrations.AddField(
            model_name='betslip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='betslips', to=settings.AUTH_USER_MODEL),
        ),
    ]
