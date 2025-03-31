import React from 'react';
import './ButtonMain.css';

const ButtonMain = ({width, text}) => {
    return (
        <div>
            <button className='ButtonMain'  style={{ width: width }}>{text}</button>
        </div>
    );
};



export default ButtonMain;