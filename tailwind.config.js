/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme")

module.exports = {
  darkMode: "class",
  content: [
    "{resources,templates}/**/*.{js,cjs,mjs,jsx,ts,tsx,vue,j2,html,htm,jinja,jinja2}",
    "src/pybama_org/frontend/templates/**/*.{js,jsx,ts,cjs,mjs,tsx,vue,j2,html,htm,jinja,jinja2}",
  ],
  safelist: ["alert", "alert-success", "alert-error", "alert-warning", "alert-info"],
  plugins: [require("@tailwindcss/typography"), require("@tailwindcss/aspect-ratio"), require("daisyui")],
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      colors: {
        "python-primary": "#4584b6",
        "python-accent": "#ffde57",
        "python-secondary": "#646464",
      },
    },
  },
  daisyui: {
    darkTheme: "dark",
    base: true,
    styled: true,
    utils: true,
    themes: [
      {
        light: {
          primary: "#4584b6",
          secondary: "#646464",
          accent: "#70b2e7",
          neutral: "#e5e7eb",
          "base-100": "#f3f4f6",
          info: "#7dd3fc",
          success: "#86efac",
          warning: "#fcd34d",
          error: "#f87171",
        },
        dark: {
          primary: "#4584b6",
          secondary: "#ebebe9",
          accent: "#70b2e7",
          neutral: "#202020",
          "base-100": "#121212",
          info: "#7dd3fc",
          success: "#86efac",
          warning: "#fcd34d",
          error: "#f87171",
        },
      },
    ],
  },
}
