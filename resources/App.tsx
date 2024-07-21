import { Route, Routes } from "react-router-dom"
// pages imports
import Placeholder from "@/pages/Placeholder"
import Home from "@/pages/Home"
import PageNotFound from "@/pages/PageNotFound"
import React from "react"
// import { ThemeProvider } from "@/components/theme-provider"

const App: React.FC = () => {
  return (
    <Routes>
      <Route path="/">
        <Route index element={<Home />} />
      </Route>
      <Route path="/landing" element={<Placeholder />} />
      <Route path="/terms" element={<Placeholder />} />
      <Route path="/privacy" element={<Placeholder />} />
      <Route path="*" element={<PageNotFound />} />
    </Routes>
  )
}

export default App
