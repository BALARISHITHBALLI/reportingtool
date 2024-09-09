import subprocess

# List of pip-installable pentesting tools (without wapiti)
tools = [
    "theHarvester",
    "sublist3r",
    "scapy",
    "xsstrike",
    "python-owasp-zap-v2.4",
    "crackmapexec",
    "impacket",
    "pwntools",
    "r2pipe",
    "volatility3",
    "boofuzz",
    "scoutsuite",
    "pacu"
]

def install_tools():
    for tool in tools:
        try:
            print(f"Installing {tool}...")
            subprocess.check_call(["pip", "install", tool])
        except subprocess.CalledProcessError:
            print(f"Failed to install {tool}.")
        
if __name__ == "__main__":
    install_tools()
