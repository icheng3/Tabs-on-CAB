package Courses;

import java.time.LocalTime;

public class Schedule {
    private String days;
    private LocalTime startTime;
    private LocalTime endTime;

    @Override
    public boolean equals(final Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (this.getClass() != obj.getClass())
            return false;
        final Schedule other = (Schedule) obj;
        return (this.days.equals(other.days) && this.startTime.equals(other.startTime) &&
                this.endTime.equals(other.endTime));
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + this.days.hashCode() + this.startTime.hashCode() + this.endTime.hashCode();
        return result;
    }
}