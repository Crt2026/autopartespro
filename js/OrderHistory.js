// src/components/OrderHistory.js
const OrderHistory = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    const fetchOrders = async () => {
      const user = auth.currentUser;
      if (!user) return;

      const snapshot = await db.collection('orders')
        .where('userId', '==', user.uid)
        .orderBy('createdAt', 'desc')
        .get();

      setOrders(snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() })));
    };

    fetchOrders();
  }, []);

  return (
    <div className="container mx-auto px-4 py-8">
      <h2 className="text-2xl font-bold mb-6">Tus Pedidos</h2>
      {orders.map(order => (
        <div key={order.id} className="bg-white p-4 mb-4 rounded-lg shadow">
          <p>Orden #: {order.id}</p>
          <p>Total: ${order.total.toLocaleString('es-CL')}</p>
        </div>
      ))}
    </div>
  );
};