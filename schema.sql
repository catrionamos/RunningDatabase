CREATE TABLE IF NOT EXISTS programs (
    program_id SERIAL PRIMARY KEY,
    program_name VARCHAR(100) NOT NULL,
    target_level VARCHAR(50),
    duration_weeks INT,
    description TEXT
);

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    fitness_level VARCHAR(50),
    running_goal VARCHAR(100),
    program_id INT REFERENCES programs(program_id)
);

CREATE TABLE IF NOT EXISTS runs (
    run_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    run_date DATE NOT NULL,
    distance_km FLOAT NOT NULL,
    duration_minutes INT NOT NULL,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price FLOAT NOT NULL,
    stock_quantity INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    product_id INT REFERENCES products(product_id),
    quantity INT NOT NULL,
    total_amount FLOAT NOT NULL,
    order_date DATE DEFAULT CURRENT_DATE
);