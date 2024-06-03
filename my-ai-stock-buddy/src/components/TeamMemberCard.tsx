import React from 'react';
import { TeamMember } from '../teamData';

interface TeamMemberCardProps {
  member: TeamMember;
}

const TeamMemberCard: React.FC<TeamMemberCardProps> = ({ member }) => {
  return (
    <div className="team-member">
      <img src={member.image} alt={member.name} className="team-member-image" />
      <h3>{member.name}</h3>
      <p>{member.role}</p>
      <div className="team-member-links">
        <a href={member.linkedin} target="_blank" rel="noopener noreferrer">LinkedIn</a>
        <a href={member.github} target="_blank" rel="noopener noreferrer">GitHub</a>
      </div>
    </div>
  );
};

export default TeamMemberCard;