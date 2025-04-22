import React from 'react';
import { Link } from 'react-router-dom'; 
import './SignUpSecondStep.css';
import FieldsGroup from '../../components/LogInLogOut/FieldsGroup/FieldsGroup';
import ButtonMain from '../../components/ButtonMain/ButtonMain';
import BackgroundSignUp from '../../components/LogInLogOut/BackgroundSignUp/BackgroundSignUp';


const SignUpSecondStep = () => {
    return (
      <div className="login-page">
        <BackgroundSignUp SectionMinHeight="262px">
          <div className="fields-container">
            <div className="input-with-arrow">
              <img 
                className='arrow-above-input' 
                alt='Arrow' 
                src='/assets/arrowRight.svg' 
              />
              <div className="centered-group">
                <FieldsGroup mode="logIn" />
                <ButtonMain width="351px">Зарегистрироваться</ButtonMain>
              </div>
            </div>
          </div>
        </BackgroundSignUp>
      </div>
    );
  };

export default SignUpSecondStep;