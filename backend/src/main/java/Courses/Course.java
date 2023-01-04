package Courses;

public class Course {
    private String name;
    private String instructor;
    private String section;
    private CourseCode code;
    private Boolean enrollment;
    private Schedule schedule;
    private Integer crn;

    public boolean checkEnrollmentStatus() {
        return enrollment;
    }
    public boolean OpenedUp(Course currCourse) {
        if ((currCourse.enrollment != this.enrollment) && (currCourse.enrollment)) {
            return true;
        } return false;
    }

    public boolean ClosedUp(Course currCourse) {
        if ((currCourse.enrollment != this.enrollment) && !(currCourse.enrollment)) {
            return true;
        } return false;
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + this.crn;
        return result;
    }

    @Override
    public boolean equals(final Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (this.getClass() != obj.getClass())
            return false;
        final Course other = (Course) obj;
        return (this.crn == other.crn);
    }
}