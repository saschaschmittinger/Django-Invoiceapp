// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/", "./node_modules/flowbite/**/*.js"], // updated line here!
  theme: {
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
};
