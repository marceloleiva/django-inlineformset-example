from crispy_forms.layout import Submit, Layout, Div, Field, Fieldset, HTML, ButtonHolder
from django.forms import models, inlineformset_factory
from crispy_forms.helper import FormHelper

from example.custom_layout_object import Formset
from example.models import Order, OrderedItem


class OrderForm(models.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.html5_required = True
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Div(
                Field('customer'),
                Fieldset('Items',
                         Formset('items_formset')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'Save')),
            )
        )


class OrderedItemForm(models.ModelForm):
    class Meta:
        model = OrderedItem
        fields = '__all__'


OrderedItemFormSet = inlineformset_factory(Order, OrderedItem, OrderedItemForm, max_num=5, min_num=1,
                                           validate_min=True, extra=1)
