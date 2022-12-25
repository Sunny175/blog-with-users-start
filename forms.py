from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Enter your email ", validators=[DataRequired()])
    name = StringField("Enter your name ", validators=[DataRequired()])
    password = PasswordField("Enter your password ", validators=[DataRequired()])
    submit = SubmitField("Sign me up!")


class LoginForm(FlaskForm):
    email = StringField("Enter your email ", validators=[DataRequired()])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    submit = SubmitField("Logged me in!")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
