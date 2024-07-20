import Alpine from "alpinejs"
import feather from "feather-icons"
import "./input.css"
import "./logo.png"

feather.replace({
  "stroke-width": 2,
  width: 24,
  height: 24,
})

// @ts-ignore
window.Alpine = Alpine
Alpine.start()
