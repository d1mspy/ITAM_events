import React from 'react';
import './ButtonMain.css';

const ButtonMain = ({width, children, iconBefore, iconAfter, iconBeforeWidth, iconBeforeHeight, iconAfterWidth, iconAfterHeight }) => {
    return (
        <div>
            <button type='button' className='ButtonMain'  style={{ width: width }}>{iconBefore && (
                    <img 
                        src={iconBefore} 
                        alt='icon' 
                        style={{
                            width: iconBeforeWidth, 
                            height: iconBeforeHeight, 
                            marginRight: '2px',
                        }} 
                    />
                )}
                {children}
                {iconAfter && (
                    <img 
                        src={iconAfter} 
                        alt='icon' 
                        style={{
                            width: iconAfterWidth, 
                            height: iconAfterHeight,
                            marginLeft: '3px', 
                        }} 
                    />
                )}
            </button>
        </div>
    );
};



export default ButtonMain;