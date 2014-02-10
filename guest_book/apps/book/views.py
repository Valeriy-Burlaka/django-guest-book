from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.core.paginator import Paginator, EmptyPage

import httpagentparser
from .forms import MessageForm
from .models import Message


class MessageBoardView(FormView):
    template_name = "book/message_board.html"
    form_class = MessageForm
    success_url = reverse_lazy('book:board')

    def form_valid(self, form):
        data = form.cleaned_data
        user_addr = self.request.META.get('REMOTE_ADDR', '')
        try:
            ua = self.request.META['HTTP_USER_AGENT']
            info = httpagentparser.detect(ua)
            user_browser = info['browser']['name']
            data['user_browser'] = user_browser
        except KeyError:
            pass
        Message.objects.create(username=data['username'],
                               user_email=data['email'],
                               message_text=data['message_body'],
                               user_homepage=data['homepage'],
                               user_addr=user_addr,
                               user_browser=data.get('user_browser', '')
                               )
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(FormView, self).get_context_data(**kwargs)
        messages = Message.objects.all()
        paginator = Paginator(messages, 10)
        # if no page provided return the first page
        index = int(self.request.REQUEST.get('page', 1))
        try:
            page = paginator.page(index)
        except EmptyPage:
            # if requested page is out of range, deliver the last page
            page = paginator.page(paginator.num_pages)
        context['page'] = page
        context['page_numbers'] = paginator.page_range

        return context
