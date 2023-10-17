
from twilio.rest import Client 
import random


def appointment_id():
    n=random.randrange(10000,99999)
    aptid = 'allowtalks'+str(n)
    return aptid

doctor = "Dr. ALINA"
def appointed_patient(patient_number,appointment_id):
    account_sid = 'AC2affb3fcd424dbfa4a44940a42ef5b9b'
    auth_token = 'd3e0847eefff6dce5ddf23639c45c2e0'
    client = Client(account_sid, auth_token)

    customer_number_='+91'+str(patient_number)
    message = client.messages.create(
        body=' is your Appointment ID.\nDoctor Name:'+str(doctor),
        from_= '+91 7011101001',
        to=patient_number)
    return