from django.forms import ModelForm
from myapp.models import Article
from django.utils.translation import gettext_lazy as _


# Create the form class.
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter']
        # or
        fields = '__all__'
        # or
        exclude = ['title']

        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

        labels = {
            'headline': _('Writer'),
        }

        help_texts = {
            'headline': _('Some useful help text.'),
        }

        error_messages = {
            'headline': {
                'max_length': _("This writer's name is too long."),
            },
        }


