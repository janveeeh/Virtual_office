from django.shortcuts import render

# Create your views here.
import bcrypt
import json
from pickle import NONE
from django.shortcuts import redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse




import uuid,os
from django.shortcuts import render
from .models import *
from .forms import CustomerForm
from django.http import HttpResponseRedirect
from .models import Customer, OurProducts,SoldProduct,Employee 
# Create your views here.

def Login(request):
    try:
        result = request.session['ADMIN']
        return render(request,'Login.html')

        # return redirect("admin-dashboard")
    except Exception as e:
        # print("Err",e)
        # return redirect("admin-dashboard")

        return render(request,'Login.html')

def Logout(request):
    request.session.flush()
    return render(request,'Login.html')


def CheckAdminLogin(request):
    

    try:
        email_id = request.POST['emailid']
        print(email_id)
        password = request.POST['password']
        try:
            admin=Employee.objects.get(emailid=email_id)
        except:
            admin=Employee.objects.get(contact=email_id)

        print("hello",admin)
        # Adminlogins.ob
        if bcrypt.checkpw(password.encode("utf8"), admin.password.encode("utf8")):
            request.session['ADMIN']=admin.id
            return redirect('myteam')
        else:
            return render(request, "Login.html", { 'msg': 'Invalid Userid or Password'})

    except Exception as e:
          print("Error",e)
          Logout(request) 
          return render(request, "Login.html", {'msg': 'User Not Registered'})


def Dashboard(request):
    try:
        result = request.session['ADMIN']
        data=Employee.objects.get(id=result)
        
        return render(request, "dashboard.html",{'data':data})
    except  Exception as e:
        Logout(request) 
        print(e)
        return redirect('login')


def Myteam(request):
    try:
        result = request.session['ADMIN']
        data=Employee.objects.get(id=result)
        res=Employee.objects.filter(hr=result)
        print(res)
        return render(request,'Headtemplates/Myteam.html',{'data':data,'res':res})
    except Exception as e:
          print("Error",e)
          return render(request, "Login.html", {'msg': 'User Not Registered'})
    
def Ouremployee(request):
    try:
        result = request.session['ADMIN']
        data=Employee.objects.get(id=result)
   
        res=reversed(Employee.objects.all())
        total=Employee.objects.all().count()
        all_cities=AllCities.objects.all()
        all_institute=AllInstitute.objects.all()
       
        return render(request,'Headtemplates/Ouremployee.html',{'data':data,'total':total,'res':res,'all_cities':all_cities,'all_institute':all_institute})
    except Exception as e:
        print("Error",e)
        return render(request, "Login.html", {'msg': 'User Not Registered'})
    
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def Addnewemployee(request):
    
    try:
        result = request.session['ADMIN']
        
        if is_ajax(request=request) and request.method == "POST":
            
            first_name = request.POST.get('firstname',None)
            last_name = request.POST.get('lastname',None)
            email_id = request.POST.get('emailid')
            pin_code = request.POST.get('pincode',None)
            contact_number = request.POST.get('contactnumber')
            aadhaar_number = request.POST.get('aadhaarnumber',None)
            address = request.POST.get('address',None)
            city = request.POST.get('city',None)
            institute = request.POST.get('institute',None)
            description = request.POST.get('description',None)
            employee_type = request.POST.get('employeetype',None)
            team_head = request.POST.get('teamhead',None)
            start_date = request.POST.get('startdate',None)
            end_date = request.POST.get('enddate',None)
            salt= bcrypt.gensalt()
            hashed = bcrypt.hashpw(contact_number.encode("utf8"),salt)
            hashed=(hashed.decode("utf8"))

            t=Employee.objects.create(hr=result,empid="PGR"+email_id,password=hashed,firstname=first_name,lastname=last_name,emailid=email_id,pincode=pin_code,contact=contact_number,address=address,city=city,aadhaar=aadhaar_number, institute=institute,description=description,emptype=employee_type,teamhead=team_head,start_date=start_date,end_date=end_date) 
            t.save()
          #  EmailService.SendMail(email_id,"Hi your default password is {}".format(contact_number))


            

            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "User Exists"}, status=400)
    except  Exception as e:
            print("error",e)
            return JsonResponse({"error": "User Exists"}, status=400)

