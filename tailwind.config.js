// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,js}",
    "./node_modules/flowbite/**/*.js",
    "./invoices/forms.py",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("flowbite/plugin"), require("daisyui")],

  safelist: ["alert-info", "alert-success", "alert-warning", "alert-error"],
};
