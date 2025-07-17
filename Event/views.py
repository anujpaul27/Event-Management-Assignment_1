# views.py
from django.shortcuts import render, redirect, HttpResponse
from .models import Event, Participant, Category
from .forms import EventForm, ParticipantForm, CatagoriForm
from django.contrib import messages
import datetime

        # ---------- Event Views ----------
def event_list(request):
    return Event.objects.select_related("category").all()
    
def event_create(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request , "Event added successfully !")            
        else:
            messages.error(request , "Something Went Wrong !")
    return render(request, 'form.html', {'form': form, 'title': 'Create Event'})

def event_update(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request , "Form updated successfully!")            
        else:
            messages.error(request, "Something went wrong!")
    else:
        form = EventForm(instance=event)
    return render(request, 'form.html', {'form': form, 'title': 'Update Event'})

def event_delete(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'confirm_delete.html', {'type': 'event'})


# ------ HOME PAGE ---------    

def Home (request):
    events = event_list(request)
    return render(request,'home.html', {"events": events, })


# ------ Dashboard PAGE ---------

def dashboard (request):
    events = event_list(request)
    TotalParticipant = Participant.objects.count()
    TotalEvent = Event.objects.count()
    today= datetime.date.today()
    PastEvent = Event.objects.filter(date__lt=today).count()
    UpcomingEvent = Event.objects.filter(date__gte=today).count()
    TodayEvent = Event.objects.filter(date = today)
    context={   'total_participant':TotalParticipant,
                'total_event': TotalEvent,
                'past': PastEvent,
                'upcoming': UpcomingEvent,
                'TodayEvent' : TodayEvent,
                'events': events
                                            }    
    return render(request,'dashboard.html',context)

# Insertoin Tail as a dashboard 
# ---------- Participant Views ----------

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'participant_list.html', {'participants': participants})

def participant_create(request):
    form = ParticipantForm()    
    if request.method == "POST":
        form = ParticipantForm(request.POST or None)        
        if form.is_valid():
            form.save()
            messages.success(request,"Participant Added Successfull")
        else:
            messages.error(request,"Something Went to Wrong !")
    return render(request, 'form.html', {'form': form, 'title': 'Create Participant'})

def participant_update(request, pk):
    participant = Participant.objects.get(pk=pk)    
    if request.method == "POST":
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            messages.success(request,"Participant Update Successfull")
        else:
            messages.error(request,"Something Went to Wrong!")
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'form.html', {'form': form, 'title': 'Update Participant'})

def participant_delete(request, pk):
    participant = Participant.objects.get(pk=pk)
    if request.method == 'POST':
        participant.delete()
        return redirect('participant_list')
    return render(request, 'confirm_delete.html', {'object': participant, 'type': 'Participant'})


# ---------- Category Views ----------
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_create(request):
    form = CatagoriForm()
    if request.method == "POST":
        form = CatagoriForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Category Create Seccessfull !")
        else:
            messages.error(request,"Something Went to Error!")
    return render(request, 'form.html', {'form': form, 'title': 'Create Category'})

def category_update(request, pk):
    category = Category.objects.get(pk=pk)
    form = CatagoriForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'form.html', {'form': form, 'title': 'Update Category'})

def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'confirm_delete.html', {'object': category, 'type': 'Category'})

    