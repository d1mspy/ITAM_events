import React from 'react';
import './TextTipsLogInOut.css';


const TextTipsLogInOut = ({type, text}) => {
    if (type === 'Error') {
       return (
            <div className='TextTips'>
                <h5 className='Error'>{text}</h5>
            </div>
        ); 
    } else {
        return (
            <div className='TextTips'>
                <h5 className='BaseText'>{text}</h5>
            </div> 
        )
    }
};

export default TextTipsLogInOut;