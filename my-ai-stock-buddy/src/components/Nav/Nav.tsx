import React, {FC} from 'react';
import styles from './Nav.module.css';




const Nav: FC = () => {
    return (
        <nav className={styles.navbar}>

            <div className={styles['logo-container']}>
                <a href='https://www.websiteName.com'>Logo??</a>
            </div>

            <div className={styles['links-container']}>


                <div className={styles['About']}>
                <a href='/about'>About</a>
                </div>

                <div className={styles['Login']}>
                    <a href='/login'>Login</a>
                </div>

                <div className={styles['SignUp']}>
                    <a href='/signup'>Sign Up</a>
                </div>

                <div className={styles['Profile']}>
                    <a href='/profile'>Profile</a>
                </div>


            </div>
        </nav>
    );
}

export default Nav;