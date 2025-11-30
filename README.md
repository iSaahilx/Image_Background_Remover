# 🐱 Meow Background Remover

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

**✨ Remove image backgrounds instantly with AI-powered precision ✨**

*Drag. Drop. Done.*

</div>

---

## 🎯 What is this?

A lightweight, self-hosted background removal tool powered by the **U2-Net** deep learning model. Simply upload an image, and watch the magic happen — get a clean, transparent PNG in seconds.

No subscriptions. No limits. No cloud uploads. **Your images stay on your machine.**

## 🚀 Features

- 🖼️ **Drag & Drop** — Just drop your image, no clicking required
- ⚡ **Instant Processing** — AI removes backgrounds in seconds
- 🔒 **Privacy First** — All processing happens locally
- 🐳 **Docker Ready** — One command to deploy anywhere
- 📦 **Lightweight** — Minimal dependencies, maximum performance

## 📸 How It Works

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   Upload    │  →   │   U2-Net    │  →   │  Download   │
│   Image     │      │   Magic     │      │    PNG      │
└─────────────┘      └─────────────┘      └─────────────┘
```

The app uses **rembg** with the U2-Net model to detect foreground objects and create precise alpha masks, resulting in clean transparent backgrounds.

## 🛠️ Quick Start

### Option 1: Run Locally

```bash
# Clone the repo
git clone <repository-url>
cd bgremover

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Open http://localhost:5000 and start removing backgrounds!

### Option 2: Docker

```bash
# Download U2Net model first (required)
# https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx

# Build the image
docker build -t bgremover .

# Run the container
docker run -p 5000:5000 bgremover
```

## 📁 Project Structure

```
bgremover/
├── app.py              # Flask application
├── templates/
│   └── index.html      # Drag & drop UI
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container configuration
└── README.md
```

## 🔧 Requirements

```
flask
rembg
pillow
```

## 🐳 Docker Setup

For faster container startup, pre-download the U2Net model:

1. Download [u2net.onnx](https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx) (~176MB)
2. Place it in the project root
3. Build and run the Docker image

This avoids downloading the model every time the container starts.

## 💡 Use Cases

- 🛍️ **E-commerce** — Clean product photos
- 🎨 **Design** — Quick cutouts for compositions
- 📱 **Social Media** — Profile pictures & stickers
- 🖥️ **Presentations** — Professional image assets

## ⚙️ API Endpoint

```http
POST /
Content-Type: multipart/form-data

file: <image-file>
```

**Response:** PNG image with transparent background

## 🤝 Contributing

Pull requests welcome! Feel free to:
- Add new features
- Improve the UI
- Optimize performance
- Fix bugs

## 📄 License

MIT — Use it however you want.

---

<div align="center">

**Made with 🐱 and Python**

*Meow will remove the background for you*

</div>

