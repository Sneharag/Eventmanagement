from django.shortcuts import render,redirect

from django.views.generic import View

from eventapp.models import EventManager

from eventapp.forms import SignUpForm,SignInForm,EventForm

from django.contrib.auth import authenticate,login,logout

from django.utils.decorators import method_decorator

from eventapp.decorators import signin_required

from django.views.decorators.cache import never_cache

decs=[signin_required,never_cache]

class SignUpView(View):

    template_name="signup.html"

    form_class=SignUpForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("signin")

        return render(request,self.template_name,{"form":form_instance})

class SignInView(View):

    template_name="signin.html"

    form_class=SignInForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_data=request.POST 

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pwd=data.get("password")

            user_obj=authenticate(request,username=uname,password=pwd)

            if user_obj:

                login(request,user_obj)

                return redirect("eventlist")

        return render(request,self.template_name,{"form":form_instance})
    
class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")

@method_decorator(decs,name="dispatch")
class EventListView(View):

    template_name="eventlist.html"

    form_class=EventForm

    def get(self,request,*args,**kwargs):

        qs=EventManager.objects.filter(owner=request.user)

        return render(request,self.template_name,{"data":qs})

@method_decorator(decs,name="dispatch")
class EventCreateView(View):

    template_name="eventadd.html"

    form_class=EventForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            EventManager.objects.create(**data,owner=request.user)

            print("event added")

            return redirect("eventlist")

        return render(request,self.template_name,{"form":form_instance})
   
    

