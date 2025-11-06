import React, {useState, useEffect} from 'react'


function Card(props) {


  return (
    <div className='CardBlock'>
        <div className='CardBlock--upper'>
            <div className='CardBlock--visualPar'>

            </div>
            <div>
                <h3></h3>
                <div>
                    <h6></h6>
                    <div className='CardBlock_verticalLine'></div>
                    <h6></h6>
                    <div className='CardBlock_verticalLine'></div>
                    <h6></h6>
                </div>
            </div>
        </div>


        <div className='CardBlock_arrowBtn'>
            <a href=""></a> //должна открывать карточку события поверх экрана
        </div>
    </div>
  )


}



export default Card
