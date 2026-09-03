# app.py
import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Book of Enoch: Complete Entity & Heavenly World",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inline data setup so no external world_data.json file is required
data = {
  "entities": [
    {
      "id": "god_throne",
      "name": "The Great Glory on the Crystal Throne (Enoch 14:18-22)",
      "x": 0, "y": 100, "z": 0,
      "size": 6.0,
      "color": "#FFFFFF",
      "model_file": "assets/throne.glb",
      "scripture": "Enoch 14:20 — 'The Great Glory sat thereon, and His raiment shone more brightly than the sun and was whiter than any snow.'"
    },
    {
      "id": "seraphim_host",
      "name": "The Seraphim — Six-Winged Fiery Spirits (Enoch 61:10, 71:7)",
      "x": 10, "y": 105, "z": 10,
      "size": 3.0,
      "color": "#FF2200",
      "model_file": "assets/seraphim.glb",
      "scripture": "Enoch 71:7 — 'And round about were Seraphim, Cherubim, and Ophanim: these are they who sleep not and guard the throne of His glory.'"
    },
    {
      "id": "cherubim_host",
      "name": "The Cherubim (Enoch 14:11, 71:7)",
      "x": -10, "y": 105, "z": -10,
      "size": 3.0,
      "color": "#FFD700",
      "model_file": "assets/cherubim.glb",
      "scripture": "Enoch 14:11 — 'And the ceiling was like the path of the stars and the lightnings, and between them were fiery cherubim.'"
    },
    {
      "id": "ophanim_host",
      "name": "The Ophanim — Wheels of Eyes (Enoch 61:10, 71:7)",
      "x": 0, "y": 92, "z": 0,
      "size": 5.0,
      "color": "#00E5FF",
      "model_file": "assets/ophanim.glb",
      "scripture": "Enoch 61:10 — 'And all the host of the heavens, and all the holy ones above... the Cherubim, the Seraphim, and the Ophanim.'"
    },
    {
      "id": "archangel_michael",
      "name": "Archangel Michael (Enoch 20:5, 71:3)",
      "x": 20, "y": 95, "z": 20,
      "size": 2.5,
      "color": "#FFD700",
      "model_file": "assets/michael.glb",
      "scripture": "Enoch 20:5 — 'Michael, one of the holy angels, set over the best part of mankind and over chaos.'"
    },
    {
      "id": "archangel_uriel",
      "name": "Archangel Uriel (Enoch 20:2, 19:1)",
      "x": -20, "y": 95, "z": -20,
      "size": 2.5,
      "color": "#FF0055",
      "model_file": "assets/uriel.glb",
      "scripture": "Enoch 20:2 — 'Uriel, one of the holy angels, who is over the world and over Tartarus.'"
    },
    {
      "id": "archangel_raphael",
      "name": "Archangel Raphael (Enoch 20:3, 10:4)",
      "x": 20, "y": 95, "z": -20,
      "size": 2.5,
      "color": "#00FFCC",
      "model_file": "assets/raphael.glb",
      "scripture": "Enoch 20:3 — 'Raphael, one of the holy angels, who is over the spirits of men.'"
    },
    {
      "id": "archangel_gabriel",
      "name": "Archangel Gabriel (Enoch 20:7, 10:9)",
      "x": -20, "y": 95, "z": 20,
      "size": 2.5,
      "color": "#FFFFFF",
      "model_file": "assets/gabriel.glb",
      "scripture": "Enoch 20:7 — 'Gabriel, one of the holy angels, who is over Paradise, the serpents, and the Cherubim.'"
    },
    {
      "id": "archangel_phanuel",
      "name": "Archangel Phanuel (Enoch 40:9)",
      "x": 0, "y": 95, "z": 30,
      "size": 2.5,
      "color": "#AA00FF",
      "model_file": "assets/phanuel.glb",
      "scripture": "Enoch 40:9 — 'And the fourth, who is set over the repentance unto hope of those who inherit eternal life, is named Phanuel.'"
    },
    {
      "id": "watcher_semyaza",
      "name": "Semyaza — Leader of Fallen Watchers (Enoch 6:3, 10:11)",
      "x": 35, "y": 20, "z": 35,
      "size": 3.0,
      "color": "#4A5568",
      "model_file": "assets/semyaza.glb",
      "scripture": "Enoch 6:3 — 'And Semjaza, who was their leader, said unto them: I fear ye will not indeed agree to do this deed.'"
    },
    {
      "id": "watcher_azazel",
      "name": "Azazel — Bound in Dudael Darkness (Enoch 8:1, 10:4)",
      "x": -35, "y": 15, "z": -35,
      "size": 3.0,
      "color": "#1A202C",
      "model_file": "assets/azazel.glb",
      "scripture": "Enoch 10:4 — 'Bind Azazel hand and foot, and cast him into the darkness: and make an opening in the desert, which is in Dudael, and cast him therein.'"
    },
    {
      "id": "enoch_prophet",
      "name": "Enoch the Scribe (Enoch 12:3, 14:24)",
      "x": 0, "y": 80, "z": 40,
      "size": 1.8,
      "color": "#00FF66",
      "model_file": "assets/enoch.glb",
      "scripture": "Enoch 14:24 — 'And the Lord called me with His own mouth, and said to me: Come hither, Enoch, and hear my word.'"
    }
  ]
}

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

        // LIGHTING ENGINE
        scene.add(new THREE.AmbientLight(0xffffff, 0.6));

        // Throne light source
        const throneLight = new THREE.PointLight(0xffffff, 4, 250);
        throneLight.position.set(0, 100, 0);
        scene.add(throneLight);

        const loader = new THREE.GLTFLoader();

        // ENTITY RENDERER
        worldData.entities.forEach(item => {{
            const group = new THREE.Group();

            // Try loading actual 3D GLTF asset; automatically fallback to standalone meshes if no files exist
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

            if (selectedTarget === item.name) {{
                controls.target.set(item.x, item.y, item.z);
                camera.position.set(item.x + 15, item.y + 10, item.z + 25);
            }}
        }});

        // RENDER LOOP
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
