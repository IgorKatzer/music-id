export type HealthResponse = {
  status: string
  database: string
}

/** Turns the /api/health response into a short message for the screen. */
export function describeHealth(health: HealthResponse | null): string {
  if (health === null) return 'API unreachable'
  if (health.database !== 'ok') return 'API online, database unavailable'
  return 'API and database online'
}
