
# 📊 Bitcoin Tracker

A comprehensive Bitcoin price tracking application that monitors Bitcoin prices in real-time, stores historical data, and provides trading recommendations through a web interface.

---

## 🚀 Features

- **Real-time Bitcoin Price Tracking**: Fetches current Bitcoin price every minute from CoinGecko API  
- **Statistical Analysis**: Calculates average, minimum, and maximum prices from application start  
- **Trading Recommendations**: Provides BUY/SELL/HOLD recommendations based on price analysis  
- **Web Dashboard**: Flask-based web interface displaying live statistics  
- **Database Storage**: Persistent SQLite database for historical price data  
- **Containerized Architecture**: Multi-container Docker setup for scalability  
- **Automated Deployment**: Ansible playbooks for easy deployment and Docker installation  

---

## 🏗️ Architecture

The application consists of two main containers:

1. **Tracker Container** – Python application that fetches Bitcoin prices and stores them in the database  
2. **API Service Container** – Flask web service that serves statistics and recommendations

---

## 📋 Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop) and Docker Compose installed  
- [Ansible](https://www.ansible.com/) (optional, for automated deployment)

---

## 🔧 Installation & Setup

### 🔹 Option 1: Using Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/toharbarazi/bitcoin.git
cd bitcoin-tracker

# Start the application
docker compose up --build
````

### 🔹 Option 2: Using Ansible Playbooks

```bash
# Install Docker (if not already installed)
ansible-playbook ansible/install_docker.yml

# Deploy the application
ansible-playbook ansible/deploy.yml
❗ after, run this command to see the output:
docker logs -f bitcoin-tracker
```

---

## 🖥️ Usage

### Accessing the Web Dashboard

Once the application is running, open in browser:

```
http://localhost:5000/stats
```

The dashboard displays:

* 🧮 **Average Price** – Mean price since app start
* 📉 **Minimum Price** – Lowest recorded price
* 📈 **Maximum Price** – Highest recorded price
* 📊 **Trading Recommendation** – BUY / SELL / HOLD

---

### 💡 Trading Logic

* **BUY** – When average price < \$25,000
* **SELL** – When average price > \$40,000
* **HOLD** – When average price is between \$25,000 and \$40,000

---

### 📟 Console Output Example

```
[2025-06-10 10:30:00] Current: $67,500 | Avg: $65,200.45 | Min: $63,100 | Max: $69,800 | Recommendation: Hold


## 🐳 Container Details

### 🛒 Tracker Container

* **Base Image**: `python:3.12-slim`
* **Role**: Fetches Bitcoin prices every 60 seconds
* **Dependencies**: `requests`
* **Data**: Writes to shared SQLite database

### 📊 API Service Container

* **Base Image**: `python:3.10-slim`
* **Role**: Serves statistics & recommendations over HTTP
* **Port**: `5000`
* **Dependencies**: `Flask`
* **Auto-refresh**: Page refreshes every 5 seconds

---

## 🛠️ Configuration

### 🗄️ Database Configuration

* **Type**: SQLite
* **File**: `bitcoin.db`
* **Location**: Shared volume between containers
* **Schema**: Table with `timestamp`, `price` columns

---

## 🚦 API Endpoint

### `GET /stats`

Returns an HTML dashboard with:

* Current Bitcoin statistics
* BUY/SELL/HOLD recommendation
* Auto-refreshing interface (every 5 seconds)
* Responsive layout

---

## 📈 Happy Trading! 🚀


