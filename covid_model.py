import random
import pandas as pd


def generate_covid_data(num_samples=100):
    data = []
    for _ in range(num_samples):
        fever = round(random.uniform(97.0, 104.0), 1)  
        cold = random.choice([True, False])  
        shivering = random.choice([True, False])  
        weight_loss = round(random.uniform(0, 10), 1) 
        
        data.append({"fever": fever, "cold": cold, "shivering": shivering, "weight_loss": weight_loss})
    
    return pd.DataFrame(data)


covid_data = generate_covid_data()

def sort_and_display(data, sort_by="fever"):
    if sort_by not in data.columns:
        print("Invalid parameter for sorting. Please choose from 'fever', 'cold', 'shivering', or 'weight_loss'.")
        return
    
    sorted_data = data.sort_values(by=sort_by, ascending=True)
    print(sorted_data)


sort_by = input("Enter the parameter to sort by (fever, cold, shivering, weight_loss): ").lower()
sort_and_display(covid_data, sort_by)
