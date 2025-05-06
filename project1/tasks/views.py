from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = []

def index(request):
    if "tasks" not in request.session: # If the Task List does not exist in this session
        request.session["tasks"] = [] # Create an empty Task List (array)
    return render(request, "tasks/index.html", { 
        "tasks": request.session["tasks"] # Pass the Task List (array) to the index.html template.
    })

def add(request):
    # POST request used to process the task entered by the user when they click the button on the Add Task form.
    if request.method == "POST":
        form = NewTaskForm(request.POST) # Creates a blank form accepting request.POST
        if form.is_valid(): # If the form is verified as secure (string does not contain illegal characters)
            task = form.cleaned_data["task"] # Put the clean string in a variable
            request.session["tasks"] += [task] # Add the task (string) to the task list (array)
            return HttpResponseRedirect(reverse("tasks:index")) # Return to the Task List displaying the added item.
        else:
            return render(request, "tasks/add.html", { # If the data is not verified
                "form": form # Re-display the form with the data and error message.
            })

    # GET request used to present a blank form when the user clicks the New Task link on the Task List
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })

class NewTaskForm(forms.Form):
    task = forms.CharField(
        label='',  # Set label to an empty string to remove it
        widget=forms.TextInput(attrs={
            'autofocus': 'autofocus', 
            'id': 'task', 
            'placeholder': 'New Task'  # Add a placeholder attribute
        })
    )
