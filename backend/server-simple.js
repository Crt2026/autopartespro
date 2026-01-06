// backend/server-simple.js
const express = require("express");
const cors = require("cors");
const mercadopago = require("mercadopago");

const app = express();

// CORS (acepta localhost y 127.0.0.1)
app.use(cors({
  origin: ["http://localhost:3000", "http://127.0.0.1:3000"]
}));

app.use(express.json());

// CONFIGURACIÓN CORRECTA
mercadopago.configure({
  access_token: "APP_USR-3958451180314489-071617-1c2f487d4246a0a9f112915dbe7c6542-343776998"
});

// RUTA REAL
app.post("/api/create-preference", (req, res) => {
  const preference = {
    items: req.body.items,
    payer: req.body.payer,
    auto_return: "approved",
    back_urls: {
      success: "http://localhost:3000/#cart?payment=success",
      failure: "http://localhost:3000/#cart?payment=failure",
      pending: "http://localhost:3000/#cart?payment=pending"
    }
  };

  mercadopago.preferences.create(preference).then((result) => {
    res.json({ id: result.body.id });
  }).catch((error) => {
    console.error("❌ Mercado Pago error:", error);
    res.status(500).json({ error: "No se pudo crear la preferencia" });
  });
});

app.listen(3003, (err) => {
  if (err) {
    console.error("Error al iniciar servidor:", err);
  } else {
    console.log("✅ Backend Mercado Pago activo en http://localhost:3003");
  }
});