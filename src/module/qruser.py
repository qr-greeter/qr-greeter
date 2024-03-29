import json

userid_cache = ""

def qr_json_action(json_data):
    try:
        data = json.loads(json_data)
    except:
        loginwindow.qr.refresh()
    global userid_cache
    role=str(data["userInfoData"]["role"])
    userid=data["userInfoData"]["userId"]
    name=data["userInfoData"]["name"]
    surname=data["userInfoData"]["surname"]
    if userid_cache == userid:
        return
    userid_cache = userid
    if role == "2" or role == "300" or role == "301":
        username = username_prepare(name+"-"+surname)
        create_user(username,userid)
        lightdm.username = username+"-qr"
        lightdm.password = userid
        lightdm.login()
    else:
        loginwindow.qr.refresh()

def username_prepare(u):
    u = u.lower()
    u = u.replace("ç","c")
    u = u.replace("ı","i")
    u = u.replace("ğ","g")
    u = u.replace("ö","o")
    u = u.replace("ş","s")
    u = u.replace("ü","u")
    u = u.replace(" ","-")
    return u


def create_user(username,password):
    defpass=username
    if os.path.exists("/etc/qr-pass"):
        defpass=open("/etc/qr-pass","r").read().strip()
    os.system("""
        user='{0}'
        pass='{1}'
        defpass='{2}'
        if [ ! -d /home/$user ] ; then
            useradd -m $user -s /bin/bash -p $(openssl passwd "$defpass") -U -d /home/$user
            useradd $user-qr -s /bin/bash -p $(openssl passwd "$defpass") -d /home/$user
            mkdir -p /home/$user
            chown $user -R /home/$user
            chmod 755 /home/$user
            uida=$(grep "^$user:" /etc/passwd | cut -f 3 -d ":")
            uidb=$(grep "^$user-qr:" /etc/passwd | cut -f 3 -d ":")
            sed -i "s/:$uidb:/:$uida:/g" /etc/passwd
            for g in ogretmen floppy audio video plugdev netdev lpadmin scanner $user
            do
                usermod -aG $g $user-qr || true
                usermod -aG $g $user || true
            done
            usermod $user-qr -p $(openssl passwd -6 "$pass")
       fi
   """.format(username,password,defpass))

def module_init():
    loginwindow.qr.data_action = qr_json_action
