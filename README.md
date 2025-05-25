# ACM SERVER

This project provides a backend server built with **Express.js** and **Prisma ORM**, connected to a **PostgreSQL** database. It also includes a `data/` folder with **Python scripts** to generate and insert data into the same database. All configuration is handled via a single `.env` file containing a `DATABASE_URL`.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/acm-server.git
cd acm-server
```

### 2. Configure Environment Variables 
Create a .env file in the root directory:

```
DATABASE_URL=postgresql://user:password@localhost:5432/db_name
```
### 3. Install Node.js Dependencies

```bash
npm install
npx prisma generate
```

Run migrations if needed:
```bash
npx prisma migrate dev --name init
```

### 4. Set Up Python Virtual Environment
Run migrations if needed:
```bash
cd data
source .venv\Scripts\activate
pip install -r requirements.txt
```

### 5. Start the Express Server

```bash
npm run dev
```

### 6. Run Python Scripts (Optional)
```bash
cd data
.venv\Scripts\activate 
```
Run data generation or insertion scripts:
```bash
python craftData.py
python main.py
```