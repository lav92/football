from django.forms import models
from news.models import News, Category, Tag


class AddNewsForm(models.ModelForm):
    category = models.ModelChoiceField(queryset=Category.objects.all(), empty_label='Category not chosen')
    tags = models.ModelChoiceField(queryset=Tag.objects.all(), empty_label='Tag not chosen')

    class Meta:
        model = News
        fields = ['title', 'content', 'photo']
        prepopulated_fields = {'slug': ('title',)}
