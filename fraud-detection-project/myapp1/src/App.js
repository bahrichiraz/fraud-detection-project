import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Logincopi from './Components/loginpages/logincopier';
import LandingPage1 from './Components/loginpages/landingcopie';
import HomePage from './Components/loginpages/homepage';
import DashboardPage from './Components/loginpages/dhashbord';
import UsersList from './Components/List/UserList';
import SideBar from './Components/loginpages/navbarhome';
import { Layout } from 'antd';
import ForgotPassword from './Components/Mdp/ForgotPassword';
import ResetPassword from './Components/Mdp/ResetPassword';

import './App.css';

const { Content } = Layout;

const App = () => {
  const isAuthenticated = !!localStorage.getItem('accessToken');
  const [selectedMenuItem, setSelectedMenuItem] = useState('1'); // Définissez setSelectedMenuItem comme fonction d'état

  return (
    <Router>
      <Layout style={{ minHeight: '100vh' }}>
        {isAuthenticated && <SideBar setSelectedMenuItem={setSelectedMenuItem} />} {/* Passez setSelectedMenuItem comme prop à SideBar */}
        <Layout style={{ marginLeft: isAuthenticated ? 250 : 0 }}>
          <Content style={{ padding: '20px', backgroundColor: '#fff' }}>
            <Routes>
              <Route path="/" element={<LandingPage1 />} />
              <Route path="/login" element={<Logincopi />} />
              <Route path="/home" element={<DashboardPage />} />
              <Route path="/" element={isAuthenticated ? <HomePage /> : <Navigate to="/login" />} />
              <Route path="/dashboard" element={isAuthenticated ? <DashboardPage /> : <Navigate to="/home" />} />
              <Route path="/listuser" element={<UsersList />} />
              <Route path="/forgot_password" element={<ForgotPassword/>} />
              <Route path="/ResetPassword" element={<ResetPassword/>} />
              </Routes>
          </Content>
        </Layout>
      </Layout>
    </Router>
  );
};

export default App;
