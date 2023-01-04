package CourseData;
import Courses.Course;
import UserInfo.User;
import com.google.firebase.remoteconfig.User;
import java.util.ArrayList;
import java.util.HashMap;

public class CourseData {
  private HashMap<String, ArrayList<User>> data;
  private HashMap<Course, Boolean> courseStatus;
  private HashMap<String, Course> courseInfo;
  // possibly need to make some overriding hashmap functions
  // but if we're keying in based off certain information NOT including the
  // enrollment status, it should be fine...

  // two hashamps ..? one hashmap has keys of courses and values of a list of users
  // another hashmap has key of course + all relevant info besides enrollment..
  // and then value is true or false based on enrollment...
  // ugh idk how to organize this info
  public void updateData(HashMap<String, Course> newInfo) {
    for (Course course: courses) {
      this.updateCourseInfo(course);
      this.updateCourseStatus(course);
      // first check if course is in the dictionary
      // if not, add it with the correct course status
      // if it is in the dictionary, then compare the two
      // if they are the same,

    }
  }

  public void updateCourseInfo(Course course) {
    if (courseInfo.containsKey(course)) {
      // then do this
    } else {

    }
  }

  public void updateCourseStatus(Course course) {
    if (courseInfo.containsKey(course)) {
      Course oldCourse = courseStatus.get(course);
      boolean currStatus = course.checkEnrollmentStatus();
      if (oldStatus != currStatus) {

      }
    }
  }


}

