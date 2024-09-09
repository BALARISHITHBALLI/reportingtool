from jinja2 import Template

def generate_report(data, template_file="report_template.html"):
    # Load the HTML template
    with open(template_file) as file:
        template = Template(file.read())
    
    # Render the template with data
    report = template.render(results=data)
    
    # Save the report to an HTML file
    with open("pentest_report.html", "w") as report_file:
        report_file.write(report)

if __name__ == "__main__":
    report_data = {
        "domain": "example.com",
        "harvester_results": "theHarvester report data here...",
        "sublist3r_results": "Sublist3r report data here..."
    }
    
    generate_report(report_data)
