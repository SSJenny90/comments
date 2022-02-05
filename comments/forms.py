from django.utils.translation import gettext_lazy as _
from django_comments_xtd.forms import XtdCommentForm

class SuperCommentForm(XtdCommentForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['followup'].label = _("Notify me of replies")
        self.fields['followup'].widget.attrs = {'class': 'form-check-input',}
        self.fields['comment'].widget.attrs = {'rows': 5, 'placeholder':'Your Comment'}