def Updateprofile(request):
    
    try:
        result = request.session['ADMIN']
        
        if is_ajax(request=request) and request.method == "POST":
            
            email_id = request.POST.get('emailid')
            contact_number = request.POST.get('contactnumber')
            aadhaar_number = request.POST.get('aadhaar',None)
            address = request.POST.get('address',None)
            pin_code = request.POST.get('pincode',None)
           
        
            Employee.objects.filter(id=result).update(emailid=email_id,pincode=pin_code,contact=contact_number,address=address,aadhaar=aadhaar_number) 
                 
            # EmailService.SendMail(email_id,"Hi your default password is {}".format(contact_number))


            

            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "User Exists"}, status=400)
    except  Exception as e:
            print("error",e)
            return JsonResponse({"error": "User Exists"}, status=400)



def Update_Password(request):
    print("hello")
    try:
        result = request.session['ADMIN']
        password=(Employee.objects.get(id=result)).password
        # print(password,result)
        if is_ajax(request=request) and request.method == "POST":
            currentpwd= request.POST.get('currentpwd',None)
            # print(currentpwd.encode("utf8"))
            newpwd = request.POST.get('newpwd',None)
            confirmpwd = request.POST.get('confirmpwd',None)
            if bcrypt.checkpw(currentpwd.encode("utf8"), password.encode("utf8") ):
                # print("hello")
                salt = bcrypt.gensalt()
                hashed = bcrypt.hashpw(newpwd.encode("utf8"),salt)
                hashed=(hashed.decode("utf8"))
                Employee.objects.filter(id=result).update(password=hashed) 
            else:
                return JsonResponse({"error": "Status not upadated"}, status=400)

            # EmailService.SendMail((Employee.objects.get(id=result)).email,"Hi your password has been updated your new password is {}".format(newpwd))
            # msg = "{}".format(newpwd)
            # a=SendSMS.SendMessage(msg,(Employee.objects.get(id=result)).studentmob) 
            Logout(request)
            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            print(e)
            return JsonResponse({"error": "Status not upadated "}, status=400)


def UpdateProfilePicture(request):
    

    try:
        result = request.session['ADMIN']
        
        if is_ajax(request=request) and request.method == "POST":
            
            picture = request.FILES['upload']
            print(picture)
            filename = str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]
            
            # q = "update employee set picture='{}' where employeeid={} ".format(filename,empid)
            print(filename)  
            oldpicture=Employee.objects.get(id=result).photograph 
            
            Employee.objects.filter(id=result).update(photograph=filename) 
            
            F = open('F:/virtual_office_management/assets/images/'+filename,"wb")
            for chunk in picture.chunks():
                    F.write(chunk)
            F.close()
                
            os.remove('F:/virtual_office_management/assets/images/'+oldpicture)


            

            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "User Exists"}, status=400)
    except  Exception as e:
            print("error",e)
            return JsonResponse({"error": "User Exists"}, status=400)




def ModalCustomerView(request):
    submitted=False

    if request.method == "POST":
        form=CustomerForm(request.POST)
        if form.is_valid():


            Customer.objects.create(
            firstname=form.cleaned_data['firstname'],
            lastname=form.cleaned_data['lastname'],
            emailid=form.cleaned_data['emailid'],
            contact=form.cleaned_data['contact'],
            address=form.cleaned_data['address'],
            pincode=form.cleaned_data['pincode'],
            aadhaar=form.cleaned_data['aadhaar'],
            empid="1",
            )


            #form.save()#also save emp id in db after integrating with registration             
            return HttpResponseRedirect('/modalcustomerview')
    else: 
        form=CustomerForm
        if 'submitted' in request.GET: 
            submitted = True
    # return render(request,'customer_form.html',{'form':form,'submitted':submitted})
    customers=Customer.objects.all()
    #emp_name="Employee one"#pass employee name in object form after registration integration
    return render(request,'customer.html',{'customers':customers,'form':form,'submitted':submitted})




