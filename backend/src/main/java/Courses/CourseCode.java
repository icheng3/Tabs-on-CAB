package Courses;

public class CourseCode {
    private String department;
    private Integer code;

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + this.department.hashCode() + this.code.hashCode();
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
        final CourseCode other = (CourseCode) obj;
        return (this.department.equals(other.department) && this.code == other.code);
    }
}