from django.shortcuts import render, redirect
from django.http import HttpResponse
#ดึงข้อมูลโมเดล person มา
from myapp.models import Person
#ดึง mesages มาทำงาน
from django.contrib import messages
import sweetify

# Create your views here.
def index(request):
    #เป็น Obj ได้ข้อมูลมา ทั้งหมด
    all_person = Person.objects.all()
    #เป็น Obj ได้ข้อมูลมา แบบfiter
    #all_person = Person.objects.filter(age=27)
    return render(request, "index.html", {"all_person":all_person})

def about(request):
    return render(request, "about.html")

def form(request):
    if request.method == "POST":
        #รับข้อมูล
            name = request.POST["name"]
            age = request.POST["age"]
            print(name, age)
            #return redirect("/") #ต้องมี return เสมอ
        #บันทึก โดยสร้าง Obj ใหม่
            person = Person.objects.create(
                #ระบุชื่อ field
                name=name,
                age=age
            )
            person.save() #บันทึกเสร็จแล้ว เปลี่ยนเส้นทาง
            #ข้อความตอบกลับ
                # ใช้ messages
            messages.success(request, "บันทึกข้อมูลสำเร็จ")
                #ใช้ switch alert
            sweetify.success(request, 'บันทึกข้อมูลสำเร็จ')
        #เปลี่ยนเส้นทาง
            return redirect("/")
    else :
        return render(request, "form.html")
    
def edit(request,person_id):
    #ตรวจสอบข้อมูลมาแก้ไข
    if request.method == "POST":
        person = Person.objects.get(id=person_id)#เอาข้อมูลมา
        person.name = request.POST["name"]#เอาข้อมูลชื่อมา ที่ส่งมา
        person.age = request.POST["age"]#เอาข้อมูลอายุมา ที่ส่งมา
        #save ทับตัวเดิม
        person.save()
        #ข้อความตอบกลับ
            # ใช้ messages
        messages.info(request, "อัปเดตข้อมูลสำเร็จ")
            #ใช้ switch alert
        sweetify.success(request, 'อัปเดตข้อมูลสำเร็จ')
        #เปลี่ยนเส้นทาง
        return redirect("/")
    else:    #ไม่ส่งข้อมูลมาให้แสดงเฉยๆ
        #ดึงข้อมูลมาแสดง
        person = Person.objects.get(id=person_id)
        return render(request, "edit.html",{"person":person})
    
def delete(request,person_id):
    #ตรวจสอบข้อมูลมาแก้ไข
        person = Person.objects.get(id=person_id)#เอาข้อมูลมา
        #delete ลบ
        person.delete()
        #ข้อความตอบกลับ
            # ใช้ messages
        messages.error(request, "ลบข้อมูลสำเร็จ")
            #ใช้ switch alert
        sweetify.success(request, 'ลบข้อมูลสำเร็จ')
        #เปลี่ยนเส้นทาง
        return redirect("/")
    