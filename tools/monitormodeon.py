import subprocess

def set_monitor_mode_on():
    interface = input(" \033[1;32m|--- \033[1;31m Your network interface: \033[1;32m")
    try:
        subprocess.run(["sudo", "airmon-ng", "start", interface,], check=True)
        print(f"Your {interface} change to monitor mode")
    except subprocess.CalledProcessError as e:

        print(f"Error: {e}")


def set_monitor_mode_off():
    interface = input(" \033[1;32m|--- \033[1;31m Your network interface: \033[1;32m")
    try:
        subprocess.run(["sudo", "airmon-ng", "stop", interface,], check=True)
        print(f"Your interface {interface} change to Managed mode")
    except subprocess.CalledProcessError as e:

        print(f"Error: {e}")



def monitor():
    select = input(" \033[1;32m|--- \033[1;31m monitor mode (on or off): \033[1;32m")
    if select == "on":
        set_monitor_mode_on()

    elif select == "off":
        set_monitor_mode_off()

    else:
        print("Error")