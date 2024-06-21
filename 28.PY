

student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis', 'Machine Learning'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St, New York, NY 10001'
}


student['skills'].append('Public Speaking')
student['skills'].append('Project Management')


print(f"The updated skills are: {student['skills']}")
