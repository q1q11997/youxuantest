# Generated by Django 2.0 on 2018-05-12 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('url', models.URLField(max_length=1000, verbose_name='网址')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='价格')),
                ('loc', models.CharField(default='暂无', max_length=255, verbose_name='作者/出版社')),
                ('review', models.IntegerField(default=0, verbose_name='评论数')),
                ('photo', models.URLField(max_length=1000, verbose_name='图片名')),
                ('owner', models.CharField(choices=[('当当书城', 'DD'), ('淘宝图书', 'TB'), ('京东图书', 'JD')], default='当当书城', max_length=255, verbose_name='所属书城')),
            ],
            options={
                'verbose_name': '书籍',
                'verbose_name_plural': '书籍',
            },
        ),
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=100, unique=True, verbose_name='类型名')),
            ],
            options={
                'verbose_name': '书籍类型',
                'verbose_name_plural': '书籍类型',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='typename',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bookType', to='book.BookType', verbose_name='标签'),
        ),
    ]
