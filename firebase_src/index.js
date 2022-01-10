// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyD_ViwI1LS8gwnyduAVlIjPxEv_j9949Gg",
    authDomain: "cab2-4f8d2.firebaseapp.com",
    projectId: "cab2-4f8d2",
    storageBucket: "cab2-4f8d2.appspot.com",
    messagingSenderId: "951663881259",
    appId: "1:951663881259:web:28d76656a60b170104ce6e",
    measurementId: "G-9DX5CM9LFZ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);