import SearchBar from "../components/SearchBar";
import JSONDATA from "../MOCK_DATA";
import getCourses from "../MOCK_DATA";

/**
 * 
 * @returns basic components of find a course page... implements search bar
 */
function FindCourse() {
    return (
        <div>
            <h1 className='text-center text-3xl font-bold py-8'>Find Courses:</h1>
            <div>
                <SearchBar placeholder="Enter a Course Name..." data={getCourses}/>
            </div>
        </div>
    )
}

export default FindCourse