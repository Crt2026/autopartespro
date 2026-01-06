const express = require('express');
const cors = require('cors');
const { MercadoPagoConfig, Preference } = require('mercadopago');

const app = express();
const port = 3001;

// --- CONFIGURACIÓN DE MERCADO PAGO ---
const client = new MercadoPagoConfig({
    accessToken: "APP_USR-4187617697526848-100820-a4cc82ec1b7a7f2a0525f1bc6c20d66f-2914738060"
});

// --- CONFIGURACIÓN DEL SERVIDOR ---
app.use(cors());
app.use(express.json());

// --- ENDPOINT PARA CREAR LA PREFERENCIA DE PAGO ---
app.post('/create_preference', async (req, res) => {
    const { items, payer, back_urls, auto_return } = req.body;

    // Validación básica para evitar errores 400
    if (!items || !Array.isArray(items) || items.length === 0) {
        return res.status(400).json({ error: 'El carrito está vacío o mal formado.' });
    }

    const preferenceRequest = {
        items: items.map(item => ({
            title: String(item.title).substring(0, 255),
            description: String(item.description || '').substring(0, 255),
            quantity: Number(item.quantity),
            unit_price: Number(item.unit_price),
            currency_id: item.currency_id || 'CLP'
        })),
        payer: payer,
        back_urls: back_urls,
        auto_return: auto_return,
        external_reference: `orden-${Date.now()}`
    };

    try {
        const preference = new Preference(client);
        const response = await preference.create(preferenceRequest);
        res.status(200).json({ id: response.id });
    } catch (error) {
        console.error('Error al crear preferencia:', error);
        res.status(500).json({ error: 'Error interno al procesar el pago.' });
    }
});

// Ruta de prueba para evitar "Cannot GET /"
app.get('/', (req, res) => {
    res.send('✅ Servidor de Mercado Pago activo. Usa POST /create_preference.');
});

app.listen(port, () => {
    console.log(`✅ Servidor corriendo en http://localhost:${port}`);
});