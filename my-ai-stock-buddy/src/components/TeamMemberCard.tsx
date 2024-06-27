import React from 'react';
import { TeamMember } from '../teamData';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGithub } from '@fortawesome/free-brands-svg-icons';
import { faLinkedin} from '@fortawesome/free-brands-svg-icons';


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
        <a href={member.linkedin} target="_blank" rel="noopener noreferrer"><FontAwesomeIcon icon={faLinkedin} size="2x" /></a>
        <a href={member.github} target="_blank" rel="noopener noreferrer"><FontAwesomeIcon icon={faGithub} size="2x" /></a>
      </div>
    </div>
  );
};

export default TeamMemberCard;