import React from 'react'
import './App.css'
import UserButton from './components/atoms/UserButton/UserButton.jsx';
import AdminHeader from './components/atoms/Header/Header.jsx';
import Profile from './components/pages/Profile/Profile.jsx';

function App() {

  return (
    <div>
      {/* <ButtonMain width="331px" 
                iconAfter="/assets/arrowRight.svg"
                iconAfterWidth="18px"
                iconAfterHeight="11px"> Далее </ButtonMain> */}
      <UserButton/>
      <AdminHeader/>
      <Profile/>
    </div>

  );
}

export default App
