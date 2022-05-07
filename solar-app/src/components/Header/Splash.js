import React from 'react';

import './Header.styles.css';

import favicon from '../../assets/img/favicon.png'

const Header = () => {
    return (
        <header className='header'>
            <div className='title'>
                <img src={favicon} alt='logo' className='logo' />
                <h1 className='title_text'>Solar App</h1>
            </div>
            <h2>by Hazem Ammar and Richmond Tran</h2>
            <h3>APIC Energy Hackathon 2022</h3>
        </header>
    );
}
export default Header;