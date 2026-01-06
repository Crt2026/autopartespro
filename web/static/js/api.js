// Ejemplo con Node.js/Express
const mercadopago = require('mercadopago');

mercadopago.configure({
  access_token: 'TU_ACCESS_TOKEN'
});

app.post('/api/create_preference', async (req, res) => {
  try {
    const preference = await mercadopago.preferences.create(req.body);
    res.json({ id: preference.body.id });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.post('/api/webhook', (req, res) => {
  // Procesa notificaciones de pago
  console.log('Webhook recibido:', req.body);
  res.status(200).send('OK');
});