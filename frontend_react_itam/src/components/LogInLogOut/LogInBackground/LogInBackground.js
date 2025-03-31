import React from 'react';
import './LogInBackground.css';

const LogInBackground = ({SectionHeight}) => {
    return (
        <main>
            <header className='HeaderOut'>
                <div className="optionOut">
                    <div><h5 className='InOutText'>Вход</h5></div>

                </div>
                <div className="optionOut activeOut">
                    <div ><h5 className='InOutText'>Регистрация</h5></div>
                </div>
            </header>
            <section className='SectionOut' style={{ height: SectionHeight }}></section>
        </main>
    );
};

export default LogInBackground;