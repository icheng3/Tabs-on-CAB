import { onChildAdded, ref, remove, set, onValue} from "firebase/database"
import sgMail from '@sendgrid/mail'

var courseN; 
var crnn;  
var u_email; 
var email_list = [];

// add user info
export function addUI(db, name, email, crn) {
    const userRef = ref(db, 'users/' + name)
      set(userRef, {
          user_email : email, 
          user_crn : crn
      });
}

// remove user info 
function removeUI(db, name, email, crn){
    const userRef = ref(db, 'users/' + email)
    remove(userRef, {
        user_name: name, 
        user_course: course
    });
}

// check that a course that has a seat available is returning true, 
// then go into users node in findStudents()
export function checkForUpdates(db) {
    var courseRef = ref(db, 'opened up courses/');
    onChildAdded(courseRef, (data) => {
        var updatedDataKey = data.key; 
        var updatedDataVal = data.val(); 
        console.log("added node! ")
        findStudents(db, updatedDataKey);
    });
}

// in the users node, checks that the course being passed in is in the user's watchlist, 
// gets the user's email to send an email notification when a seat opens up
function findStudents(db, crn) {
    console.log("finding students ...")
    var userInfoRef = ref (db, 'users');
    onValue(userInfoRef, (snapshot) => {
        snapshot.forEach((childSnapshot) => {
            const childKey = childSnapshot.key; 
            const childVal = childSnapshot.val();
            var grandChildRef = ref(db, 'users/' + childKey);
            onValue(grandChildRef, (gchildSnapshot) => {
                gchildSnapshot.forEach((gcSnapshot) => {
                    const gchildKey = gcSnapshot.key; 
                    const gchildVal = gcSnapshot.val();
                    if (gchildKey == 'user_crn'){
                        for(let i = 0; i < gchildVal.length; i++){
                            if (gchildVal[i].toString() == crn){
                                crnn = crn; 
                            }
                        }
                    }
                    if (gchildKey == 'user_email'){
                        u_email = String(gchildVal); 
                        if (!email_list.includes(u_email)){
                            email_list.push(u_email);
                        }
                        getCourseName(db, crnn, email_list);
                    }
                })
            });
        });
    });  
}

// sets up Send Grid to send a user an email when a seat has opened up on CAB
function notify(emails, crn) {
    sgMail.setApiKey('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'); 
    const msg = {
        to: emails, 
        from: 'tabsoncab@gmail.com',
        subject: 'Spot Available In ' + crn,
        text: 'A spot is now availbe in ' + crn + '. Register for this course on CAB!' + '\n' + 'Best,' + '\n' + 'TabsOnCab Team',
    };
    //sgMail.send(msg);
    console.log("Email sent!")
    removeFromElist(email_list);
}

// gets the course name to include in our email notification
function getCourseName(db, crn, u_email){
    const courseRef = ref(db, 'courses'); 
    onValue(courseRef, (snapshot) => {
        snapshot.forEach((childSnapshot) => {
            const childKey = childSnapshot.key;
            const gChildRef = ref(db, 'courses/' + childKey)
            if (childKey == crn){
                onValue(gChildRef, (gSnapshot) => {
                    gSnapshot.forEach((snapshots) => {
                        const key = snapshots.key;
                        const val = snapshots.val(); 
                        if (key == 'code'){
                            courseN = String(val)
                            notify(u_email, courseN);
                        }
                    });
                });
            }
        });
    });
}

function removeFromElist(email_list) {
    while (email_list.length) { 
        email_list.pop();
        
    }
}