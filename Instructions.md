# This Assesment is for EMIS job interview stage 2.

# Data from patients is given as FHIR standards.

# we have implemented code based on json data. where data will be converted to Tabular data.

# we have choosen mongo DB as its no-sql data and we can easily do operations on.

# We have resource types in Data. 

# i have seen one gap in data. Thats lack of connection between patient and resource when we transfered to different resource collections.

# My approach is first finding pateint resource and adding to patients Table or collections and finding its id.

# Now i have taken id as primary key to use as foreign key for all the other resources by user.

# Now in all Resorce tables patient id will be appended as foreign key.


>> For running git clone repo.

>> pip install -r requirements.txt

>> python converter.py


or with CI/CD

>> docker-compose build

>> docker-compose up.


# Thanks