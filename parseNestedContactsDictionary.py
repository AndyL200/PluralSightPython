contacts = {
    'number' : 4,
    'students' : [
        {'name' : 'Sarah H', 'email' : 'sarah@example.com'},
        {'name' : 'Bobby Bobbert' , 'email' : 'bob@example.com'},
        {'name' : 'Craig JustCraig', 'email' : 'craig@example.com'}
    ]
}

#only print emails
print('Student Emails')
for student in contacts['students']:
    print(student['email'])