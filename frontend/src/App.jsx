import React from 'react'
import './App.css'
import ButtonMain from './components/atoms/ButtonMain/ButtonMain.jsx';
import UserButton from './components/atoms/UserButton/UserButton.jsx';
import AdminHeader from './components/atoms/Header/Header.jsx';

function App() {

  return (
    <div>
      {/* <ButtonMain width="331px" 
                iconAfter="/assets/arrowRight.svg"
                iconAfterWidth="18px"
                iconAfterHeight="11px"> Далее </ButtonMain> */}
      <UserButton/>
      <AdminHeader/>
    </div>

  );
}

export default App
