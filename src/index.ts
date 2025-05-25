import express from 'express';
import alumosRoutes from './routes/alumnos';

const app = express();
app.use(express.json());

app.use('/alumnos', alumosRoutes);

app.listen(3000, () => {
  console.log('Serper listening on http://localhost:3000');
});