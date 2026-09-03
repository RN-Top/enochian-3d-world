import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Book of Enoch: Complete Entity & Heavenly World",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    with open("world_data.json", "r") as f:
        return json.load(f)

data = load_data()

st.sidebar.title("📖 Book of Enoch Characters")
st.sidebar.caption("Complete Hierarchy of Angels, Watchers, and Divine Beings")

entity_names = [e["name"] for e in data["entities"]]
selected_entity = st.sidebar.selectbox("Select Character/Entity to Inspect:", ["View All"] + entity_names)

if selected_entity != "View All":
    item = next(e for e in data["entities"] if e["name"] == selected_entity)
    st.sidebar.subheader("Scripture & Details")
    st.sidebar.write(f"**Entity:** {item['name']}")
    st.sidebar.info(f"**Manuscript Citation:** {item['scripture']}")

json_payload = json.dumps(data)
selected_payload = json.dumps(selected_entity)

threejs_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ margin: 0; padding: 0; overflow: hidden; background-color: #010103; font-family: sans-serif; }}
        #canvas-container {{ width: 100vw; height: 88vh; position: relative; }}
        #hud {{
            position: absolute;
            top: 15px;
            left: 15px;
            color: #ffffff;
            background: rgba(10, 15, 30, 0.9);
            padding: 12px 18px;
            border-radius: 8px;
            font-size: 13px;
            border: 1px solid rgba(255, 215, 0, 0.4);
            pointer-events: none;
            max-width: 350px;
        }}
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"></script>
</head>
<body>
    <div id="canvas-container">
        <div id="hud">
            <b style="color: #ffd700;">Book of Enoch Entity Engine</b><br>
            Left-Click: Rotate | Scroll: Zoom | Right-Click: Pan
        </div>
    </div>

    <script>
        const worldData = {json_payload};
        const selectedTarget = {selected_payload};

        const container = document.getElementById('canvas-container');
        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x010103, 0.003);

        const camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 1000);
        camera.position.set(0, 90, 120);

        const renderer = new THREE.WebGLRenderer({{ antialias: true }});
        renderer.setSize(container.clientWidth, container.clientHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.4;
        container.appendChild(renderer.domElement);

        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.04;

        // --- LIGHTING ENGINE ---
        scene.add(new THREE.AmbientLight(0xffffff, 0.6));

        // Blinding divine throne light source
        const throneLight = new THREE.PointLight(0xffffff, 4, 250);
        throneLight.position.set(0, 100, 0);
        scene.add(throneLight);

        const loader = new THREE.GLTFLoader();

        // --- ENTITY RENDERER ---
        worldData.entities.forEach(item => {{
            const group = new THREE.Group();

            // Try loading actual 3D GLTF asset; fallback to generated meshes
            loader.load(
                item.model_file,
                function(gltf) {{
                    const model = gltf.scene;
                    model.position.set(item.x, item.y, item.z);
                    model.scale.set(item.size, item.size, item.size);
                    scene.add(model);
                }},
                undefined,
                function(error) {{
                    // Fallback visual representations if .glb model files are absent
                    let mesh;
                    if (item.id === "god_throne") {{
                        const geo = new THREE.OctahedronGeometry(item.size, 2);
                        const mat = new THREE.MeshStandardMaterial({{ color: 0xffffff, emissive: 0xffffff, emissiveIntensity: 1.0 }});
                        mesh = new THREE.Mesh(geo, mat);
                    }} else if (item.id === "ophanim_host") {{
                        const geo = new THREE.TorusGeometry(item.size, 0.6, 16, 100);
                        const mat = new THREE.MeshStandardMaterial({{ color: 0x00e5ff, wireframe: true }});
                        mesh = new THREE.Mesh(geo, mat);
                    }} else {{
                        const geo = new THREE.DodecahedronGeometry(item.size, 1);
                        const mat = new THREE.MeshStandardMaterial({{ color: item.color, emissive: item.color, emissiveIntensity: 0.4 }});
                        mesh = new THREE.Mesh(geo, mat);
                    }}
                    
                    mesh.position.set(item.x, item.y, item.z);
                    group.add(mesh);
                    scene.add(group);
                }}
            );

            // Set Orbit Camera Focus if selected from dropdown
            if (selectedTarget === item.name) {{
                controls.target.set(item.x, item.y, item.z);
                camera.position.set(item.x + 15, item.y + 10, item.z + 25);
            }}
        }});

        // --- RENDER LOOP ---
        function animate() {{
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        }}
        animate();

        window.addEventListener('resize', () => {{
            camera.aspect = container.clientWidth / container.clientHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(container.clientWidth, container.clientHeight);
        }});
    </script>
</body>
</html>
"""

st.title("Book of Enoch: Complete Entity & Divine Hierarchy Viewer")
components.html(threejs_html, height=750)
