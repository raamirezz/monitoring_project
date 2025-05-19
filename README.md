# 🚀 Proyecto de Monitorización con Ansible, Prometheus y Grafana

Este proyecto implementa un sistema completo de monitorización automatizada mediante **Ansible**, **Docker Compose**, **Prometheus**, **Grafana**, y dos aplicaciones monitorizadas: una externa que simula métricas (`sample_app`) y una aplicación personalizada en Flask (`my_flask_app`).

---

## 📦 Tecnologías utilizadas

- **Ansible** – Automatización del despliegue y gestión
- **Docker & Docker Compose** – Contenerización de servicios
- **Prometheus** – Recolección de métricas
- **Grafana** – Visualización de métricas y alertas
- **Node Exporter** – Métricas del sistema host
- **Sample App** – Aplicación externa que simula métricas variadas
- **My Flask App** – Aplicación personalizada con login que expone métricas

---

## 🧱 Arquitectura del sistema

```
Ansible
  │
  └── Docker Compose
        ├── Prometheus
        ├── Grafana
        ├── Node Exporter
        ├── Sample App
        └── My Flask App
```

- **Prometheus** scrapea métricas de las apps y node-exporter.
- **Grafana** muestra dashboards interactivos y alertas.
- **Ansible** permite levantar, parar y destruir todo el stack con un solo comando.

---

## ▶️ Cómo usar

### 1. Requisitos previos

- Tener Ansible instalado
- Tener Docker y Docker Compose instalados en el host objetivo

### 2. Ejecutar los playbooks

- 🔼 **Levantar el stack**:
  ```bash
  ansible-playbook -i inventories/hosts.ini start.yml
  ```

- 🟡 **Parar los contenedores sin eliminar datos**:
  ```bash
  ansible-playbook -i inventories/hosts.ini stop.yml
  ```

- 🔽 **Eliminar completamente todos los contenedores y volúmenes**:
  ```bash
  ansible-playbook -i inventories/hosts.ini down.yml
  ```

---

## 📊 Dashboards en Grafana

- Dashboard para **Node Exporter** con métricas del sistema (CPU, RAM, etc.)
- Dashboard para **Sample App** con métricas simuladas (counters, histograms...)
- Dashboard para **My Flask App** que muestra intentos de login por usuario
- Alertas configuradas: login fallido más de 10 veces en 5 minutos

---

## 📌 Objetivos alcanzados

- ✅ Automatización total del stack de monitorización
- ✅ Visualización clara de métricas de sistema y aplicaciones
- ✅ Alertas en tiempo real configurables
- ✅ Aplicación propia integrada con métricas personalizadas

---

## ✍️ Autor

Carlos – Proyecto realizado como parte de un curso de 8 semanas sobre automatización y monitorización.
