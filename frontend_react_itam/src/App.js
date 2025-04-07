import React from 'react';
import { Routes, Route } from 'react-router-dom'; // Убрали BrowserRouter
import LogInPage from './pages/LogIn/LogInPage';
import './App.css'

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="*" element={<LogInPage />} />
      </Routes>
    </div>
  );
}

export default App;