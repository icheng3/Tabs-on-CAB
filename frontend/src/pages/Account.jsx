import React from 'react';
import { UserAuth } from '../context/AuthContext';
import { Link } from 'react-router-dom';
import NavBar from './NavBar';

// implements authentication on account page

/**
 * 
 * @returns basic webapp components for account page (handles onClick)
 */
const Account = () => {
  const { logOut, user } = UserAuth();

  const handleSignOut = async () => {
    try {
      await logOut();
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className='w-[300px] m-auto'>
      <div className="NavBar">
        <NavBar></NavBar>
        <div>
        <h1 className='text-center text-2xl font-bold pt-12'>Account</h1>
        <p>Welcome, {user?.displayName}</p>
      </div>
      <button onClick={handleSignOut} className='border py-2 px-5 mt-10'></button>
      </div>
    </div>
  )
}

export default Account;
