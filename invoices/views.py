from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Invoice
from profiles.models import Profile
from .forms import InvoiceForm
from django.views import generic
from django.contrib import messages
from positions.forms import PositionForm


class Home_base_view(generic.ListView):
    title: str = "SSC Consult"
    template_name: str = "invoices/index.html"
    model = Invoice
    paginate_by = 3
    context_object_name: str = "qs"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            profil = get_object_or_404(Profile, user=self.request.user)
            return super().get_queryset().filter(profil=profil).order_by("-erstellt")
        else:
            return super().get_queryset().none()

    def get_context_data(self, **kwargs):
        context = super(Home_base_view, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return context


class InvoiceFormView(generic.FormView):
    title: str = "SSC Create Invoice"
    form_class = InvoiceForm
    template_name: str = "invoices/create.html"
    # success_url = reverse_lazy("invoices:base_view")
    i_instance = None

    def get_success_url(self):
        return reverse(
            "invoices:AddPositionsFormView", kwargs={"pk": self.i_instance.pk}
        )

    def form_valid(self, form):
        profil = Profile.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profil = profil
        form.save()
        self.i_instance = instance
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(InvoiceFormView, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return context


class SimpleTemplateView(generic.DetailView):
    title: str = "SSC Detail View"
    model = Invoice
    template_name: str = "invoices/simple_template.html"

    def get_context_data(self, **kwargs):
        context = super(SimpleTemplateView, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return context


class AddPositionsFormView(generic.FormView):
    title: str = "SSC Addpositions"
    form_class = PositionForm
    template_name: str = "invoices/addpositions.html"

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        rechnung_pk = self.kwargs.get("pk")
        rechnung_obj = Invoice.objects.get(pk=rechnung_pk)
        instance = form.save(commit=False)
        instance.rechnung = rechnung_obj
        form.save()
        messages.success(
            self.request, f"Positionen erfolgreich hinzugefügt - {instance.leistung} "
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "SSC Position hinzufügen"
        rechnung_obj = Invoice.objects.get(pk=self.kwargs.get("pk"))
        qs = rechnung_obj.positions
        context["obj"] = rechnung_obj
        context["qs"] = qs
        return context


class InvoiceUpdateView(generic.UpdateView):
    title: str = "SSC Update View"
    model = Invoice
    form_class = InvoiceForm
    success_url = reverse_lazy("invoices:base_view")
    template_name: str = "invoices/update.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.rechnungsdatum = obj.rechnungsdatum.strftime("%Y-%m-%d")
        obj.erfüllungsdatum = obj.erfüllungsdatum.strftime("%Y-%m-%d")
        obj.zahlungsziel = obj.zahlungsziel.strftime("%Y-%m-%d")
        return obj

    def form_valid(self, form):
        instance = form.save()
        messages.success(
            self.request, f" {instance.rechnungsnummer} erfolgreich gespeichert"
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(InvoiceUpdateView, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return context


class CloseInvoiceView(generic.RedirectView):
    pattern_name = "invoices:AddPositionsFormView"

    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        obj = Invoice.objects.get(pk=pk)
        obj.abgeschlossen = True
        obj.save()
        messages.info(
            self.request,
            f" {obj.rechnungsnummer} wurde abgeschlossen, und kann nicht mehr bearbeitet werden",
        )
        return super().get_redirect_url(*args, **kwargs)
