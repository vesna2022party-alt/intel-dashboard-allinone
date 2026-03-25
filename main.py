from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/regions")
def regions():
    return [
        {"region":"Kyiv","risk":0.8},
        {"region":"Lviv","risk":0.4},
        {"region":"Kharkiv","risk":0.9},
        {"region":"Odesa","risk":0.7}
    ]

@app.get("/", response_class=HTMLResponse)
def home():
    return \"\"\"
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Dashboard</title>

<script src="https://unpkg.com/react@18/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
</head>

<body>
<div id="root"></div>

<script>
const { useEffect, useState } = React;

function App(){
  const [data,setData]=useState([]);

  useEffect(()=>{
    fetch("/api/regions")
      .then(r=>r.json())
      .then(setData);
  },[]);

  return React.createElement("div",null,
    React.createElement("h2",null,"Ukraine Dashboard"),
    data.map(r=>React.createElement("div",null,
      r.region + " risk: " + r.risk
    ))
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(React.createElement(App));
</script>
</body>
</html>
\"\"\"
