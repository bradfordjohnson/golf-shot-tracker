import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Shots from './pages/Shots';
import Clubs from './pages/Clubs';

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/clubs" element={<Clubs />} />
          <Route path="/shots" element={<Shots />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
