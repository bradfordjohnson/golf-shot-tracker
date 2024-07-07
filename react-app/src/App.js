import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './homePage';
import ClubsPage from './clubsPage';
import Navigation from './navigation';
function App() {
  return (
    <>
    <Router>
      <div>
        <Navigation />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/clubs" element={<ClubsPage />} />
        </Routes>
      </div>
    </Router>
    </>
  );
}

export default App;
