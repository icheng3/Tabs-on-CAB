# Tabs on Cab

#### Group Members & Contributions
Iris Cheng (icheng3):    
Sophia Sokolowsky (ssokolow):   
Yulianna Cruz-Trinidad (ycruztri): index.js, watchlist.js, implementing Firebase in backend to access data from realtime database. Adding user information, courses to track, sending email notification.   
Nancy Gramajo Reyes (ngramaj1): index.js, watchlist.js, implementing Firebase in backend to access data from realtime database. Adding user information, courses to track, sending email notification. 

## About
Tabs on Cab is inspired by the app Coursicle. We aim to allow users to track seat availabity for capped courses on CAB. A user can add courses they are interested in tracking and will receive an email when a seat has opened up in those courses. 

## Frontend

## Backend
Our backend uses a Firebase realtime database. The backend uses courses, users, and opened up courses nodes in our database. The courses node contains all courses being offered in a given semester. Each course is identifiable by a course number which maps to a course code, enrollment status, instructor, name, and time. The users node contains all user information including name, email, and courses they are tracking. The opened up courses node contains courses that were previously full but now have seat(s) available. The backend works to add users, add courses they want to track, and checks whether a course in a user's watchlist is in the opened up courses node, and if it is, sends an email notification to the user. 

