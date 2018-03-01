# ！/usr/bin/python3
# _*_ coding:utf-8 _*_

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, \
    TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import Admin, Tag, Auth, Role

tags = Tag.query.all()
auth_list = Auth.query.all()
role_list = Role.query.all()

class LoginForm(FlaskForm):
    """管理员登录表单"""
    account = StringField(
        label='帐号',
        validators=[
            DataRequired('请输入帐号！')
        ],
        description='帐号',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入帐号！',
            # 'required': 'required'
        }
    )
    pwd = PasswordField(
        label='密码',
        validators=[
            DataRequired('请输入密码！')
        ],
        description='密码',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入密码！',
            # 'required': 'required'
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            'class': 'btn btn-primary btn-block btn-flat'
        }
    )

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError('帐号不存在！')


# Tag表单
class TagForm(FlaskForm):
    name = StringField(
        label='名称',
        validators=[
            DataRequired('请输入标签！')
        ],
        description='标签',
        render_kw={
            'class': 'form-control',
            'id': 'input_name',
            'placeholder': '请输入标签名称！'
        }
    )
    submit = SubmitField(
        '添加',
        render_kw={
            'class': 'btn btn-primary'
        }
    )


# movie表单
class MovieForm(FlaskForm):
    title = StringField(
        label='片名',
        validators=[
            DataRequired('请输入片名！')
        ],
        description='片名',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入片名！'
        }
    )
    url = FileField(
        label='文件',
        validators=[
            DataRequired('请上传文件！')
        ],
        description='文件'
    )
    info = TextAreaField(
        label='简介',
        validators=[
            DataRequired('请输入简介！')
        ],
        description='简介',
        render_kw={
            'class': 'form-control',
            "row": 10,
        }
    )
    logo = FileField(
        label='封面',
        validators=[
            DataRequired('请上传封面！')
        ],
        description='封面'
    )
    star = SelectField(
        label='星级',
        validators=[
            DataRequired('请输入星级！')
        ],
        coerce=int,
        choices=[(1, '1星级'), (2, '2星级'), (3, '3星级'), (4, '4星级'), (5, '5星级')],
        description='星级',
        render_kw={
            'class': 'form-control'
        }
    )
    tag_id = SelectField(
        label='标签',
        validators=[
            DataRequired('请输入标签！')
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in tags],
        description='标签',
        render_kw={
            'class': 'form-control'
        }
    )
    area = StringField(
        label='地区',
        validators=[
            DataRequired('请输入地区！')
        ],
        description='地区',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入地区！'
        }
    )
    length = StringField(
        label='片长',
        validators=[
            DataRequired('请输入片长！')
        ],
        description='片长',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入片长！'
        }
    )
    release_time = StringField(
        label='上映时间',
        validators=[
            DataRequired('请输入上映时间！')
        ],
        description='上映时间',
        render_kw={
            'class': 'form-control',
            'id': 'input_release_time',
            'placeholder': '请输入上映时间！'
        }
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            'class': 'btn btn-primary'
        }
    )

# 上映预告
class PreviewForm(FlaskForm):
    title = StringField(
        label='预告标题',
        validators=[
            DataRequired('请输入预告标题！')
        ],
        description='预告标题',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入预告标题！'
        }
    )
    logo = FileField(
        label='预告封面',
        validators=[
            DataRequired('请上传预告封面！')
        ],
        description='预告封面'
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            'class': 'btn btn-primary'
        }
    )

# 修改密码表单
class PwdForm(FlaskForm):
    old_pwd = PasswordField(
        label='旧密码',
        validators=[
            DataRequired('请输入旧密码！')
        ],
        description='旧密码',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入旧密码！',
            # 'required': 'required'
        }
    )
    new_pwd = PasswordField(
        label='新密码',
        validators=[
            DataRequired('请输入新密码！')
        ],
        description='新密码',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入新密码！',
            # 'required': 'required'
        }
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            'class': 'btn btn-primary'
        }
    )

    def validate_old_pwd(self, field):
        from flask import session
        pwd = field.data
        name = session['admin']
        admin = Admin.query.filter_by(
            name=name
        ).first()
        if not admin.check_pwd(pwd):
            raise ValidationError('旧密码错误！')


# 权限表单
class AuthForm(FlaskForm):
    name = StringField(
        label='权限名称',
        validators=[
            DataRequired('请输入权限名称！')
        ],
        description='权限名称',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入权限名称！'
        }
    )
    url = StringField(
        label='权限地址',
        validators=[
            DataRequired('请输入权限地址！')
        ],
        description='权限地址',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入权限名称！'
        }
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            'class': 'btn btn-primary'
        }
    )


# 角色管理
class RoleForm(FlaskForm):
    name = StringField(
        label='角色名称',
        validators=[
            DataRequired('请输入角色名称！')
        ],
        description='角色名称',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入角色名称！'
        }
    )
    auths = SelectMultipleField(
        label='权限列表',
        validators=[
            DataRequired('请选择权限列表！')
        ],
        description='权限列表',
        coerce=int,
        choices=[(v.id, v.name) for v in auth_list],
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入角色权限列表！'
        }
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            'class': 'btn btn-primary'
        }
    )

class AdminForm(FlaskForm):
    name = StringField(
        label='管理员名称',
        validators=[
            DataRequired('请输入管理员名称！')
        ],
        description='管理员名称',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入管理员名称！',
            # 'required': 'required'
        }
    )
    pwd = PasswordField(
        label='管理员密码',
        validators=[
            DataRequired('请输入管理员密码！')
        ],
        description='管理员密码',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入管理员密码！',
            # 'required': 'required'
        }
    )
    repwd = PasswordField(
        label='管理员重复密码',
        validators=[
            DataRequired('请输入管理员重复密码！'),
            EqualTo('pwd', message='两次密码不一致！')
        ],
        description='管理员重复密码',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入管理员重复密码！',
            # 'required': 'required'
        }
    )
    role_id = SelectField(
        label='所属角色',
        choices=[(v.id, v.name) for v in role_list],
        coerce=int,
        render_kw={
            'class': 'form-control'
        }
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            'class': 'btn btn-primary'
        }
    )
