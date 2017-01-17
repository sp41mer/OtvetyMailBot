import peewee
from playhouse.migrate import *

database_sqlite = peewee.SqliteDatabase("temporary.db")

class Question(peewee.Model):
    date = peewee.DateTimeField(null=False)
    href = peewee.TextField(default='', null=False, unique=True)
    title = peewee.TextField(default='', null=False)
    content = peewee.TextField(null=True)
    inf_title = peewee.TextField(null=True)
    inf_content = peewee.TextField(null=True)
    isAnswered = peewee.BooleanField(default=0, null=False)
    answer = peewee.TextField(null=True)

    class Meta:
        database = database_sqlite

class Article(peewee.Model):
    href = peewee.TextField(default='', null=False)
    title = peewee.TextField(default='', null=False)
    text = peewee.TextField(default='', null=False)
    #возможно не сохранилось
    # is_scaned = peewee.BooleanField(default=False, null=False)
    inf_title = peewee.TextField(default='', null=False)
    inf_text = peewee.TextField(default='', null=False)
    keywords = peewee.TextField(default='', null=False)
    times_match = peewee.IntegerField(default=0, null=False)

    class Meta:
        database = database_sqlite

class Text(peewee.Model):
    text = peewee.TextField(default='', null=False)
    last_time = peewee.DateTimeField(null=True)

database_sqlite.create_tables([Question, Article], safe=True)
# migrator = SqliteMigrator(database_sqlite)
# migrate(
#     migrator.add_column('article', 'is_scaned', peewee.BooleanField(default=False, null=False))
# )