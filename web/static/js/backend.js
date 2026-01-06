const express = require('express');
const bodyParser = require('body-parser');
const mercadopago = require('mercadopago');

// Configura MercadoPago con tu access token
mercadopago.configurations.setAccessToken('TU_ACCESS_TOKEN');

const app = express();
app.use(bodyParser.json());

// Endpoint para crear la preferencia de pago
app.post('/api/create-preference', (req, res) => {
    const items = req.body.items;

    // Crear preferencia de pago
    const preference = {
        items: items,
        back_urls: {
            success: 'http://localhost:3000/payment-success',
            failure: 'http://localhost:3000/payment-failure',
            pending: 'http://localhost:3000/payment-pending'
        },
        auto_return: 'approved'
    };

    // Crear la preferencia de pago
    mercadopago.preferences.create(preference)
        .then(function(response) {
            res.json({ id: response.body.id });
        })
        .catch(function(error) {
            console.error('Error al crear la preferencia:', error);
            res.status(500).send('Error al crear la preferencia');
        });
});

app.listen(3000, () => {
    console.log('Servidor en http://localhost:3000');
});
