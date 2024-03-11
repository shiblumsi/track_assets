import React from "react";
import { Link } from "react-router-dom";

function SideNav() {
  return (
    <div className="SideNav">
      <ul>
        <li>
          <Link to="/employ">Employ</Link>
        </li>
        <li>
          <Link to="/device">Device</Link>
        </li>
        <li>
          <Link to="/checkout">Checkout</Link>
        </li>
      </ul>
    </div>
  );
}

export default SideNav;
