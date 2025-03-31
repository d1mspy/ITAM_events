import React from 'react';
import './FieldsGroup.css';
import Field from '../Field/Field.js';

const FieldsGroup = ({mode}) => {
    if (mode==='logIn') {
        return (
            <div className='Fields'>
                <Field type='email' placeholder='Email'/>
                <Field type='password' placeholder='Пароль'/>
            </div>
        );
    } else {
        return (
            <div className='Fields'>
                <Field className='date' type='date' placeholder='Дата рождения'/>
                <Field type='text' placeholder='Фамилия'/>
                <Field type='text' placeholder='Имя'/>
                <Field type='text' placeholder='Группа'/>
            </div>
        );
    };
};



export default FieldsGroup;