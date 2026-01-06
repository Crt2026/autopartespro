// backend/server.js
const express = require('express');
const cors = require('cors');
// const axios = require('axios');
const { MercadoPagoConfig, Preference } = require('mercadopago');

const app = express();
app.use(cors());
app.options('*', cors()); // Manejar preflight OPTIONS
app.use(express.json());

// Headers CORS adicionales para asegurar compatibilidad
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization');
    if (req.method === 'OPTIONS') {
        res.sendStatus(200);
    } else {
        next();
    }
});

// Configurar Mercado Pago
const client = new MercadoPagoConfig({ accessToken: "APP_USR-3958451180314489-071617-1c2f487d4246a0a9f112915dbe7c6542-343776998" });
const preference = new Preference(client);

// Almacenamiento simple de órdenes (usa una DB en producción)
let orders = [];

// Ruta para crear preferencia de pago
app.post('/api/create-preference', async (req, res) => {
    console.log('Recibida solicitud de preferencia:', req.body);
    const { items, payer } = req.body;

    const body = {
        items: items.map(item => ({
            title: item.title,
            unit_price: Number(item.unit_price),
            quantity: Number(item.quantity),
            currency_id: item.currency_id
        })),
        payer: {
            email: payer.email,
            name: payer.first_name,
            surname: payer.last_name
        },
        back_urls: {
            success: "http://localhost:8000/pago-exitoso",
            failure: "http://localhost:8000/pago-fallido",
            pending: "http://localhost:8000/pago-pendiente"
        },
        auto_return: "all",
        notification_url: "http://localhost:3002/api/webhook" // Webhook para seguimiento
    };

    try {
        console.log('Creando preferencia con items:', items);
        const response = await preference.create({ body });
        console.log('Respuesta de Mercado Pago:', response);

        // Guardar orden temporalmente
        const orderId = Date.now();
        orders.push({
            id: orderId,
            items,
            total: items.reduce((sum, item) => sum + (item.unit_price * item.quantity), 0),
            email: payer.email,
            status: 'pendiente',
            mp_preference_id: response.id,
            createdAt: new Date()
        });

        res.json({ id: response.id });
    } catch (error) {
        console.error('Error creando preferencia:', error.response?.data || error.message);
        res.status(500).json({ error: 'No se pudo crear el pago' });
    }
});

// Webhook: Recibe notificaciones de Mercado Pago
app.post('/api/webhook', async (req, res) => {
    const { type, data } = req.body;

    if (type === 'payment') {
        // Comentado temporalmente para evitar errores con axios
        /*
        try {
            const payment = await axios.get(`https://api.mercadopago.com/v1/payments/${data.id}`, {
                headers: {
                    'Authorization': 'Bearer TEST-8878346678387368-071818-719929487982946-736907538'
                }
            });

            const mpPreferenceId = payment.data.external_reference;
            const order = orders.find(o => o.mp_preference_id === mpPreferenceId);

            if (order) {
                order.status = payment.data.status; // approved, rejected, pending
                order.mp_payment_id = payment.data.id;
                order.mp_status_detail = payment.data.status_detail;

                // Aquí puedes enviar un correo al cliente
                console.log(`Pedido ${order.id} actualizado: ${order.status}`);
            }
        } catch (err) {
            console.error('Error en webhook:', err.message);
        }
        */
    }

    res.status(200).send('OK');
});

// Ruta para ver órdenes (para seguimiento)
app.get('/api/orders', (req, res) => {
    res.json(orders);
});

app.listen(3002, () => {
    console.log('Servidor corriendo en http://localhost:3002');
});