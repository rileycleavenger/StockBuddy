import React, {useState} from 'react';
import Nav from '../components/Nav/Nav';
import styles from './StockBuddyHomePage.module.css';


const filters = Array.from({ length: 8 }, (_, i) => `Filter ${i + 1}`);

const StockBuddyHomePage: React.FC = () => {


/* Filter color change and labels handling: */
const [clicked, setClicked] = useState<boolean[]>(Array(filters.length).fill(false));

const handleFilterClick = (index: number) => {
    setClicked(prevState => {
        const newClicked = [...prevState];
        newClicked[index] = !newClicked[index];
        return newClicked;
    });
};


    /* Switch movement handling: */
    const [isRightAligned, setIsRightAligned] = useState(true);

    const toggleSwitch = () => {
      setIsRightAligned(!isRightAligned);
    };

    return (
      <div className={styles.body}>
        <Nav />

        <div className={styles.content}>

          <div className={styles.main}>
            <div className={styles.leftColumn}>
              <div className = {styles.switch} 
              style={{
                justifyContent: isRightAligned ? 'flex-end' : 'flex-start',
              }}              
              >
              <div className = {styles.switchButton} onClick={toggleSwitch}>
                <p>Click me</p>
              </div>
              </div>


            <div className={styles.filterContainer}>
            {filters.map((filter, index) => (
                  <div
                    key={index}
                    className={`${styles.filter} ${clicked[index] ? styles.clicked : ''}`}
                    onClick={() => handleFilterClick(index)}
                  > {/* Replace with your icon */}
                    {filter}
                  </div>
                ))}

    
        </div>
        </div>

        <div className={styles.rightColumn}>
        <div className = {styles.contentBox}></div>

        <div className = {styles.redButtonRow}>
        <div className = {styles.generateButton}>
          <p>Generate</p>
        </div>
        <div className = {styles.saveResultsButton}>
          <p>Save Results</p>
        </div>
        </div>

        

          </div>
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