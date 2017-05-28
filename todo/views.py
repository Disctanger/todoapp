from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django import http
from .forms import (
    ListForm,
    ItemForm,
    ItemCompleteForm,
    ItemDeleteForm,
    ListDeleteForm,
    ToDoForm)
from .models import (List, Item)


import datetime
# Create your views here.

def list (request):
    info=""
    delete_form = ListDeleteForm(request.POST or None)
    print (str(request.POST or None))
    form = ListForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        incompleteItem = instance.incomplete_tasks
        info="Successfully changed to Created new Todo List: " + instance.title
    queryset = List.objects.all()    
        
    for item in queryset:        
        if str(item.id) in request.POST:
            item.delete()
                
    form = ListForm()
    queryset = List.objects.order_by('-createTime')
    for items in queryset:
        items.todoAmount = Item.objects.filter(list=items.id).count()
        items.finishedAmount = Item.objects.filter(list=items.id, completed=True).count()
 
    context = {
        "info" : info,
        "object_list": queryset,
        "title" : "List",
        "form" : form,
        "finishedItems" : "",
        "allItems" : "",
        "delete_form" : delete_form
    }
    return render(request, "toppage/toppage.html", context)



def detail (request, id):
    info=""

    instance = get_object_or_404(List,id=id)
    currentItem = None
    deleteForm = ItemDeleteForm(request.POST or None)
    completeForm = ItemCompleteForm(request.POST or None)
    test = request.POST.get('title')
    form = []
    form = ToDoForm(request.POST or None)
    
    queryset = Item.objects.filter(list=id).order_by('due_Date')
    for item in queryset:        
        if str(item.id) in request.POST:
            currentItem = item
            

    
    if (not currentItem == None):
        if (request.POST[str(currentItem.id)])== 'Complete':
            currentItem.completed = True
            currentItem.completed_date = datetime.datetime.now()
            currentItem.save()
            info="Successfully changed to Completed state"
            
        elif (request.POST[str(currentItem.id)])== 'Uncomplete':
            currentItem.completed = False
            currentItem.save()
            info="Successfully changed to Uncomplete state"
        elif (request.POST[str(currentItem.id)])== 'Delete':
            info="Successfully Deleted the item: " + currentItem.title
            currentItem.delete()
            
            
        instance.save()
    else:
        print ("Item equals to None")
    
    queryset = Item.objects.filter(list=id).order_by('due_Date')
    currentList = List.objects.filter(id=id)
    for itemIter in currentList:        
        list_title = itemIter.title

    print(list_title)
    

    
    if test:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.list_id= id
            instance.save()
            info="Successfully added new Item: " + instance.title
            #return http.HttpResponseRedirect('')
            
        
    
    form = ToDoForm()
    print(str(form))
    context = {
        "info" : info,
        "object_list": queryset,
        "instance": instance,
        "title" : "Item",
        "form" : form,
        "completeForm" : completeForm,
        "deleteForm": deleteForm,
        "listId" : id,
        "list_title": list_title,
    }
    return render(request, "toppage/detail.html", context)

def search (request):
    info=""
    messageList=""
    messageItem= ""
    query_list_for_list= List.objects.all()
    query_list_for_item= Item.objects.all()
    
    queryList = request.GET.get('q')
    if queryList:
        query_list_for_list= query_list_for_list.filter(title__icontains=queryList).order_by('-createTime')
        if not query_list_for_list:
            messageList="There are no ToDo lists related to " + str(queryList)
        
    elif queryList == "" or queryList== None:
        query_list_for_list = []
        messageList="There are no ToDo lists to show"
        

    queryItem = request.GET.get('q')
    if queryItem:
        query_list_for_item= query_list_for_item.filter(title__icontains=queryItem).order_by('-due_Date')
        info = "There are " + str(query_list_for_item.count()) + " ToDos and " + str(query_list_for_list.count()) + " ToDo lists according to the search request"
        if not query_list_for_item:
            messageItem="There are no ToDos related to " + str(queryItem)
        
    elif queryItem == "" or queryItem == None:
        query_list_for_item = []
        print("Nothing there")
        messageItem="There are no ToDos to show"
    
        
    
    print(str(query_list_for_list))
    print(str(query_list_for_item))
    context = {
        "info" : info,
        "messageItem": messageItem,
        "messageList": messageList,
        "todoContent" : query_list_for_item,
        "todoListContent" : query_list_for_list,        
        }
    
    return render(request, "toppage/search.html", context)

def edit(request):
    if request.method == 'GET':
        form = ToDoForm()
    else:
        form = ToDoForm(request.POST)
    return render(request,
                  "toppage/template.html",
                  dict(form=form))
