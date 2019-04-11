'''
Created by ZhouSp 18-11-8.
'''
from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, Email, ValidationError

from app.models.user import User

__author__ = 'zhou'


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱格式不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 32)])
    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称最少两个字符，最多10个字符')])

    # 自定义验证器
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮箱已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱格式不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 32)])
