// An index to track Ada's memberships
{
  "courses": {
    "ENGL": { // crn for a given course, i'm just not sure whether or not 
    // to structure as individual crn keys or departments with inner dictionaries ...
      "12345": {
        "time": "MW 1-3:30p",
        "instructor": "D. Ritchie",
        "name": "Intro English",
        "code": "ENGL 0110",
        "enrollment": false
      }
    },
    "AFRI": {
      "56789": {
        ...
      }
    }
  }, // end of courses
  "users": {
    "user001": {
      "name": "Iris",
      "contact email": "some@email.com",
      "phone number": 4802873802,
      "tracking": {
        "12345": true,
      }
    },
    ...
  }
  "tracking": {
    "12345": {
      "user001": true, // or can store something else here
    }
  }
}