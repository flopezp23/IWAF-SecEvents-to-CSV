import requests
import pandas as pd
import json

# Suppress SSL warnings if needed
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
Auth='Basic YWRtaW46cmFkd2FyZQ==' #Replace with the value in the Authorization header
Auth2='vantage_auth=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6ImFkbWluIiwiYXB3IjoicmFkd2FyZSIsInJvbGUiOiJBZG1pbmlzdHJhdG9ycyIsIndlYkFwcElkcyI6W10sImFwdCI6IjRGNDNCQjJCNlA0YkExOTQyNDE0TDlXQUVFYkE5NzRCIiwiaWF0IjoxNzIwNDg2Mzc2LCJleHAiOjE3MjA0ODczOTZ9.tGr6chP94gMYNoXyZz1Bkl4PpgbXp5eGkMiu4hN24FrFt3BL7VaKfBmB9y53B7JzQsRnUGmsMDNqxh2Yrl2HLg; io=_kChfH2vP5AtwLJGAA-G' #Replace with the value in the Cookie header

Index=0
# Define the API endpoint and headers if necessary
url = 'https://172.30.4.45/appwall-api/v3/Forensics' #Replace with the IP or hostname of your device
headers = {
    'Authorization': Auth,
    'Content-Type': 'application/json; charset=utf-8',
    'Cookie': Auth2
}

# Define the payload for the POST request
payload = {
    "Select": {
        "Order": {
            "field": "Date",
            "dir": "desc"
        },
        "PageIndex": Index,
        "Query": {
            "Name": "Default View",
            "ID": "",
            "EventTable": "Security",
            "EventType": [
                "Lowest",
                "Low",
                "Medium",
                "High",
                "Critical"
            ],
            "DateTime_From": {"Year":2024,"Month":"May","Day":6,"Hour":"23","Minutes":"00"}, #Replace with the desired initial date and time
            "DateTime_To": {}, #Fill out with the desired end date and time
            "Source": {
                "ID": "",
                "Value": "",
                "Type": "",
                "Exclude": False
            },
            "Target": {
                "ID": "258", #Leave blank for all the applications. For a specific applicaiton read the instructions
                "Value": "vuln-apps-local", #Fill out with the application name for a specific application. Set as All for all the applications.
                "Type": "Web Applications",
                "Exclude": False
            },
            "TargetPort": "",
            "TargetIP": {
                "Value": "",
                "Exclude": False
            },
            "User": {
                "ID": "",
                "Value": "All",
                "Exclude": False
            },
            "UserName": {
                "Value": "",
                "Exclude": False
            },
            "TransID": {
                "Value": "",
                "Exclude": False
            },
            "URI": {
                "Value": "",
                "Exclude": False
            },
            "ParamName": {
                "Value": "",
                "Exclude": False
            },
            "Description": {
                "Value": "",
                "Exclude": False
            },
            "Tunnel": {
                "ID": "",
                "Value": "All",
                "Exclude": False
            },
            "VHost": {
                "ID": "",
                "Value": "All",
                "Exclude": False
            },
            "Role": {
                "ID": "",
                "Value": "All",
                "Exclude": False
            },
            "AppPath": {
                "ID": "",
                "Value": "All",
                "Exclude": False
            },
            "IsPassiveMode": {
                "Value": "All",
                "Exclude": False
            },
            "SuppressedCount": {
                "Value": "All",
                "Exclude": False
            },
            "Refine": {
                "Value": "All",
                "Exclude": False
            },
            "Geo": {
                "Value": "",
                "Exclude": False
            },
            "Attack": {
                "ID": "",
                "Value": "",
                "IsNull": False
            },
            "Group": {
                "IP": False,
                "Attack": False
            }
        }
    }
   
}

# Make a POST request to the API
response = requests.post(url, headers=headers, json=payload, verify=False)
st=response.status_code
print (st)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    json_data = response.json()
    extracted_data=response.json().get('EventLog', {}).get('Event')
    #keys_to_extract = ['Info']
    #extracted_data = {key: json_data[key] for key in keys_to_extract if key in json_data}
     #Convert the JSON data to a DataFrame
    datakey='RecordID'
    df = pd.json_normalize(extracted_data)
    # Define the output CSV file path
    csv_file_path = 'output.csv'
    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False, mode='a')
    print("Index", Index, "has been written")
    while Index in range(0, 100000):
        Index+=1
        payload = {
    "Select": {
        "Order": {
            "field": "Date",
            "dir": "desc"
        },
        "PageIndex": Index,
        "Query": {
            "Name": "Default View",
            "ID": "",
            "EventTable": "Security",
            "EventType": [
                "Lowest",
                "Low",
                "Medium",
                "High",
                "Critical"
            ],
            "DateTime_From": {"Year":2024,"Month":"May","Day":6,"Hour":"23","Minutes":"00"},
            "DateTime_To": {},
            "Source": {
                "ID": "",
                "Value": "",
                "Type": "",
                "Exclude": False
            },
            "Target": {
                "ID": "258",
                "Value": "vuln-apps-local",
                "Type": "Web Applications",
                "Exclude": False
            },
            "TargetPort": "",
            "TargetIP": {
                "Value": "",
                "Exclude": False
            },
            "User": {
                "ID": "",
                "Value": "All",
                "Exclude": False
            },
            "UserName": {
                "Value": "",
                "Exclude": False
            },
            "TransID": {
                "Value": "",
                "Exclude": False
            },
            "URI": {
                "Value": "",
                "Exclude": False
            },
            "ParamName": {
                "Value": "",
                "Exclude": False
            },
            "Description": {
                "Value": "",
                "Exclude": False
            },
            "Tunnel": {
                "ID": "",
                "Value": "All",
                "Exclude": False
            },
            "VHost": {
                "ID": "",
                "Value": "All",
                "Exclude": False
            },
            "Role": {
                "ID": "",
                "Value": "All",
                "Exclude": False
            },
            "AppPath": {
                "ID": "",
                "Value": "All",
                "Exclude": False
            },
            "IsPassiveMode": {
                "Value": "All",
                "Exclude": False
            },
            "SuppressedCount": {
                "Value": "All",
                "Exclude": False
            },
            "Refine": {
                "Value": "All",
                "Exclude": False
            },
            "Geo": {
                "Value": "",
                "Exclude": False
            },
            "Attack": {
                "ID": "",
                "Value": "",
                "IsNull": False
            },
            "Group": {
                "IP": False,
                "Attack": False
            }
        }
    }
   
}
        # Make a POST request to the API
        response = requests.post(url, headers=headers, json=payload, verify=False)
        st=response.status_code
        #print(response)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()
            extracted_data=response.json().get('EventLog', {}).get('Event')
            #keys_to_extract = ['Info']
            #extracted_data = {key: json_data[key] for key in keys_to_extract if key in json_data}
            #Convert the JSON data to a DataFrame
            #print(extracted_data)
            if not extracted_data:
                print('Collection completed')
                Index='string'
            else:
                df = pd.json_normalize(extracted_data)
                # Define the output CSV file path
                csv_file_path = 'output.csv'
                # Save the DataFrame to a CSV file
                df.to_csv(csv_file_path, index=False, mode='a',header=False)
                print("Index", Index, "has been written")
                


            
        else:
            print('process failed during data collection')
            
            

 
    print(f"Data has been successfully saved to {csv_file_path}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}, Response: {response.text}")