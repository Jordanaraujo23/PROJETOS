import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
  apiKey: "AIzaSyAO6azVpX988Vwu___-pp9c0oprqPThMlQ",
  authDomain: "matematica-em-foco.firebaseapp.com",
  projectId: "matematica-em-foco",
  storageBucket: "matematica-em-foco.firebasestorage.app",
  messagingSenderId: "1031540454030",
  appId: "1:1031540454030:web:af79c9407ffc7dfd694fdf",
  measurementId: "G-0TGT0E9YL8"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);