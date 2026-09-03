# 📖 Enochian Cosmological 3D Visualizer

An interactive, browser-rendered 3D visualization tool built to map the cosmology of the Enochian system (including the 30 Æthyrs, the Four Watchtowers, and the Central Seat/Throne) directly from the primary manuscript diaries of John Dee and Edward Kelley.

This project uses **Python (Streamlit)** for the interface and data loading, paired with **Three.js (WebGL)** to render responsive 3D graphics directly on the user's GPU without relying on server-side rendering.

---

## 🌟 Key Features

* **Literal Manuscript Mapping:** Structural data (coordinates, colors, descriptions) is stored independently in JSON format to remain faithful to original primary sources without modern secondary additions.
* **Interactive WebGL Engine:** Built with Three.js to provide smooth orbit, zoom, and panning camera controls.
* **Streamlit Integration:** Uses Streamlit's native UI controls to filter entities, focus the 3D camera on specific structures, and read primary manuscript citations.
* **Zero Heavy Dependencies:** Lightweight setup ready for free, instant deployment on Streamlit Community Cloud.

---

## 📁 Repository Structure

```text
.
├── app.py              # Main Streamlit application and WebGL Three.js renderer
├── world_data.json     # Primary text database containing coordinates and citations
├── requirements.txt    # Python package dependencies
└── README.md           # Project documentation
