const express = require('express');
const MercadoPago = require('mercadopago');
const app = express();

// Configura tu Access Token
MercadoPago.configurations.setAccessToken('APP_USR-3958451180314489-071617-1c2f487d4246a0a9f112915dbe7c6542-343776998');

app.use(express.json());

// Endpoint para crear una preferencia de pago
app.post('/create-preference', (req, res) => {
    const { cartItems, userEmail } = req.body; // Asegúrate de recibir los productos y el correo del usuario

    const preference = {
        items: cartItems.map(item => ({
            title: item.name,
            unit_price: item.price,
            quantity: item.quantity,
            currency_id: 'CLP',
        })),
        payer: {
            email: userEmail,
        },
        back_urls: {
            success: "https://tusitio.com/pago-exitoso",
            failure: "https://tusitio.com/pago-fallido",
            pending: "https://tusitio.com/pago-pendiente",
        },
        auto_return: 'approved',
    };

    MercadoPago.preferences.create(preference)
        .then(response => {
            const preferenceId = response.body.id;
            res.status(200).json({ preferenceId });
        })
        .catch(error => {
            console.error('Error creando preferencia de pago:', error);
            res.status(500).send('Error al crear preferencia');
        });
});

// Escucha el puerto
app.listen(3000, () => console.log('Servidor en puerto 3000'));
