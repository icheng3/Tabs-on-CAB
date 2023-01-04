import "./styles.css";
import "./index.css";
import { Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Protected from './components/Protected';
import { AuthContextProvider } from './context/AuthContext';
import Account from './pages/Account';
import Home from './pages/Home';
import Signin from './pages/Signin';
import FindCourse from './pages/FindCourse';
import WatchList from './pages/WatchList';

const client_id = "843244371398-bdurmk2fegf8p5kf3fr5sjhb81bjh2i7.apps.googleusercontent.com"

/**
 * 
 * @returns the webapp... main function... contains routing between all pages and main components of the webapp
 */
function App() {
  return (
	  <div>
      <AuthContextProvider>
        <Navbar />
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/signin' element={<Signin />} />
          <Route path='/account' element={<Protected> <Account /> </Protected>}/>
          <Route path='/FindCourse.jsx' element={<FindCourse />} />
          <Route path='/WatchList.jsx' element={<WatchList />} />
        </Routes>
      </AuthContextProvider>
    </div>
  )};

export default App