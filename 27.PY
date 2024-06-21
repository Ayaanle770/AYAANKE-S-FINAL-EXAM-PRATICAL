


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

# Get the value of skills
skills = student['skills']

# Check the data type of skills
skills_type = type(skills)

# Print the value of skills and its data type
print(f"The value of skills is: {skills}")
print(f"The data type of skills is: {skills_type}")
