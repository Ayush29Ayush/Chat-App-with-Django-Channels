from django.shortcuts import render, get_object_or_404, redirect
from a_rtchat.models import ChatGroup, GroupMessage
from django.contrib.auth.decorators import login_required
from a_rtchat.forms import ChatmessageCreateForm

# Create your views here.
@login_required
def chat_view(request):
    # print(f'request.method: {request.method}')
    # print(f'request.POST: {request.POST}')
    # print(f'request.user: {request.user}')

    #! Since we created a dummy group named public-chat, we can use that as value for the group_name field.
    chat_group = get_object_or_404(ChatGroup, group_name='public-chat')
    #! chat_messages is the related name of the group field from the GroupMessage model
    chat_messages = chat_group.chat_messages.all()[:30]

    form = ChatmessageCreateForm()

    if request.method == 'POST':
        form = ChatmessageCreateForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            return redirect('home')

    return render(request, 'a_rtchat/chat.html', {'chat_messages':chat_messages, 'form':form})