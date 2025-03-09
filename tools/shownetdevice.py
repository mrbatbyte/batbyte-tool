import subprocess

def show():
    # الكود المطلوب تشغيله بلغة باش لاكتشاف الأجهزة المتصلة
    bash_command = """
    #!/bin/bash

    echo ""
    echo "\033[32m =++= update nmap =++= "
    echo "\033[31m"
    sudo apt-get install nmap
    echo ""

    echo "\033[32m =++= start scanning =++= "
    echo "\033[31m"
    network="192.168.1.0/24"

    nmap -sn $network
    echo ""
    """

    # تشغيل الكود باستخدام subprocess
    process = subprocess.Popen(bash_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # الحصول على النتيجة من المخرجات
    stdout, stderr = process.communicate()

    # طباعة النتيجة
    if process.returncode == 0:
        print(stdout.decode())
    else:
        print("Error:", stderr.decode())
