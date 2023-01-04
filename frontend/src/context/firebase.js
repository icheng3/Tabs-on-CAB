// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyD48KcKMMV5oiuXyDqXNcLyXDPBxPLQWNc",
    authDomain: "tabsoncab.firebaseapp.com",
    databaseURL: "https://tabsoncab-default-rtdb.firebaseio.com",
    projectId: "tabsoncab",
    storageBucket: "tabsoncab.appspot.com",
    messagingSenderId: "106219151643",
    appId: "1:106219151643:web:63a97ddc592ca5f49df3be",
    measurementId: "G-FL0BTGX71W"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  export const auth = getAuth(app);