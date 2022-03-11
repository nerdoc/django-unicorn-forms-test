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
    # form = ExampleForm
    form_class = ExampleModelForm
    count = 1

    def get_form(self):
        # Instantiate the form with the component's attributes
        return self.form_class(self._attributes())
