import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { BrowserRouter } from 'react-router-dom';

/**
 * renders root
 */
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);























// import React from "react";
// import ReactDOM from "react-dom/client";
// import App from "./App";
// import "./index.css";
// import { BrowserRouter } from "react-router-dom";
// import { initializeApp } from "firebase/app";
// import { getAnalytics } from "firebase/analytics";
// import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
// import { signOut } from "firebase/auth";

// const firebaseConfig = {
//   apiKey: "AIzaSyD48KcKMMV5oiuXyDqXNcLyXDPBxPLQWNc",
//   authDomain: "tabsoncab.firebaseapp.com",
//   databaseURL: "https://tabsoncab-default-rtdb.firebaseio.com",
//   projectId: "tabsoncab",
//   storageBucket: "tabsoncab.appspot.com",
//   messagingSenderId: "106219151643",
//   appId: "1:106219151643:web:63a97ddc592ca5f49df3be",
//   measurementId: "G-FL0BTGX71W"
// };

// const app = initializeApp(firebaseConfig);
// const analytics = getAnalytics(app);

// const provider = new GoogleAuthProvider();

// provider.addScope('https://www.googleapis.com/auth/contacts.readonly');

// const auth = getAuth();
// signInWithPopup(auth, provider)
//   .then((result) => {
//     // This gives you a Google Access Token. You can use it to access the Google API.
//     const credential = GoogleAuthProvider.credentialFromResult(result);
//     const token = credential.accessToken;
//     // The signed-in user info.
//     const user = result.user;
//     // ...
//   }).catch((error) => {
//     // Handle Errors here.
//     const errorCode = error.code;
//     const errorMessage = error.message;
//     // The email of the user's account used.
//     const email = error.customData.email;
//     // The AuthCredential type that was used.
//     const credential = GoogleAuthProvider.credentialFromError(error);
//     // ...
//   });

// const authout = getAuth();
// signOut(authout).then(() => {
//   // Sign-out successful.
// }).catch((error) => {
//   // An error happened.
// });

// const root = ReactDOM.createRoot(document.getElementById("root"))
// root.render(
//   <React.StrictMode>
//     <BrowserRouter>
//       <App />
//     </BrowserRouter>
//   </React.StrictMode>
// )