import React from 'react';
import Nav from '../components/Nav/Nav';
import { Link } from 'react-router-dom';

const LoginPage: React.FC = () => {  
    return (
      <>
        <Nav />
        <div className="login-container">
          <div className="login-box">
            <h1 className="login-title">Login</h1>
            <form className="login-form">
              <div className="form-group">
                <label htmlFor="email">Enter Email</label>
                <input type="email" id="email" name="email" placeholder="email@domain.com" required />
              </div>
              <div className="form-group">
                <label htmlFor="password">Enter Password</label>
                <input type="password" id="password" name="password" placeholder="●●●●●●●●" required />
                <a href="/forgot-password" className="forgot-password">Forgot your password?</a>
              </div>
              <button type="submit" className="login-button">Login</button>
            </form>
            <div className="create-account">
              <p>Create an account</p>
            </div>
            <Link to="/signup" className="signup-button">Sign Up</Link>
          </div>
        </div>
      </>
    );
  }


export default LoginPage;