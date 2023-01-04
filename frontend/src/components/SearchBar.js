import React, {useState} from "react";
import "./SearchBar.css";
import SearchIcon from "@material-ui/icons/Search";
import CloseIcon from "@material-ui/icons/Close";
import "./SearchBar.css";
import { useNavigate } from "react-router-dom";

/**
 * 
 * @param {placeholder, data} params placeholder sets the underscript text in the search bar and data is the
 * data base with all the courses from cab
 * @returns a functional, filtering search bar that filters based on active user input along with a clear all button
 * In addition, when user clicks on a course, it currently routes them to their watchlist... not yet able to transfer
 * the data from the onClick... tried with routing and onClick functions.
 */
function SearchBar({placeholder, data}) {

  const [filteredData, setFilteredData] = useState([]);
  const [wordEntered, setWordEntered] = useState("");

  const handleFilter = (event) => {
    const searchWord = event.target.value
    setWordEntered(searchWord);
    const newFilter = data.filter((value) => {
      return (value.code.toLowerCase().includes(searchWord.toLowerCase())) || 
      (value.name.toLowerCase().includes(searchWord.toLowerCase()));
    });

    if (searchWord === "") {
      setFilteredData([])
    } else {
      setFilteredData(newFilter);
    }
  };

  const clearInput = () => {
    setFilteredData([]);
    setWordEntered("");
  };

  return (
    <div className="search">
      <div className="searchInputs">
        <input type="text" placeholder={placeholder} value={wordEntered} onChange={handleFilter}/>
        <div className="searchIcon">
          {filteredData.length === 0 ? (
            <SearchIcon />
          ) : (
            <CloseIcon id="clearBtn" onClick={clearInput} />
          )}
        </div>
      </div>
      {filteredData.length != 0 && (
        <div className="searchOutput">
          {filteredData.slice(0, 15).map((value, key) => {
            return (
            <a className="dataItem" href="/WatchList.jsx" target="_blank">
              <p>{value.code} : {value.name}</p>
            </a>
          );
        })}
      </div>
      )}
    </div>
  )
}

export default SearchBar