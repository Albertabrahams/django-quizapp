# Generated by Django 4.0.6 on 2022-07-18 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Quiz Title')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.category')),
            ],
            options={
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=300, verbose_name='Question Title')),
                ('difficulty', models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')], default='E', max_length=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('answer_text', models.CharField(max_length=300, verbose_name='Answer Text')),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
            ],
            options={
                'verbose_name_plural': 'Answers',
            },
        ),
    ]
