import feather from "feather-icons"
import "./input.css"
import "./logo.png"
import "vite/modulepreload-polyfill"

import React from "react"
import ReactDOM from "react-dom/client"
import App from "@/App.tsx"
import "@/styles.css"
import { BrowserRouter } from "react-router-dom"

feather.replace({
  "stroke-width": 2,
  width: 24,
  height: 24,
})

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
)
