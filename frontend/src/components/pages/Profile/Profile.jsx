import React from 'react'
import './Profile.css';
import PropTypes from 'prop-types'

function Profile() {
    return (
        <div className='personalAccountBackGround'>
        <div className="personalAccount">
            <img 
                    className='arrow-above-input' 
                    alt='Arrow' 
                    src='/assets/arrowLeft.svg' 
            />
            <div className='MainUserInfoBlock'>
              <div className='userPhoto'></div> 
              <div className='nameAndMail'>
                <div className='accounPhoto'>{/* <img alt='usersPhoto' className='accounPhoto_photo'></img> */}</div>
                <div className='MainInfotmation'>
                  <div className='NameLastName'>
                    <h2 className='NameLastName_Text'>Никита</h2> 
                    <h2 className='NameLastName_Text'>Попов</h2>
                  </div>
                  <h4 className='MainInformation_mail h4NormsPro'>exxample@email.com</h4>
                </div>      
                </div>
            </div>
            <div className='FieldsUserInformation'>
              <div className='FieldsUserInformation_fields'>
                <div className='labelUnderInput'>
                  <p className='labelP'>Имя</p>
                  <input type='text' className='infoFields' required></input>
                </div>
                <div className='labelUnderInput'>
                  <p className='labelP'>Фамилия</p>
                  <input type='text' className='infoFields' required></input>
                </div>
                <div className='labelUnderInput'>
                  <p className='labelP'>Email</p>
                  <input readonly type='email' className='infoFields' required></input>
                </div>
                <div className='labelUnderInput'>
                  <p className='labelP'>Номер телефона</p>
                  <input type='tel' className='infoFields' required></input>
                </div>
                <div className='labelUnderInput'>
                  <p className='labelP'>Дата рождения</p>
                  <input type='date' className='infoFields' required></input>
                </div>
                <div className='labelUnderInput'>
                  <p className='labelP'>Группа</p>
                  <input type='text' className='infoFields' required></input>
                </div>
              </div>
              <button type='button' className='saveInformationEdit'>Сохранить изменения</button>
            </div>
        </div>
        </div>
      );
}

Profile.propTypes = {}

export default Profile



