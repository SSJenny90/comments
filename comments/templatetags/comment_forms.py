from django import template
from crispy_forms.utils import render_crispy_form
from django.template.context_processors import csrf
from ..forms import FloatingCommentForm
register = template.Library()

@register.simple_tag(takes_context=True)
def floating_comment_form(context):
    """Renders a comment form that can be used for direct replies in the comment section"""
    return render_crispy_form(FloatingCommentForm, context=csrf(context['request']))