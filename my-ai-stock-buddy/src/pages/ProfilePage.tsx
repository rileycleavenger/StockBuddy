import React, { useState } from 'react';
import Nav from '../components/Nav/Nav';
import styled from 'styled-components';

const ProfileContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  height: 100vh;
  overflow: hidden;
`;

const MainContent = styled.div`
  display: flex;
  gap: 20px;
  margin-top: 20px;
  width: 100%;
  height: calc(100vh - 100px);
`;

const Sidebar = styled.div`
  flex: 1;
  background-color: #2c2c2c;
  color: white;
  padding: 20px;
  border-radius: 10px;
  height: 100%;
`;

const Portfolio = styled.div`
  flex: 1;
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  height: 100%; /* Ensure full height */
  overflow-y: auto;
  position: relative;
`;

const PortfolioHeader = styled.div`
  background-color: white;
  padding: 10px;
  position: sticky;
  top: 0;
  z-index: 1;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
`;

const ProfileHeader = styled.div`
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
`;

const ProfileImage = styled.div`
  width: 50px;
  height: 50px;
  background-color: red;
  border-radius: 50%;
`;

const ProfileName = styled.h2`
  margin: 0;
`;

const Suggestions = styled.div`
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
  height: calc(100% - 70px);
`;

const ToggleContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
`;

const ToggleLabel = styled.h3`
  margin: 0;
  flex-grow: 1;
`;

const ToggleButton = styled.div<{ isActive: boolean }>`
  width: 50px;
  height: 25px;
  background-color: ${props => (props.isActive ? '#4caf50' : '#ccc')};
  border-radius: 15px;
  position: relative;
  cursor: pointer;
  margin-left: 10px;
  transition: background-color 0.3s;
  flex-shrink: 0;
`;

const ToggleCircle = styled.div<{ isActive: boolean }>`
  width: 20px;
  height: 20px;
  background-color: white;
  border-radius: 50%;
  position: absolute;
  top: 2.5px;
  left: ${props => (props.isActive ? '27px' : '2px')};
  transition: left 0.3s;
`;

const SuggestionItemContainer = styled.div`
  flex-grow: 1;
  overflow-y: auto;
`;

const SuggestionItem = styled.div`
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  padding: 10px;
  background-color: #3c3c3c;
  border-radius: 5px;
`;

const PortfolioItemContainer = styled.div`
  max-height: calc(100% - 40px);
  overflow-y: auto;
`;

const PortfolioItem = styled.div`
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
`;

const Graph = styled.div`
  width: 45%;
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  height: 100%;
  overflow: hidden;
`;

const Iframe = styled.iframe`
  width: 100%;
  height: 100%;
  border: none;
`;

const ProfilePage: React.FC = () => {
  const [isPurchase, setIsPurchase] = useState(false);

  const toggleSuggestions = () => {
    setIsPurchase(prev => !prev);
  };

  const purchaseSuggestions = [...Array(10)].map((_, index) => (
    <SuggestionItem key={index}>
      <span>02/21</span>
      <span>Purchase Suggestion</span>
    </SuggestionItem>
  ));

  const sellSuggestions = [...Array(10)].map((_, index) => (
    <SuggestionItem key={index}>
      <span>10/30</span>
      <span>Sell Suggestion</span>
    </SuggestionItem>
  ));

  return (
    <>
      <Nav />
      <ProfileContainer>
        <MainContent>
          <Sidebar>
            <ProfileHeader>
              <ProfileImage />
              <ProfileName>USERNAME</ProfileName>
            </ProfileHeader>
            <Suggestions>
              <ToggleContainer>
                <ToggleLabel>{isPurchase ? 'Saved Purchase Suggestions' : 'Saved Sell Suggestions'}</ToggleLabel>
                <ToggleButton isActive={isPurchase} onClick={toggleSuggestions}>
                  <ToggleCircle isActive={isPurchase} />
                </ToggleButton>
              </ToggleContainer>
              <SuggestionItemContainer>
                {isPurchase ? purchaseSuggestions : sellSuggestions}
              </SuggestionItemContainer>
            </Suggestions>
          </Sidebar>
          <Portfolio>
            <PortfolioHeader>Portfolio</PortfolioHeader>
            <PortfolioItemContainer>
              {[...Array(20)].map((_, index) => (
                <PortfolioItem key={index}>
                  <span>Stock {index + 1}</span>
                  <span>+0.00{index + 1}</span>
                </PortfolioItem>
              ))}
            </PortfolioItemContainer>
          </Portfolio>
          <Graph>
            <Iframe 
              src="https://www.nyse.com/index" 
              title="NYSE"
            />
          </Graph>
        </MainContent>
      </ProfileContainer>
    </>
  );
};

export default ProfilePage;