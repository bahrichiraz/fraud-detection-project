import React, { useState } from 'react';
import { Form, Input, Button, message } from 'antd';
import { Container, Row, Col } from 'react-bootstrap';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const ForgotPassword = () => {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);

  const onFinishForgotPassword = async (values) => {
    setLoading(true);
    try {
      await axios.post('http://localhost:5000/forgot_password', values);
      message.success('Un code de vérification a été envoyé à votre adresse e-mail.');
      navigate('/ResetPassword');
    } catch (error) {
      console.error('Error:', error);
      message.error('Une erreur s\'est produite. Veuillez réessayer plus tard.');
    } finally {
      setLoading(false);
    }
  };

  const handleCancel = () => {
    navigate('/login');
  };

  return (
    <div style={{ backgroundColor: '#f0f2f5' }} className="min-vh-100 d-flex align-items-center">
      <Container>
        <Row className="justify-content-center">
          <Col xs={12} md={6}>
            <div className="p-4 bg-white rounded shadow">
              <h2 className="mt-4 mb-3 text-center" style={{ fontFamily: 'Arial, sans-serif', fontSize: '24px', fontWeight: 'bold', color: '#1890ff' }}>
                Réinitialiser le mot de passe
              </h2>
              <br />
              <h4 style={{ fontFamily: 'Arial, sans-serif', fontSize: '16px', fontWeight: 'normal', color: '#333' }}>
                Veuillez entrer votre e-mail pour rechercher votre compte.
              </h4>
              <Form onFinish={onFinishForgotPassword}>
                <Row gutter={16}>
                  <Col span={24}>
                    <Form.Item
                      label="Adresse e-mail"
                      name="email"
                      rules={[{ required: true, message: 'Veuillez saisir votre adresse e-mail' }, { type: 'email', message: 'Format d\'e-mail incorrect' }]}
                    >
                      <Input style={{ borderRadius: '6px' }} />
                    </Form.Item>
                  </Col>
                </Row>
                <Row gutter={16} justify="center">
                  <Col span={12} className="text-center">
                    <Form.Item>
                      <Button type="primary" htmlType="submit" loading={loading} style={{ width: '100%', backgroundColor: '#1890ff', border: 'none' }}>
                        Envoyer le code de vérification
                      </Button>
                    </Form.Item>
                  </Col>
                  <Col span={12} className="text-center">
                    <Form.Item>
                      <Button onClick={handleCancel} style={{ width: '100%', borderColor: '#1890ff', color: '#1890ff', backgroundColor: 'transparent' }}>
                        Annuler
                      </Button>
                    </Form.Item>
                  </Col>
                </Row>
              </Form>
            </div>
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default ForgotPassword;
