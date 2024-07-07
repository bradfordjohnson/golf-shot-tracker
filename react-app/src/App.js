import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './HomePage';
import ClubsPage from './ClubsPage';
import Navigation from './Navigation';
function App() {
  return (
    <Router>
      <div>
        <Navigation />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/clubs" element={<ClubsPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
