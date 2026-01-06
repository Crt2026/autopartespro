import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyAIQR_CZrsp9IQyM8uS_Etrcyjs4yv-7F8",
  authDomain: "autopartes-pro.firebaseapp.com",
  projectId: "autopartes-pro",
  storageBucket: "autopartes-pro.firebasestorage.app",
  messagingSenderId: "716724882226",
  appId: "1:716724882226:web:408d6fc203df36cfb9652b"
};

// Inicializa Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export { auth };

