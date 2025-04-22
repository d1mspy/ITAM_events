import React from 'react';
import { Link } from 'react-router-dom'; 
import './SignUpFirstStep.css';
import FieldsGroup from '../../components/LogInLogOut/FieldsGroup/FieldsGroup';
import ButtonMain from '../../components/ButtonMain/ButtonMain';
import BackgroundSignUp from '../../components/LogInLogOut/BackgroundSignUp/BackgroundSignUp';





const SignUpFirstStep = () => {
  return (
    <div className="login-page">
      <BackgroundSignUp SectionMinHeight="376px">
        <div className="fields-container">
          <div className="centered-group">
            <FieldsGroup />
            <ButtonMain width="351px" 
                iconAfter="/assets/arrowRight.svg"
                iconAfterWidth="18px"
                iconAfterHeight="11px"> Далее </ButtonMain>
          </div>
        </div>
      </BackgroundSignUp>
    </div>
  );
};

export default SignUpFirstStep;