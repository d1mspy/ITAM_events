import React from 'react';
import { Link } from 'react-router-dom';
import './BackgroundSignUp.css';

const BackgroundSignUp = ({SectionMinHeight, children}) => {
    return (
        <main >
            <div className='mainLogInSignUP'>
                <header className='HeaderOut'>
                    <div className="optionOut">
                        <div><Link to="/register" className='InOutText'>Вход</Link></div>
                    </div>
                    <div className="optionOut activeOut">
                        <div ><Link to="/register" className='InOutText'>Регистрация</Link></div>
                    </div>
                </header>
                <section className='SectionOut' style={{ minHeight: SectionMinHeight }}>{children}</section>
            </div>
        </main>
    );
};

export default BackgroundSignUp;