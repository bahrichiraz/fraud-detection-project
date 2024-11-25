import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Table, Spin, Button, Modal } from 'antd';
import 'antd/dist/reset.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Swal from 'sweetalert2';
import 'sweetalert2/dist/sweetalert2.css';
import SideBar from '../loginpages/navbarhome';

const UsersList = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [disabledUsers, setDisabledUsers] = useState([]);
  const [modalVisible, setModalVisible] = useState(false);

  const fetchUsers = async () => {
    setLoading(true);
    try {
      const response = await axios.get('http://localhost:5000/users');
      setUsers(response.data);
      setLoading(false);
    } catch (error) {
      Swal.fire({
        icon: 'error',
        title: 'Erreur',
        text: `Erreur lors de la récupération des utilisateurs : ${error}`,
      });
      setLoading(false);
    }
  };

  const fetchDisabledUsers = async () => {
    try {
      const response = await axios.get('http://localhost:5000/usersDésactiver');
      setDisabledUsers(response.data);
    } catch (error) {
      Swal.fire({
        icon: 'error',
        title: 'Erreur',
        text: `Erreur lors de la récupération des utilisateurs désactivés : ${error}`,
      });
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const handleDisableUser = async (id) => {
    try {
      await axios.post(`http://localhost:5000/users/${id}/disable`);
      setUsers((prevUsers) =>
        prevUsers.filter((user) => user.id !== id)
      );
      Swal.fire({
        icon: 'success',
        title: 'Succès',
        text: 'Utilisateur désactivé avec succès',
      });
      fetchDisabledUsers();
      fetchUsers()
    } catch (error) {
      Swal.fire({
        icon: 'error',
        title: 'Erreur',
        text: `Erreur lors de la désactivation de l'utilisateur : ${error}`,
      });
    }
  };

  const handleActivateUser = async (id) => {
    try {
      await axios.post(`http://localhost:5000/users/${id}/activate`);
      setDisabledUsers((prevUsers) =>
        prevUsers.filter((user) => user.id !== id)
      );
      Swal.fire({
        icon: 'success',
        title: 'Succès',
        text: 'Utilisateur activé avec succès',
      });
      fetchDisabledUsers();
      fetchUsers();
    } catch (error) {
      Swal.fire({
        icon: 'error',
        title: 'Erreur',
        text: `Erreur lors de l'activation de l'utilisateur : ${error}`,
      });
    }
  };

  const showDisabledUsersModal = async () => {
    await fetchDisabledUsers();
    setModalVisible(true);
  };

  const handleCancel = () => {
    setModalVisible(false);
  };

  const columns = [
    {
      title: 'ID',
      dataIndex: 'id',
      key: 'id',
    },
    {
      title: 'Email',
      dataIndex: 'email',
      key: 'email',
    },
    {
      title: 'Nom',
      dataIndex: 'nom',
      key: 'nom',
    },
    {
      title: 'Prénom',
      dataIndex: 'prenom',
      key: 'prenom',
    },
    {
      title: 'Statut',
      dataIndex: 'status',
      key: 'status',
      render: (text, record) => (
        <span>{record.status}</span>
      ),
    },
    {
      title: 'Action',
      key: 'action',
      render: (text, record) => (
        <div>
          <Button
            type="primary"
            danger
            onClick={() => handleDisableUser(record.id)}
            disabled={record.status === 'désactiver'}
            style={{ marginRight: 8 }}
          >
            {record.status === 'désactiver' ? 'Désactivé' : 'Désactiver'}
          </Button>
          {record.status === 'désactiver' && (
            <Button onClick={() => handleActivateUser(record.id)}>
              Activer
            </Button>
          )}
        </div>
      ),
    },
  ];

  const columnsModal = [
    {
      title: 'ID',
      dataIndex: 'id',
      key: 'id',
    },
    {
      title: 'Email',
      dataIndex: 'email',
      key: 'email',
    },
    {
      title: 'Nom',
      dataIndex: 'nom',
      key: 'nom',
    },
    {
      title: 'Prénom',
      dataIndex: 'prenom',
      key: 'prenom',
    },
    {
      title: 'Action',
      key: 'action',
      render: (text, record) => (
        <Button
          type="primary"
          danger
          onClick={() => handleActivateUser(record.id)}
        >
          Activer
        </Button>
      ),
    },
  ];

  if (loading) {
    return <Spin tip="Chargement..." />;
  }

  return (
    <div className="container mt-5">
      <SideBar />
      <div className="row justify-content-center">
        <div className="col-md-9">
          <h1 style={{ textAlign: 'center', color: 'red' }}>Liste des Utilisateurs</h1>
          <Button
            onClick={showDisabledUsersModal}
            className="mb-3"
            style={{
              backgroundColor: 'grey',
              borderColor: 'grey',
              borderRadius: '0',
              padding: '10px 20px',
              fontWeight: 'bold',
              color: 'white',
            }}
          >
            Utilisateurs désactivés
          </Button>
          <Table columns={columns} dataSource={users} rowKey="id" />
        </div>
      </div>

      <Modal
        title="Utilisateurs Désactivés"
        visible={modalVisible}
        onCancel={handleCancel}
        footer={[
          <Button key="back" onClick={handleCancel}>
            Fermer
          </Button>
        ]}
      >
        <Table columns={columnsModal} dataSource={disabledUsers} rowKey="id" pagination={false} />
      </Modal>
    </div>
  );
};

export default UsersList;
