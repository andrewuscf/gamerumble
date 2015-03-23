# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('explorer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConnectionTicket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_sessionid', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FantasyContract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round', models.PositiveIntegerField(null=True, blank=True)),
                ('pick', models.PositiveIntegerField(null=True, blank=True)),
                ('position', models.CharField(max_length=3, choices=[(b'Top', b'Top'), (b'Jun', b'Jungle'), (b'Mid', b'Mid'), (b'Adc', b'ADC'), (b'Sup', b'Support'), (b'Sub', b'Sub')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FantasyMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('games', models.ManyToManyField(to='explorer.RawGameData', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FantasyTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'The Bedazzling Defaults', max_length=32)),
                ('wins', models.PositiveIntegerField(default=0)),
                ('losses', models.PositiveIntegerField(default=0)),
                ('ties', models.PositiveIntegerField(default=0)),
                ('draft_pick', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('locked', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('public', models.BooleanField(default=False)),
                ('size', models.PositiveIntegerField(default=8, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(32)])),
                ('draft_start', models.DateTimeField(default=datetime.datetime(2015, 2, 19, 5, 9, 6, 66610))),
                ('season', models.CharField(default=b'S4Spr', max_length=5, choices=[(b'S5Spr', b'Season 5 Spring'), (b'S5Sum', b'Season 5 Summer'), (b'S5Fall', b'Season 5 Fall')])),
                ('region', models.CharField(default=b'NA', max_length=4, choices=[(b'NA', b'North America'), (b'EU', b'Europe'), (b'NAEU', b'North America & Europe')])),
                ('transactions_per_time_period', models.PositiveIntegerField(default=3)),
                ('transaction_time_period', models.CharField(default=b'W', max_length=1, choices=[(b'D', b'Daily'), (b'W', b'Weekly')])),
                ('team_size', models.PositiveIntegerField(default=7, validators=[django.core.validators.MinValueValidator(5)])),
                ('top_score', models.CharField(default=b'([kda] * 15 + [cs]) / [game time]', max_length=64)),
                ('jungle_score', models.CharField(default=b'([kda] * 25 + [cs]) / [game time]', max_length=64)),
                ('mid_score', models.CharField(default=b'([kda] * 15 + [cs]) / [game time]', max_length=64)),
                ('ad_score', models.CharField(default=b'([kda] * 15 + [cs]) / [game time]', max_length=64)),
                ('support_score', models.CharField(default=b'([kda] + [gold]) * 25 / [game time]', max_length=64)),
                ('per_game_losing_mod', models.CharField(default=b'[score]*0.8', max_length=32)),
                ('per_game_godly_mod', models.CharField(default=b'[score]*1.2', max_length=32)),
                ('season_length', models.PositiveIntegerField(default=8)),
                ('commish', models.ForeignKey(related_name='managed_leagues', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='leagues', through='drafter.FantasyTeam', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invite', models.BooleanField(default=False)),
                ('request', models.BooleanField(default=False)),
                ('message', models.CharField(max_length=256, blank=True)),
                ('new', models.BooleanField(default=True)),
                ('recipient', models.ForeignKey(related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
                ('target_league', models.ForeignKey(blank=True, to='drafter.League', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('region', models.CharField(max_length=2, choices=[(b'NA', b'North America'), (b'EU', b'Europe')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='drafter.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fantasyteam',
            name='league',
            field=models.ForeignKey(related_name='teams', to='drafter.League'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fantasyteam',
            name='manager',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fantasyteam',
            name='players',
            field=models.ManyToManyField(related_name='fantasy_teams', through='drafter.FantasyContract', to='drafter.Player', blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='fantasyteam',
            unique_together=set([('manager', 'league')]),
        ),
        migrations.AddField(
            model_name='fantasymatch',
            name='teams',
            field=models.ManyToManyField(to='drafter.FantasyTeam'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fantasycontract',
            name='player',
            field=models.ForeignKey(to='drafter.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fantasycontract',
            name='team',
            field=models.ForeignKey(to='drafter.FantasyTeam'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('username', 'email')]),
        ),
    ]
