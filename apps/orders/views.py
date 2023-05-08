"""orders views"""

# django
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

# local
from .forms import OrderForm
from .models import Order, ItemTimes


class OrderList(generic.ListView):
    """Class for listing Orders objects."""
    model = Order
    paginate_by = 10
    template_name = 'orders/list.html'


class OrderCreate(generic.CreateView):
    """Class for creating Orders objects."""
    model = Order
    form_class = OrderForm
    template_name = 'orders/create_or_update.html'
    success_url = reverse_lazy('orders:list')

    def get(self, request):
        ItemTimesFormSet = modelformset_factory(ItemTimes, exclude=['order'], extra=5)
        formset = ItemTimesFormSet(queryset=ItemTimes.objects.none())

        return render(request, self.template_name, {
            'form': self.get_form(),
            'formset': formset,
        })
    
    def post(self, request):
        form = self.form_class(request.POST)
        ItemTimesFormSet = modelformset_factory(ItemTimes, exclude=['order'], extra=5)
        formset = ItemTimesFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            order = Order(**form.cleaned_data)
            order.save()

            for form in formset:
                if form.cleaned_data.get('item'):
                    item = form.cleaned_data.get('item')
                    times = form.cleaned_data.get('times')
                    item_times = ItemTimes(
                        item = item,
                        order = order,
                        times = times,
                    )
                    item_times.save()
            
            return redirect(self.success_url)


class OrderUpdate(generic.UpdateView):
    """Class for updating Orders objects."""
    model = Order
    form_class = OrderForm
    template_name = 'orders/create_or_update.html'
    success_url = reverse_lazy('orders:list')

    def get(self, request, **kwargs):
        order = Order.objects.get(pk=kwargs['pk'])
        item_times = ItemTimes.objects.filter(order=order)
        ItemTimesFormSet = modelformset_factory(ItemTimes, exclude=('order',), extra=5)
        formset = ItemTimesFormSet(queryset=item_times)

        return render(request, self.template_name, {
            'form': self.form_class(instance=order),
            'formset': formset
        })
    
    def post(self, request, *args, **kwargs):
        order = Order.objects.get(pk=kwargs['pk'])
        form = self.form_class(request.POST)
        ItemTimesFormSet = modelformset_factory(ItemTimes, exclude=['order'], extra=5)
        formset = ItemTimesFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            print('valid')
            # order = Order(**form.cleaned_data)
            # order.save()

            # for form in formset:
            #     if form.cleaned_data.get('item'):
            #         item = form.cleaned_data.get('item')
            #         times = form.cleaned_data.get('times')
            #         item_times = ItemTimes(
            #             item = item,
            #             order = order,
            #             times = times,
            #         )
            #         item_times.save()
            
            return redirect(self.success_url)
        else:
            print(formset.errors)
            return redirect(self.success_url)


class OrderDelete(generic.DeleteView):
    """Class for deleting Orders objects"""
    model = Order
    success_url = reverse_lazy('orders:list')