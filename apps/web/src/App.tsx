import { useEffect, useState } from 'react'
import { describeHealth, type HealthResponse } from './health'

export default function App() {
  const [message, setMessage] = useState('Checking API...')

  useEffect(() => {
    fetch('/api/health')
      .then((response) => (response.ok ? response.json() : null))
      .then((health: HealthResponse | null) => setMessage(describeHealth(health)))
      .catch(() => setMessage(describeHealth(null)))
  }, [])

  return (
    <main>
      <h1>Music ID</h1>
      <p>Identify a song by its composition, not just its recording.</p>
      <p className="status">{message}</p>
    </main>
  )
}
