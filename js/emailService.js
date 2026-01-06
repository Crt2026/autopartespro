const registerWithEmail = async (email, password) => {
  try {
    const userCredential = await auth.createUserWithEmailAndPassword(email, password);
    const user = userCredential.user;
    console.log('Usuario registrado:', user);
    // Redirige o muestra el contenido
  } catch (error) {
    console.error('Error al registrar usuario:', error);
  }
};

const loginWithEmail = async (email, password) => {
  try {
    const userCredential = await auth.signInWithEmailAndPassword(email, password);
    const user = userCredential.user;
    console.log('Usuario logueado:', user);
    // Redirige o muestra el contenido
  } catch (error) {
    console.error('Error al iniciar sesión:', error);
  }
};
