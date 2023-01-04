import pyrebase
import json

"""Script used to compare the most recently scraped data with past data in firebase, pushing the crn's of courses
whose registration status has 'opened up' to the 'opened up courses' node."""

firebaseConfig = {
        "apiKey": "AIzaSyD48KcKMMV5oiuXyDqXNcLyXDPBxPLQWNc",
        "authDomain": "tabsoncab.firebaseapp.com",
        "databaseURL": "https://tabsoncab-default-rtdb.firebaseio.com",
        "storageBucket": "tabsoncab.appspot.com",
        "serviceAccount": "/Users/irischeng/Documents/CS32/term-project-icheng3-ngramaj1-ssokolow-ycruztri/tabsoncab-firebase-adminsdk-21dok-3040407482.json",
    };

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def get_past_data() -> dict:
    """Retrieves the firebase data to be updated."""
    past_courses = db.child("iris courses").get().val()
    past_courses = json.loads(json.dumps(past_courses))
    return past_courses

def get_most_recent_data() -> dict:
    """Retrives data from firebase corresponding to the most recently scraped data."""
    curr_courses = db.child("scraped courses").get().val()
    curr_courses = json.loads(json.dumps(curr_courses))
    return curr_courses

def compare_data(past_data:dict, curr_data:dict):
    """Compares the hashmaps of the past and current data, returning a dictionary of
    crn course keys and inner dictionary values containing the fields to be updated for said course."""
    diff_dict = {}
    for k, v in past_data.items():
        crn = k
        inner_value = v
        if crn in curr_data:
            for inner_k, inner_v in inner_value.items():
                first_diff = True 
                if curr_data[k][inner_k] != inner_v and first_diff:
                    if first_diff:
                        diff_dict[crn] = {}
                        diff_dict[crn][inner_k] = curr_data[k][inner_k]
                        first_diff = False
                    else:
                        diff_dict[crn][inner_k] = curr_data[k][inner_k]
    for k, v in curr_data.items():
        if k not in past_data: #accounts for the case of courses being added
            diff_dict[k] = v
    print(diff_dict)
    return diff_dict

courses_opened_up = {"fake class":True} #provides a default value for the 'opened up courses' node
# if not provided, node will not exist in firebase

def rewrite_past_data():
    """Based on differences between the current and past data, updates the past data, additionally
    populates the dictionary keeping track of courses that have opened up."""
    diff_dict = compare_data(get_past_data(), get_most_recent_data())
    for k, v in diff_dict.items():
        db.child("iris courses").child(k).update(v)
        for innerk, innerv in v.items():
            if innerk == 'enrollment status' and innerv == True:
                courses_opened_up[k] = True

def node_by_code_and_name():
    # past_data = get_past_data()
    curr_data = get_most_recent_data()
    # curr_courses = get_most_recent_data(past_data, curr_data)
    new_dict = {}
    for k, v in curr_data.items():
        new_inner_dict = v
        new_inner_dict['crn'] = k
        code = new_inner_dict.pop('code', '')
        new_dict[code] = new_inner_dict
    db.child('courses by code').set(new_dict)


node_by_code_and_name()
db.child("opened up courses").set(courses_opened_up) # sets the new value of 'opened up courses' to be reflective
# of the courses that have most recently had availability in registration spots.
rewrite_past_data()
print('updated!')
