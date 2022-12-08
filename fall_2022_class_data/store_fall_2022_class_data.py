import requests, json

def getJSONFiles():
    all_departments = requests.get('http://luthers-list.herokuapp.com/api/deptlist/')
    all_department_data = all_departments.text
    all_department_json = json.loads(all_department_data)

    with open('fall_2022_class_data/all_departments.json', "w") as outfile:
        outfile.write(json.dumps(all_department_data))

    for i in range(len(all_department_json)):
        subject = all_department_json[i].get('subject')
        department = requests.get('http://luthers-list.herokuapp.com/api/dept/' + subject)

        department_data = json.dumps(department.text)

        file_name = "fall_2022_class_data/" + subject + ".json"

        with open(file_name, "w") as outfile:
            outfile.write(department_data)

getJSONFiles()