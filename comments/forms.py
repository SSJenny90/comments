from django.utils.translation import gettext_lazy as _
from django_comments_xtd.forms import XtdCommentForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.urls import reverse
import django_comments
from django import forms

class SuperCommentForm(XtdCommentForm):
    next = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['followup'].required = False
        self.helper = FormHelper(self)
        self.helper.form_id = 'commentForm'
        self.helper.form_method = 'POST'
        self.helper.form_action = django_comments.get_form_target()
        self.helper.attrs = {"onsubmit": "post.disabled = true; return true;"}
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Field('next', value=reverse('comments-xtd-sent') + '#commentTree', type="hidden"),
            'content_type',
            'object_pk',
            'timestamp',
            'security_hash',
            'reply_to',
            Field('name', type="hidden"),
            Field('email', type="hidden"),
            Field('url', type="hidden"),
            Field('honeypot', type="hidden"),
            Field('comment', rows='5', placeholder='Your comment'),
            Field('followup', template='forms/checkbox.html'),
            Submit('post','send'),
        )


class FloatingCommentForm(XtdCommentForm):
    next = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'floatingCommentForm'
        self.helper.form_method = 'POST'
        self.helper.form_action = django_comments.get_form_target()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field('next', value=reverse('comments-xtd-sent') + '#commentTree', type="hidden"),
            'content_type',
            'object_pk',
            'timestamp',
            'security_hash',
            'reply_to',
            Field('name', type="hidden"),
            Field('email', type="hidden"),
            Field('url', type="hidden"),
            Field('honeypot', type="hidden"),
            Field('comment', rows='5', placeholder='Your comment'),
            Field('followup', value='true', template='forms/checkbox.html', type="hidden"),
        )