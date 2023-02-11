from application.models import Student
import matplotlib.pyplot as plt

def Draw_eng():
    l1,l2 = [],[]
    name = Student.query.all()
    for i in name:
        l1.append(i.Student_name)
        l2.append(i.English)
    plt.figure(figsize=(20, 11))
    plt.bar(l1,l2)
    plt.savefig('static/English.png')

def Draw_phy():
    l1,l2 = [],[]
    name = Student.query.all()
    for i in name:
        l1.append(i.Student_name)
        l2.append(i.Physics)
    plt.figure(figsize=(20, 11))
    plt.bar(l1,l2)
    plt.savefig('static/Physics.png')

def Draw_maths():
    l1,l2 = [],[]
    name = Student.query.all()
    for i in name:
        l1.append(i.Student_name)
        l2.append(i.Maths)
    plt.figure(figsize=(20, 11))
    plt.bar(l1,l2)
    plt.savefig('static/Maths.png')

def Draw_chem():
    l1,l2 = [],[]
    name = Student.query.all()
    for i in name:
        l1.append(i.Student_name)
        l2.append(i.Chemistry)
    plt.figure(figsize=(20, 11))
    plt.bar(l1,l2)
    plt.savefig('static/Chemistry.png')

