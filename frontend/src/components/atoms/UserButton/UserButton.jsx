import React from 'react';
import './UserButton.css'

const UserButton = () => {
    return (
        <div className="user-button-wrapper"> 
            <div className="button-container">
                <button className='BtnUserButton' type="button" width='100' height='100'></button>
                


                <div class="dropdown-menu notAuth">
                    <div className='dropdown-menu__toAuth'>
                        <img src='/assets/logout.svg'></img>
                        <a class="dropdown-item" href="#">Вход</a>
                    </div>
                </div>

                {/* <div className="dropdown-menu Auth">
                    <div className='dropdown-menu__helpBlockFirst'>
                        <div className='dropdown-menu__helpBlockSecond'>
                            <div className='dropdown-menu__name'>
                                <p>Никита</p>
                                <p>Попов</p>
                            </div>
                            <p className='dropdown-menu__mail'>jdoe@acme.com</p>
                        </div>
                        <div className='dropdown-line'></div>
                    </div>
                    <div className='dropdown-menu__profile'>
                        <img className='dropdown-menu__img' src='/assets/userBold.svg' alt="Профиль" />
                        <a className="dropdown-item" href="#">Профиль</a>
                    </div>
                    <div className='dropdown-menu__exite'>
                        <img className='dropdown-menu__img' src='/assets/logout.svg' alt="Выйти" />
                        <a className="dropdown-item" href="#">Выйти</a>
                    </div>
                </div> */}
            </div>
        </div>
        
    )
}


export default UserButton;