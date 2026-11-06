import { describe, expect, it } from 'vitest'
import { describeHealth } from './health'

describe('describeHealth', () => {
  it('reports an unreachable API', () => {
    expect(describeHealth(null)).toBe('API unreachable')
  })

  it('reports a database problem', () => {
    expect(describeHealth({ status: 'ok', database: 'unavailable' })).toBe(
      'API online, database unavailable',
    )
  })

  it('reports everything online', () => {
    expect(describeHealth({ status: 'ok', database: 'ok' })).toBe('API and database online')
  })
})
