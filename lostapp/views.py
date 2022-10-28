from django.shortcuts import render, redirect, get_object_or_404
from .models import Lost, Comment
from getherapp.models import Classroom
from .forms import LostForm, LostEditForm, CommentForm, CheckPasswordForm

# Create your views here.
def main(request):
    forms = Lost.objects.all()
    return render(request, 'lost_main.html', {'read_forms':forms})

def write(request):
    if request.method == 'POST':
        form = LostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('lost_detail', form.id)
        else:
            context = {
                'write_form':form
            }
            return render(request, 'lost_write.html', context)
    else:
        form = LostForm()
        return render(request, 'lost_write.html', {'write_form':form})

def detail(request, id):
    detail_form = get_object_or_404(Lost, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.lost_id = detail_form
            comment.content = form.cleaned_data['content']
            comment.save()
            return redirect('lost_detail', id)
    else: 
        form = CommentForm()
        return render(request, 'lost_detail.html', {'detail_form':detail_form, 'comment_form':form})

    return render(request, 'lost_detail.html', {'detail_form':form})

def check_password(request, id, page):
    form = get_object_or_404(Lost, id=id)
    if request.method == 'POST':
        pw_form = CheckPasswordForm(request.POST)
        pw = int(request.POST['password'])
        if form.password == pw:
            if page=='edit':
                return redirect('lost_edit', form.id)
            elif page=='delete':
                return redirect('lost_delete', form.id)
        else:
            error = '비밀번호가 일치하지 않습니다.'
            password_form = CheckPasswordForm()
            return render(request, 'check_password.html', {'error':error, 'password_form':password_form})
    else:
        password_form = CheckPasswordForm()
        return render(request, 'check_password.html', {'password_form':password_form})

def edit(request, id):
    edit = get_object_or_404(Lost, id=id)
    classroom = Classroom.objects.all()
    if request.method == "POST":
        form = LostEditForm(request.POST, request.FILES, instance = edit)
        print(form)
        if form.is_valid():
            edit = form.save(commit = False)
            edit.save()
            return redirect('lost_detail', id)
    else:
        form = LostEditForm(instance = edit)
    return render(request, 'lost_edit.html', {'edit_form': form, 'edit': edit, 'classroom':classroom})

def delete(request, id):
    form = get_object_or_404(Lost, id=id)
    form.delete()
    return redirect('lost_main')