import json
import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(
    page_title="Enochian Cosmology Visualizer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Source Data from JSON
@st.cache_data
def load_data():
    with open("world_data.json", "r") as f:
        return json.load(f)

data = load_data()

# Sidebar Navigation
st.sidebar.title("Manuscript Explorer")
st.sidebar.caption("Literal mapping derived strictly from Dee & Kelley's records.")

entity_names = [e["name"] for e in data["entities"]]
selected_entity = st.sidebar.selectbox("Select Structure / Entity:", ["Show All"] + entity_names)

if selected_entity != "Show All":
    item = next(e for e in data["entities"] if e["name"] == selected_entity)
    st.sidebar.subheader("Entity Details")
    st.sidebar.write(f"**Name:** {item['name']}")
    st.sidebar.write(f"**Position (X,Y,Z):** ({item['x']}, {item['y']}, {item['z']})")
    st.sidebar.info(f"**Text Citation:** {item['description']}")

# Prepare Data for Browser WebGL Engine
json_payload = json.dumps(data)
selected_payload = json.dumps(selected_entity)

# WebGL 3D Embedded Code
threejs_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ margin: 0; padding: 0; overflow: hidden; background-color: #020205; font-family: sans-serif; }}
        #canvas-container {{ width: 100vw; height: 85vh; position: relative; }}
        #controls-hint {{
            position: absolute;
            bottom: 15px;
            left: 15px;
            color: #d1d5db;
            background: rgba(0, 0, 0, 0.75);
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 13px;
            border: 1px solid #374151;
            pointer-events: none;
        }}
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
    <div id="canvas-container">
        <div id="controls-hint">Rotate: Left-Click + Drag | Zoom: Scroll | Pan: Right-Click + Drag</div>
    </div>

    <script>
        const worldData = {json_payload};
        const selectedTarget = {selected_payload};

        const container = document.getElementById('canvas-container');
        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x020205, 0.008);

        // Camera setup
        const camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 1000);
        camera.position.set(0, 40, 70);

        // WebGL Renderer
        const renderer = new THREE.WebGLRenderer({{ antialias: true }});
        renderer.setSize(container.clientWidth, container.clientHeight);
        renderer.setPixelRatio(window.devicePixelRatio);
        container.appendChild(renderer.domElement);

        // Controls
        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;

        // Lighting
        scene.add(new THREE.AmbientLight(0xffffff, 0.7));
        const centralLight = new THREE.PointLight(0xffd700, 2, 120);
        centralLight.position.set(0, 25, 0);
        scene.add(centralLight);

        // Grid Floor (representing the Great Table base grid)
        const gridHelper = new THREE.GridHelper(80, 40, 0x00e5ff, 0x111827);
        gridHelper.position.y = -10;
        scene.add(gridHelper);

        // Draw Spherical/Ring Layers for Æthyrs
        worldData.aethyrs.forEach(aethyr => {{
            const ringGeo = new THREE.RingGeometry(aethyr.radius - 0.15, aethyr.radius + 0.15, 64);
            const ringMat = new THREE.MeshBasicMaterial({{ 
                color: aethyr.color, 
                side: THREE.DoubleSide, 
                transparent: true, 
                opacity: 0.45 
            }});
            const ring = new THREE.Mesh(ringGeo, ringMat);
            ring.rotation.x = Math.PI / 2;
            scene.add(ring);
        }});

        // Render Structures & Entities
        const meshes = [];
        worldData.entities.forEach(item => {{
            const isHighlight = (selectedTarget === item.name);
            const geo = new THREE.SphereGeometry(item.size, 32, 32);
            const mat = new THREE.MeshStandardMaterial({{ 
                color: item.color, 
                emissive: item.color,
                emissiveIntensity: isHighlight ? 0.9 : 0.25,
                roughness: 0.2
            }});
            
            const mesh = new THREE.Mesh(geo, mat);
            mesh.position.set(item.x, item.y, item.z);
            
            const pointLight = new THREE.PointLight(item.color, isHighlight ? 1.5 : 0.3, 15);
            mesh.add(pointLight);

            scene.add(mesh);
            meshes.push(mesh);

            // Focus camera if selected from sidebar
            if (isHighlight) {{
                controls.target.set(item.x, item.y, item.z);
                camera.position.set(item.x + 12, item.y + 12, item.z + 18);
            }}
        }});

        // Animation Loop
        function animate() {{
            requestAnimationFrame(animate);
            meshes.forEach(m => {{ m.rotation.y += 0.008; }});
            controls.update();
            renderer.render(scene, camera);
        }}
        animate();

        // Window Resizing
        window.addEventListener('resize', () => {{
            camera.aspect = container.clientWidth / container.clientHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(container.clientWidth, container.clientHeight);
        }});
    </script>
</body>
</html>
"""

st.title("Enochian Cosmological 3D Map")
components.html(threejs_html, height=730)
