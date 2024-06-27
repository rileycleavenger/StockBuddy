import React, {FC, useEffect, useState} from 'react';
import styles from './Nav.module.css';
import logo from './images/StockBuddyLogo.png'; // declare the logo
import { Link, useLocation } from 'react-router-dom';



const Nav: FC = () => {
    
    const location = useLocation();
    const [activePage, setActivePage] = useState<string>(location.pathname);
  
    useEffect(() => {
      setActivePage(location.pathname);
    }, [location]);

    return (
        <nav className={styles.navbar}>

            <div className={styles.logoContainer}>
                <Link to='/'><img src={logo}/></Link>
            </div>

            <div className={styles.linksContainer}>


                <div className={activePage === '/' ? styles.active : styles.inactive}>
                    <Link to='/'>Home</Link>
                </div>

                <div className={activePage === '/profile' ? styles.active : styles.inactive}>
                    <Link to='/profile' >User</Link>
                </div>

                <div className={activePage === '/about' ? styles.active : styles.inactive}>
                    <Link to='/about'>About</Link>
                </div>

                <div className={activePage === '/login' ? styles.active : styles.inactive} id={styles.login}>
                    <Link to='/login'>Login</Link>
                </div>


            </div>
        </nav>
    );
}

export default Nav;