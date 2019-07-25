'''
@Description: 
@Author: Wu Xie
@Github: https://github.com/shiehng
@Date: 2019-07-23 23:26:23
'''
from faker import Faker

from hustbook.models import Admin
from hustbook.models import Category
from hustbook.models import Post
from hustbook.extensions import db

fake = Faker()

def fake_admin():
    # 生成虚拟管理员信息
    admin = Admin(
        username='admin',
        blog_title='hustbook',
        blog_sub_title='No, I am the real thing',
        name='Max Kera',
        about='Um, l, Max Kera, had a fun time as a member of ZSM...'
    )
    admin.set_password('hellohustbook')
    ad.session.add(admin)
    db.session.commit()

def fake_categories(count=10):
    # 创建虚拟分类
    category = Category(name='Default')
    db.session.add(category)

    for i in range(count):
        category = Category(name=fake.word())
        db.session.add(category)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

def fake_posts(count=50):
    # 生成虚拟文章
    for i in range(count):
        post = Post(
            title=fake.sentence(),
            body=fake.text(2000),
            category=Category.query.get(random.randint(1, Category.query.count())),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(post)
    db.session.commit()
    