import React from 'react';

function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo">
        <span className="logo-icon">
          C
        </span>

        <span>
          CineSense
        </span>
      </div>

      <div className="nav-links">
        <a href="#home">Home</a>
        <a href="#recommendations">Recommendations</a>
        <a href="#about">About</a>
      </div>
    </nav>
  );
}

export default Navbar;