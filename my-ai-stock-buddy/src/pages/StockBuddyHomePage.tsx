import React from 'react';
import Nav from '../components/Nav/Nav';
import styles from './StockBuddyHomePage.module.css';


const StockBuddyHomePage: React.FC = () => {
    return (
      <div className={styles.body}>
        <Nav />

        <div className={styles.content}>

          <div className={styles.main}>
            <p>This is where the main content goes</p>
          </div>


          <div className={styles.right}> 

            <div className={styles.stocks}>
              <p>This is where the live stocks go</p>
            </div>

            <div className={styles.spacer}></div>

            <div className={styles.notes}>
              <div className={styles.folder}>
                <p>This is where the notes go</p>
              </div>
            </div>

          </div> 


        </div>

      </div>
    );
}

export default StockBuddyHomePage;