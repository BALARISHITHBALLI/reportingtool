import matplotlib.pyplot as plt

def create_bar_chart(data):
    labels = list(data.keys())
    values = list(data.values())
    
    plt.bar(labels, values)
    plt.xlabel('Tools')
    plt.ylabel('Findings')
    plt.title('Pentesting Results')
    plt.savefig('pentesting_results.png')
    plt.show()

if __name__ == "__main__":
    example_data = {
        "theHarvester": 15,
        "Sublist3r": 10,
        "XSStrike": 7,
        "Wapiti": 12
    }
    create_bar_chart(example_data)
