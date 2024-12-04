module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}', // Add this to ensure Tailwind scans your components in the app folder
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
