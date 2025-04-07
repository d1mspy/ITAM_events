import React from 'react';
import { Link } from 'react-router-dom'; // Для будущего роутинга
import './LogInPage.css';
import BackgroundLogIn from '../../components/LogInLogOut/BackgroundLogIn/BackgroundLogIn';
import FieldsGroup from '../../components/LogInLogOut/FieldsGroup/FieldsGroup';
import ButtonMain from '../../components/ButtonMain/ButtonMain';
import BackgroundSignUp from '../../components/LogInLogOut/BackgroundSignUp/BackgroundSignUp';
import TextTipsLogInOut from '../../components/LogInLogOut/TextTipsLogInOut/TextTipsLogInOut';





const LogInPage = () => {
  return (
    <div className="login-page">
      <BackgroundLogIn>
        <div className="fields-container">
          <div className="centered-group">
            <FieldsGroup mode="logIn" />
            <ButtonMain width="351px">Войти</ButtonMain>
          </div>
          <TextTipsLogInOut className="left-aligned-text">Забыли пароль?</TextTipsLogInOut>
        </div>
      </BackgroundLogIn>
    </div>
  );
};

export default LogInPage;