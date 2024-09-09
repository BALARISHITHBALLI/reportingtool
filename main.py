import subprocess
import csv

# Example: Running theHarvester
def run_theHarvester(domain):
    try:
        print(f"Running theHarvester on {domain}...")
        result = subprocess.run(["theHarvester", "-d", domain, "-b", "all"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error running theHarvester: {e}")
        return None

# Example: Running XSStrike
def run_XSStrike(url):
    try:
        print(f"Running XSStrike on {url}...")
        result = subprocess.run(["xsstrike", "--crawl", "--url", url], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error running XSStrike: {e}")
        return None

# Example: Running Scapy (for network scanning)
def run_scapy(target):
    try:
        print(f"Running Scapy scan on {target}...")
        result = subprocess.run(["scapy", "-c", "sniff()", "-p", target], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error running Scapy: {e}")
        return None

# Example: Running OWASP ZAP (for web application scanning)
def run_zap_scan(url):
    try:
        print(f"Running OWASP ZAP scan on {url}...")
        result = subprocess.run(["zap-cli", "spider", url], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error running OWASP ZAP: {e}")
        return None

# Save output to CSV
def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for line in data.splitlines():
            writer.writerow([line])

if __name__ == "__main__":
    domain = "example.com"
    url = "https://balarishithballi.vercel.app/"

    # Run tools and capture output
    theHarvester_report = run_theHarvester(domain)
    XSStrike_report = run_XSStrike(url)
    scapy_report = run_scapy("76.76.21.164")  # Example target IP for scapy
    zap_report = run_zap_scan(url)

    # Save the outputs to CSV
    if theHarvester_report:
        save_to_csv(theHarvester_report, f"{domain}_theHarvester_report.csv")
    if XSStrike_report:
        save_to_csv(XSStrike_report, f"{domain}_XSStrike_report.csv")
    if scapy_report:
        save_to_csv(scapy_report, f"{domain}_Scapy_report.csv")
    if zap_report:
        save_to_csv(zap_report, f"{domain}_OWASP_ZAP_report.csv")
