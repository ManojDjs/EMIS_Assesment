import json
import os
from fhir.resources.bundle import Bundle
from connection.mongo_connect import DB_instance
import json
import sys
print("run")
def main(path = "./data/"):
    json_files = os.listdir(path)
    for i in range(len(json_files)):

        filename = path + json_files[i]
        print(filename)
        try:
            data = Bundle.parse_file(filename)
        except json.decoder.JSONDecodeError:
            continue
        data_From_resource = []
        previous_type = None
        data_instance=DB_instance()
        # Initialize patient into table
        patient_details= []
        patient_id=''
        for data_elements in data.entry:
            if data_elements.resource.resource_type=='Patient':
                        patient_details.append(json.loads(data_elements.resource.json()))
                        patient_id=data_elements.resource.id
        data_instance.insert(Table_name="Patient",Data=patient_details)
        print(patient_id)
        ### we have taken patient id from Patient resource. And we are using this as primary key for all reources.
        ### in future this will impact on retreiving the data. As with primary key we can take all the data from all the resources.
        for data_elements in data.entry:
            resource_type = data_elements.resource.resource_type
            if resource_type=='Patient':
                print(data_elements.resource.json())
                
            dict_data = json.loads(data_elements.resource.json())
            dict_data['Patiend_Original_id']=patient_id
            if resource_type == previous_type or previous_type is None:
                data_From_resource.append(dict_data) 
            else:
                data_instance.insert(previous_type, data_From_resource)
                data_From_resource = [dict_data]
            previous_type = data_elements.resource.resource_type


        print("Parsing File for "+str(i)+"Json File")
    print("Completed All files parsing")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(path= sys.argv[1])
    else:
        main()