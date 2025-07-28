import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="The End 💔", layout="wide")

# Load and encode audio file
def get_audio_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

audio_base64 = get_audio_base64("emitemito.mp3")

# Render full HTML using components.html
components.html(f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>The End 💔</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display&family=Roboto+Mono&display=swap');
body {{
    margin: 0;
    background: #0d0d0d;
    color: white;
    font-family: 'Playfair Display', serif;
    overflow: hidden;
}}
.container {{
    text-align: center;
    padding: 100px 20px;
    z-index: 1;
    position: relative;
}}
h1 {{
    font-size: 60px;
    color: #ff4d4d;
}}
p {{
    font-size: 22px;
    line-height: 1.8;
    color: #dddddd;
    font-family: 'Roboto Mono', monospace;
}}
canvas#rain {{
    position: fixed;
    top: 0;
    left: 0;
    pointer-events: none;
    z-index: 0;
}}
</style>
</head>
<body>
<canvas id="rain"></canvas>

<audio autoplay loop>
    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
</audio>

<div class="container">
    <h1>THE END 💔</h1>
    <p>
        Some stories end without closure.<br>
        Some names echo in silence, even when unspoken.<br><br>
        You were never just a memory — you were my pulse.<br>
        And now, you're my ache.<br><br>
        <span style="font-size: 14px; color: #888;">
        If you're reading this... I let you go, but I never stopped loving you.
        </span>
    </p>
</div>

<script>
const canvas = document.getElementById('rain');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let drops = [];
for(let i = 0; i < 400; i++) {{
    drops.push({{
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        l: Math.random() * 1,
        xs: -4 + Math.random() * 4 + 2,
        ys: Math.random() * 10 + 10
    }});
}}

function draw() {{
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = "rgba(255,255,255,0.1)";
    ctx.lineWidth = 1;
    ctx.beginPath();
    for(let i = 0; i < drops.length; i++) {{
        let d = drops[i];
        ctx.moveTo(d.x, d.y);
        ctx.lineTo(d.x + d.l * d.xs, d.y + d.l * d.ys);
    }}
    ctx.stroke();
    move();
}}

function move() {{
    for(let i = 0; i < drops.length; i++) {{
        let d = drops[i];
        d.x += d.xs;
        d.y += d.ys;
        if(d.x > canvas.width || d.y > canvas.height) {{
            d.x = Math.random() * canvas.width;
            d.y = -20;
        }}
    }}
}}

setInterval(draw, 33);
</script>
</body>
</html>
""", height=800)
