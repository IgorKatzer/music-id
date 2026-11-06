import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// In development, requests to /api are forwarded to the FastAPI backend.
// API_URL is set by docker-compose; outside Docker it defaults to localhost.
export default defineConfig({
  plugins: [react()],
  server: {
    host: true,
    port: 5173,
    proxy: {
      '/api': process.env.API_URL ?? 'http://localhost:8000',
    },
  },
})
