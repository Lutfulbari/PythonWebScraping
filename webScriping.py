import requests
import csv

def company_id_no():

    url = "https://www.scaleupinstitute.org.uk/getCompanies.php?offset=0&min_turnover=0&max_turnover=0&min_employees=&max_employees=&min_growth=&max_growth="
    response = requests.get(url)
    data = response.json()

    companyno  = []

    for idno in data:
        company_No = idno["company_no"]
        companyno.append(company_No)

    #print(len(companyno))

    return companyno


def detailsOf_companies(companyId):
    companydetails = []
    count = 0
    for coid in companyId:
        url = "https://www.scaleupinstitute.org.uk/getCompany.php?id={}".format(coid)
        response = requests.get(url)
        data = response.json()

        for detail in data:
            details = {
            'Name' : detail["name"],
            'Address' : detail["address1"] +' '+detail["address2"]+' '+detail["address3"]+' '+detail["address4"],
            'Phone' : detail["telephone"],
            'Website' : detail["website"]
            }
            companydetails.append(details)
            
    return companydetails


all_data = detailsOf_companies(company_id_no()[0:7000])

csv_columns = ['Name', 'Address', 'Phone','Website']

with open("data.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=csv_columns)
    writer.writeheader()
    for data in all_data:
        writer.writerow(data)