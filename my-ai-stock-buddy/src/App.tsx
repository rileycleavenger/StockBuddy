import React, {FC} from 'react';
import Nav from './components/Nav/Nav';

import {BrowserRouter, Routes, Route } from 'react-router-dom';
import AboutPage from './pages/AboutPage';
import LoginPage from './pages/LoginPage';
import ProfilePage from './pages/ProfilePage';
import SignUpPage from './pages/SignUpPage';
import StockBuddyHomePage from './pages/StockBuddyHomePage';



function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<StockBuddyHomePage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignUpPage />} />
        <Route path="/profile" element={<ProfilePage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
