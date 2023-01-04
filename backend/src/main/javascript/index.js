import { initializeApp } from "firebase/app"
import { getDatabase } from "firebase/database"
import { addUI, checkForUpdates, } from "./watchlist.js"


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
const db = getDatabase();  


checkForUpdates(db);
// adding sample user names, emails, and courses they want to watch 
addUI(db, 'Yulianna Cruz-Trinidad', 'yulianna_cruz-trindad@brown.edu', [24643, 24645] ); 
addUI(db, 'Nancy Gramajo', 'nancy_gramajo_reyes@brown.edu', [24644, 24645] ); 
