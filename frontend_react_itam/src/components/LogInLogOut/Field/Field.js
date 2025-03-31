import React from 'react';
import './Field.css'


const Field = ({type, placeholder}) => {
    return (
        <div className='FieldInput'>
            <input 
                id="inputField"
                className='field' 
                type={type} 
                placeholder={placeholder} 
                required
            />
            <label htmlFor="inputField" className="labelText">{placeholder}</label>
        </div>
    );
};

export default Field;

