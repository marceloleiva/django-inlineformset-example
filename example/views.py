from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from example.forms import OrderedItemFormSet, OrderForm
from example.models import Order


class OrderListView(ListView):
    template_name = 'example/orders.html'
    queryset = Order.objects.all()


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('example:orders')
    template_name = 'example/create.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['items_formset'] = OrderedItemFormSet(self.request.POST, prefix='items')
        else:
            data['items_formset'] = OrderedItemFormSet(prefix='items')
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items_formset']
        with transaction.atomic():
            self.object = form.save()
            if items.is_valid():
                items.instance = self.object
                items.save()
            else:
                return render(self.request, self.template_name,
                              {"form": self.form_class(self.request.POST), "items_formset": items, })

        return super().form_valid(form)


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('example:orders')
    template_name = 'example/update.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        print(self.object)
        if self.request.POST:
            data['items_formset'] = OrderedItemFormSet(self.request.POST, instance=self.object, prefix='items')
        else:
            data['items_formset'] = OrderedItemFormSet(instance=self.object, prefix='items')
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items_formset']
        with transaction.atomic():
            self.object = form.save()
            if items.is_valid():
                items.instance = self.object
                items.save()
            else:
                return render(self.request, self.template_name,
                              {"form": self.form_class(self.request.POST), "items_formset": items, })

        return super().form_valid(form)
