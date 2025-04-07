import React from 'react';
import './TextTipsLogInOut.css';


const TextTipsLogInOut = ({type, children}) => {
    if (type === 'Error') {
       return (
            <div className='TextTips'>
                <h5 className='Error'>{children}</h5>
            </div>
        ); 
    } else {
        return (
            <div className='TextTips'>
                <h5 className='BaseText'>{children}</h5>
            </div> 
        )
    }
};

export default TextTipsLogInOut;