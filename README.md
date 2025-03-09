This tool is a simple command-line interface (CLI) utility that allows users to execute various network-related commands, manage IP addresses, and perform text manipulation tasks (such as converting text to ASCII Art). The tool utilizes external libraries such as subprocess to run commands, and os for interacting with the file system and directories.
Functionality

    Clear the Screen: The tool starts by clearing the terminal screen using system("cls||clear"), providing a clean interface when the program begins.

    Display the Logo: The logo or header of the program is displayed with the function logos.code_logo().

    User Command Input: The program enters a loop where it continuously accepts user input. Users can type commands in the terminal, and the program will execute them accordingly.

    Change Directory (cd): If the user enters a command starting with cd (change directory), the program attempts to change the current working directory to the path provided by the user. If the directory is invalid or permission is denied, it displays an appropriate error message.

    Available Commands: The tool has a set of predefined commands, such as:
        whattools: Lists all available tools and their descriptions.
        myip: Displays the device's current IP address.
        checkip: Shows details about a specific IP address.
        scanport: Scans ports on a website or device.
        shndevice: Lists devices connected to the network.
        netmonitor: Changes the network interface mode (e.g., monitor mode).
        texter: Converts text into ASCII art.

    Executing Other Commands: If the command doesn't match one of the predefined ones, the program attempts to execute it as a shell command using subprocess.run().

Tool Breakdown:

    myip: Displays your device's public IP address.
    checkip: Displays detailed information about a specified IP address.
    scanport: Scans for open ports on a given website or device.
    shndevice: Displays a list of devices currently connected to the same network.
    netmonitor: Changes the network interface to monitor mode, enabling the user to capture network traffic.
    texter: Converts regular text into ASCII art using libraries like figlet or pyfiglet.
