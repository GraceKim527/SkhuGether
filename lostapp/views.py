from django.shortcuts import render, redirect, get_object_or_404
from .models import Lost, Comment
from .forms import LostForm, LostEditForm, CommentForm

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

# 글 수정/삭제시 비번 확인
def check_password(request, id, page):
    form = get_object_or_404(Lost, id=id)
    if request.method == 'POST':
        ckeck_password = int(request.POST.get('check_password'))
        print(check_password)
        if ckeck_password == form.password:
            if page == 'edit':
                return redirect('lost_edit', form.id)
            elif page == 'delete':
                return redirect('lost_delete', form.id)
        else:
            error = "비밀번호가 일치하지 않습니다."
            return render(request, 'check_password.html', {'error':error})
    else:
        return render(request, 'check_password.html')

def edit(request, id):
    edit_form = get_object_or_404(Lost, id=id)
    if request.method == "POST":
        form = LostEditForm(request.POST, request.FILES, instance = edit_form)
        if form.is_valid():
            form = form.save(commit = False)
            form.save()
            return redirect('lost_detail', id)
    else:
        form = LostEditForm(instance = edit_form)
        if edit_form.image:
            url = edit_form.image.url
            return render(request, 'lost_edit.html', {'edit_form': form, 'image_url': url})
        return render(request, 'lost_edit.html', {'edit_form': form})

def delete(request, id):
    form = get_object_or_404(Lost, id=id)
    form.delete()
    return redirect('lost_main')