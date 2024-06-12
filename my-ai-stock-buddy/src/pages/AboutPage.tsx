import React from 'react';
import Nav from '../components/Nav/Nav';
import { teamMembers } from '../teamData';
import TeamMemberCard from '../components/TeamMemberCard';


const AboutPage: React.FC = () => {

    return (
      <>
        <Nav />
        <head>
        </head> 
        <div className='About-Page'>
          <img src = '/images/stockMarketImage.jpg' alt='About Us' className='About-Image'/>
          <h1 className = "About-Header">About Stock Buddy</h1>
          <p className='About-Summary'>Stock Buddy is a comprehensive stock market analysis tool developed by a group of dedicated college students. Our goal is to
            provide users with real-time data, intuitive analytics, and a user-friendly interface to help make informed investment decisions. 
            By combining our diverse skills in software development, and data analysis, we aim to create a platform that simplifies the stock
            market insights and enhances the trading experience for both beginners and experienced investors alike. Explore our project 
            repository to learn more about our work and contributions.
          </p>
          <div className='Team'>
            <h2 className='Team-Header'>Meet the Team</h2>
            <div className="team-members">
              {teamMembers.map(member => (
              <TeamMemberCard key={member.name} member={member} />
              ))}
            </div>
          </div>
        </div>
      </>
    );
  }

export default AboutPage;