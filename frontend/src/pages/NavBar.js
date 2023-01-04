/**
 * 
 * @returns functional navigation bar with links to course page and watchlist page
 */
export default function NavBar() {
    return (
        <nav className = "nav">
            <ul>
                <li>
                    <a href = "/FindCourse.jsx">Find a Course</a>
                </li>
                <li>
                    <a href = "/WatchList.jsx">Your Watchlist</a>
                </li>
            </ul>
        </nav>
    )
}