import unittest
from main.python.cabscraper.scripts.firebase.firebase_script import *

class TestFirebaseScript(unittest.TestCase):
    
    def test_compare_data(self):
        ex_past_data1 = {"27362": 
        {"code": "AFRI 0130", "name": "This is America: Reimagining the American Saga",
         "instructor": "M. Scott", "time": "M 3-5:30p",
          "enrollment status": True},
           "26081": {"code": "AFRI 0610", "name": "Black Student Protest from Jim Crow to the Present",
            "instructor": "M. Guterl", "time": "TTh 9-10:20a",
             "enrollment status": True}}
        ex_curr_data1 = ex_past_data1
        
        ex_past_data2 = ex_past_data1
        ex_curr_data2 = ex_curr_data1
        ex_curr_data2['27362']['enrollment status'] = False
        ex_curr_data2['26081']['time'] = "TTh 10:30-11:50a"
        ex_curr_data2['26081']['enrollment status'] = False
        
        ex_past_data3 = ex_past_data1
        ex_past_data3.pop('27362')
        ex_curr_data3 = ex_curr_data1
        ex_curr_data3.pop('26081')

        self.assertEqual(compare_data({}, {}), {})
        self.assertEqual(compare_data(ex_past_data1, ex_curr_data1), {})
        self.assertEqual(compare_data(ex_past_data2, ex_curr_data2), 
        {"27362": {"enrollment status": False},
            "26081": {"time": "TTh 10:30-11:50a",
                "enrollment status": False}})
        self.assertEqual(compare_data(ex_past_data3, ex_curr_data3), 
        {"27362": {"code": "AFRI 0130", "name": "This is America: Reimagining the American Saga",
         "instructor": "M. Scott", "time": "M 3-5:30p",
          "enrollment status": True}})