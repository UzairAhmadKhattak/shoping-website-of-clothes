from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
import psycopg2

#code for restriction on password
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_list=[item for item in alpha]
symbols=['!','@','#','$','^','&','*']
numb=['1','2','3','4','5','6','7','8','9','0']

def making_strong_password(password):
    sys=[]
    num=[]
    alph=[]
    for item in password:
        if item in symbols:
            sys.append(True)
        if item in numb:
            num.append(True)
        if item in alpha_list:
            alph.append(True)

    if True in sys and True in num and True in alph:
        return True
    else:
        return False


# Create your views here.
def signup(request):

    if request.method == 'POST':

        full_name = request.POST['full_name']
        user_name = request.POST['user_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2 and len(password1)>=8 and making_strong_password(password1):

            if User.objects.filter(username=user_name).exists():

                messages.error(request,'User Exist')
                return redirect('signup')

            elif User.objects.filter(email=email).exists():

                messages.info(request,'Email Exist')
                return redirect('signup')

            else:
                user = User.objects.create_user(username=user_name, first_name=full_name,password=password1, email=email)
                user.save()
                messages.success(request,'User Registered')
                return redirect('signup')

        else:
            messages.warning(request,'Invalid Password')
            return redirect('signup')

    else:

        return render(request,'registration form/form for reg.html')

def login(request):

    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(request,username=user_name,password=password)
        if user:
            auth.login(request,user)
            print('logined')
            return redirect('home')
        else:
            print('invalid password or username')
            messages.info(request,'Invalid Password Or User Name')
            return redirect('login')
    else:
        return render(request,'registration form/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


# from here i will write sql code for any changes


def view_database_contents():

    con = psycopg2.connect("dbname='postgres' user='Uzair Ahmad' password='1234' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("SELECT * FROM public.auth_user")
    rows = cur.fetchall()
    con.close()
    return rows



def delete_database_content(item_in_row):
    con = psycopg2.connect("dbname='postgres' user='Uzair Ahmad' password='1234' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("DELETE FROM public.auth_user WHERE first_name=%s",(item_in_row,))
    con.commit()
    con.close()




def insert_database_content(a,b,c):
    con = psycopg2.connect("dbname='postgres' user='Uzair Ahmad' password='1234' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("INSERT INTO public.auth_user VALUES(%s,%s,%s)",(a,b,c,))
    con.commit()
    con.close()

def update_database_content(a, b, c):
    con = psycopg2.connect("dbname='postgres' user='Uzair Ahmad' password='1234' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("UPDATE public.auth_user SET a=%s, b=%s WHERE c=%s", (a, b, c,))
    con.commit()
    con.close()

# delete_database_content("Uzair Ahmad")
# print(type(view_database_contents()))