# def updateCustomer(request,pk):
#     # order=Customer.objects.get(cusid=pk)
#     # data=Customer.objects.get(id=pk)
#     # formset = CustomerForm(instance=order)
#     if request.method == 'POST':
#         FirstName=request.POST.get('FirstName')
#         LastName=request.POST.get('LastName')
#         EmailId=request.POST.get('EmailId')
#         Contact=request.POST.get('Contact')
#         Address=request.POST.get('Address')
#         Pincode=request.POST.get('Pincode')
#         Aadhaar=request.POST.get('Aadhaar')

#         Customer.objects.filter(id=pk).update(firstname=FirstName,lastname=LastName,emailid=EmailId,pincode=Pincode,contact=Contact,address=Address,aadhaar=Aadhaar) 
                 
#         return redirect('/')
#     # context={'formset':formset}
#     return render(request,'customer.html')



def deleteCUstomer():
    #inactive
    return

def ProductView(request):
    products=OurProducts.objects.all()
    return render(request,'product.html',{'products':products})



def lastWord(string):
   
    # split by space and converting
    # string to list and
    lis = list(string.split(" "))
     
    # length of list
    length = len(lis)
     
    # returning last element in list
    return lis[length-1]




def ModalSoldProductView(request):
    # submitted=False
    sold_products=SoldProduct.objects.all()
    product_id=OurProducts.objects.all()
    cust_id = Customer.objects.all()
    if request.method == "POST":
        # form=SoldProductForm(request.POST)
        # if form.is_valid():
        product_name=request.POST.get('productname')
        sellingprice=request.POST.get('sellingprice')
        solddate=request.POST.get('solddate')
        cus_name=request.POST.get('cus_name')

            # productname = form.cleaned_data['productid']
        product= OurProducts.objects.get(productname=product_name)
        #     emp_details=Employee.objects.get(empid=1),

        #     print(emp_details[0].empid)
        #     print(product.productname)
        #     print(product.productprice)

        cus_id=lastWord(cus_name)

        SoldProduct.objects.create(
            productid=product.productid,
            productname=product.productname,
            productprice=product.productprice,
            sellingprice = sellingprice,#form.cleaned_data['sellingprice'],
            solddate= solddate,#form.cleaned_data['solddate'],
            empid=Employee.objects.get(empid=1).empid,#current
            cusid=Customer.objects.get(cusid=cus_id).cusid#form.cleaned_data['cusid']
            )         
            # form.save()#also save emp id in db after integrating with registration 
    
    return render(request,'sold_product_view.html',{'sold_products':sold_products,"product_id":product_id,"cust_id":cust_id})
    

def complainlist(request):
     w = Complains.objects.all()
     if request.method == 'POST':
          status=request.POST.get('status')
          w.status = request.POST['Status'] == 'solved'
          w.save()
     complainlist = Complains.objects.all()
     j = Complains.objects.filter(status='unsolved')     
     c = ComplainType.objects.all
     
     if request.method == 'POST':
        #id = request.POST.get('id')
        orderid = request.POST.get('orderid')
        complaintype = request.POST.get('complaintype')
        description = request.POST.get('description')
        cmpby = request.POST.get('cmpby')
        jp = Complains( description=description,orderid=orderid, complaintype = complaintype,cmpby=cmpby,date=date.today())
        jp.save()
        messages.success(request, "Complaint successfully submitted")

    
        
       

     return render(request,'Complaints/complainlist.html',{'complainlist':complainlist, 'c':c,'j':j, 'statuses': w,'w':w})

def dashboard(request):
  
     complainlist = Complains.objects.all()

     return render(request,'Complaints/dashboard.html',{'complainlist':complainlist})


def other_complains(request):
     return render(request,'Complaints/other_complains.html')



