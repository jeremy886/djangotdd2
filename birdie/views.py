from django.views.generic import TemplateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.core.mail import send_mail
from django.shortcuts import redirect

import stripe

from . import models
from . import forms


class HomeView(TemplateView):
    template_name = "birdie/home.html"


class AdminView(LoginRequiredMixin, TemplateView):
    template_name = "birdie/admin.html"


class PostUpdateView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = "birdie/update.html"
    success_url = "/"

    def post(self, request, *args, **kwargs):
        if getattr(request.user, 'first_name', None) == 'Spiderman':
            raise Http404()
        return super().post(request, *args, **kwargs)


class PaymentView(View):
    def post(self, request, *args, **kwargs):
        charge = stripe.Charge.create(
            amount=100,
            currency="aud",
            description="",
            token=request.POST.get("token")
        )

        send_mail(
            "Payment received",
            "Charge {} succeeded!".format(charge["id"]),
            "admin@learners.cafe",
            ["user1@somewhereout.com"],
        )

        return redirect("/")