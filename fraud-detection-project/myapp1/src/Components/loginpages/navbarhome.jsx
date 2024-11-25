// SideBar.jsx

import React from 'react';
import { Link } from 'react-router-dom';
import { Layout, Menu, Button } from 'antd';
import { PoweroffOutlined } from '@ant-design/icons';
import './navbarhome.css';

const { Sider } = Layout;

const SideBar = () => {
  const getUserRole = () => {
    return localStorage.getItem('userRole');
  };

  const userRole = getUserRole();

  const handleLogout = () => {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('userRole');
    window.location.href = '/login';
  };

  return (
    <Sider
      className="sidebar"
      width={250}
      style={{
        background: 'linear-gradient(to bottom right, #ff6666, #e74c3c)',
        boxShadow: '0px 2px 10px rgba(0, 0, 0, 0.2)',
        height: '100vh',
        position: 'fixed',
        left: 0,
        zIndex: 1000,
        paddingTop: 30,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <div style={{ marginTop: '50px', width: '100%' }}>
        <Menu
          theme="dark"
          mode="inline"
          defaultSelectedKeys={['1']}
          style={{
            textAlign: 'center',
            width: '100%',
            background: 'transparent',
            border: 'none',
          }}
          selectedKeys={[]}
        >
          <Menu.Item key="1" style={{ marginBottom: '20px', padding: '0' }}>
            <Link to="/dashboard" style={{ color: '#fff', fontSize: '25px' }}>Tableau de bord</Link>
          </Menu.Item>
          {userRole === 'admin' && (
            <Menu.Item key="3" style={{ marginBottom: '20px', padding: '0' }}>
              <Link to="/listuser" style={{ color: '#fff', fontSize: '18px' }}>Gestion de compte</Link>
            </Menu.Item>
          )}
        </Menu>
      </div>
      <div className="logout-button" style={{ marginTop: 'auto', marginBottom: '20px', width: '80%' }}>
        <Button
          type="primary"
          danger
          icon={<PoweroffOutlined />}
          onClick={handleLogout}
          block
          style={{
            height: '40px',
            fontSize: '14px',
            borderRadius: '20px',
            background: 'linear-gradient(to bottom right, #ff6666, #e74c3c)',
            color: '#fff',
            border: 'none',
          }}
        >
          Déconnexion
        </Button>
      </div>
    </Sider>
  );
};

export default SideBar;
