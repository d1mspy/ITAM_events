import React from 'react';
import { Routes, Route } from 'react-router-dom'; 
import LogInPage from './pages/LogIn/LogInPage';
import SignUpFirstStep from './pages/SignUpFirstStep/SignUpFirstStep';
import SignUpSecondStep from './pages/SignUpSecondStep/SignUpSecondStep';
import PersonalAccount from './pages/PersonalAccount/PersonalAccount';
import './App.css'

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="*" element={<PersonalAccount />} />
      </Routes>
    </div>
  );
}

export default App;