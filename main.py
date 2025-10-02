from fastapi import FastAPI , Path, HTTPException, Query

import json

app= FastAPI()

'''
Helper function to load patient data from JSON file
'''
def load_data():
    with open('patients.json' , 'r') as f:
        data = f.read()
    return json.loads(data)

@app.get('/')
def read_root():
    return {"msg": "Patient management system"}



@app.get('/about')
def about():
    return {"msg": "This is a patient management system"}



@app.get('/view')
def view_patients():
    patients = load_data()
    return patients


@app.get('/patient/{patient_id}')
def get_patient(patient_id: str = Path(...,description="The ID of the patient to retrieve", example="P001")):
    # the tripple dots ... indicates that this is a required parameter . 
    # Load all the patients
    patients = load_data()
    if patient_id in patients:
        return patients[patient_id]
    
    raise HTTPException(status_code=404, detail="Patient not found")



@app.get('/sort')
def sort_patients(sort_by:str = Query(..., description="sort on weight or bmi"), order:str = Query('asc',description='asc or desc')):
    valid_sort_by = ['weight', 'bmi']
    if sort_by not in valid_sort_by:
        raise HTTPException(status_code=400, detail=f"Invalid sort_by value. must be one of {valid_sort_by}")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order value. must be 'asc' or 'desc'")
    

    patients = load_data()
    sort_order = True if order == 'desc' else False

    sorted_data = sorted(patients.values(), key=lambda x: x.get(sort_by, 0), reverse= sort_order)
                         
    return sorted_data