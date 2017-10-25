# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-25 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginregis_app', '0012_auto_20171025_1308'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Document',
            new_name='Image',
        ),
        migrations.AlterField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_bookings', to='loginregis_app.User'),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_conversations', to='loginregis_app.User'),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_conversations', to='loginregis_app.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_messages', to='loginregis_app.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='loginregis_app.User'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_pictures', to='loginregis_app.User'),
        ),
        migrations.AlterField(
            model_name='place',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_places', to='loginregis_app.User'),
        ),
        migrations.AlterField(
            model_name='review_place',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_reviews_from_user', to='loginregis_app.User'),
        ),
        migrations.AlterField(
            model_name='review_user',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews_from_user', to='loginregis_app.User'),
        ),
        migrations.AlterField(
            model_name='review_user',
            name='user_being_reviewed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to='loginregis_app.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]