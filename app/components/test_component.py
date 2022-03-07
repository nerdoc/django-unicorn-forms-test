from django_unicorn.components import UnicornView
from django import forms
from ..models import Foo


class ExampleForm(forms.Form):
    c = forms.CharField(max_length=23)


class ExampleModelForm(forms.ModelForm):
    class Meta:
        model = Foo
        fields = ["name"]


class TestComponentView(UnicornView):
    # template_name = "unicorn/test_component.html"
    form = ExampleForm
    count = 1
