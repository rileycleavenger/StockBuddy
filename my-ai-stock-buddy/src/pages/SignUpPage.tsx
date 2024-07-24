import React from 'react';
import Nav from '../components/Nav/Nav';
import { Link } from 'react-router-dom';


const SignUpPage: React.FC = () => {
  return (
    <>
      <Nav />
      <div className="signup-container">
      <div className="signup-box">
        <h2 className="signup-title">Create an account</h2>
        <form className="signup-form">
          <div className="form-group-sign">
            <label htmlFor="email">Enter Email</label>
            <input type="email" id="email" name="email" placeholder="email@domain.com" required />
          </div>
          <div className="form-group-sign">
            <label htmlFor="password">Enter Password</label>
            <input type="password" id="password" name="password" placeholder="●●●●●●●●" required />
          </div>
          <div className="form-group-sign">
            <label htmlFor="confirm-password">Confirm Password</label>
            <input type="password" id="confirm-password" name="confirm-password" placeholder="●●●●●●●●" required />
          </div>
          <button type="submit" className="signup-button-sign">Sign up with email</button>
        </form>
        <div className="login-link">
          <span>Already have an account?</span>
        </div>
        <Link to="/login">
          <button className="login-button-sign">Login</button>
        </Link>
      </div>
    </div>
    </>
  );
}


export default SignUpPage;