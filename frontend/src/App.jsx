import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import SideNav from "./components/SideNav1"
import MainContent from "./components/MainContent1";
import EmployPage from "./pages/EmployPage";
import DevicePage from "./pages/DevicePage";
import CheckoutPage from "./pages/CheckoutPage";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="App">
        <SideNav />
        <MainContent>
          <Routes>
            <Route path="/" element={<EmployPage />} />
            <Route path="/device" element={<DevicePage />} />
            <Route path="/checkout" element={<CheckoutPage />} />
          </Routes>
        </MainContent>
      </div>
    </Router>
  );
}

export default App;
