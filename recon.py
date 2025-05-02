import os
import platform
import socket

def system_info():
    print("\n[+] معلومات النظام:")
    print(f"- نظام التشغيل: {platform.system()} {platform.release()}")
    print(f"- إصدار Python: {platform.python_version()}")

def network_info():
    print("\n[+] معلومات الشبكة:")
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(f"- اسم الجهاز: {hostname}")
    print(f"- IP: {ip}")

def battery_info():
    try:
        with open("/sys/class/power_supply/battery/capacity", "r") as f:
            level = f.read().strip()
            print(f"\n[+] مستوى البطارية: {level}%")
    except:
        print("\n[+] لا يمكن قراءة البطارية (قد تكون غير مدعومة).")

def installed_apps():
    print("\n[+] التطبيقات المثبتة:")
    os.system("pm list packages | head -n 10")

if __name__ == "__main__":
    system_info()
    network_info()
    battery_info()
    installed_apps()
