This tool is a simple command-line interface (CLI) utility that allows users to execute various network-related commands, manage IP addresses, and perform text manipulation tasks (such as converting text to ASCII Art). The tool utilizes external libraries such as subprocess to run commands, and os for interacting with the file system and directories.
Functionality

Install on Debian distributions

    git clone https://github.com/batbyte/batbyte-tool.git
    chmod +x batbyte-tool
    cd batbyte-tool
    bash update.sh
    python3 BatByteOs.py


Tool Breakdown:

    myip: Displays your device's public IP address.
    checkip: Displays detailed information about a specified IP address.
    scanport: Scans for open ports on a given website or device.
    shndevice: Displays a list of devices currently connected to the same network.
    netmonitor: Changes the network interface to monitor mode, enabling the user to capture network traffic.
    texter: Converts regular text into ASCII art using libraries like figlet or pyfiglet.
