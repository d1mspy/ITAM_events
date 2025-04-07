import React from 'react';
import { Link } from 'react-router-dom';
import './BackgroundLogIn.css';


const BackgroundLogIn = ({children}) => {
    return (
        <main>
            <div className='mainLogIn'>
                <header className='HeaderOutLI'>
                    <div className="optionOutLI activeOutLI">
                        <div><Link to="/login" className='InOutText'>Вход</Link></div>

                    </div>
                    <div className="optionOutLI ">
                        <div ><Link to="/register" className='InOutText'>Регистрация</Link></div>
                    </div>
                </header>
                <section className='SectionOutLI'>{children}</section>
            </div>
        </main>
    );
};

export default BackgroundLogIn;
