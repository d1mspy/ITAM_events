import './App.css';
import UserButton from './components/UserButton/UserButton';
import Header from './components/Header/Header';
import FieldsGroup from './components/LogInLogOut/FieldsGroup/FieldsGroup';
import ButtonMain from './components/ButtonMain/ButtonMain';
import TextTipsLogInOut from './components/LogInLogOut/TextTipsLogInOut/TextTipsLogInOut';
import LogInBackground from './components/LogInLogOut/LogInBackground/LogInBackground';

function App() {
  return (
    <div className="App">
      <Header />
      <UserButton />
      <FieldsGroup mode='logIn'/>
      <FieldsGroup/>
      
      <ButtonMain width='351px' text='Войти'/>
      <TextTipsLogInOut  text='Забыли пароль?'/>
      <LogInBackground SectionHeight='376px'/>
    </div>
  );
}

export default App;
