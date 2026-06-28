# Boundary: Live Integration Boundaries

Status: draft

## Summary

A live integration boundary is any dependency on a real external system, service, API, provider, account, credential, browser behavior, deployment environment, or production configuration.

## Policy

Live integrations require explicit verification when they are material to user-visible behavior or release risk.

## Examples

- external APIs
- map/tile providers
- auth providers
- hosted databases
- email providers
- payment providers
- analytics/telemetry providers
- browser-only rendering behavior
- PWA/service worker behavior
- production environment variables
- domain/CORS restrictions
- quotas and billing state
- SLO monitoring and error budget tracking against Top K user journey targets

## Live verification is useful for

- real credentials
- real response status
- real schema shape
- provider availability
- domain restrictions
- browser fetch/render behavior
- deployment configuration

## Live verification is not for

- exhaustive edge cases
- fast local TDD loops
- every save or every unit test run
- replacing deterministic unit tests

## Required documentation

For each material live boundary, document:

- dependency
- production behavior
- verification method
- required environment/config
- cadence
- release requirement
- failure response

## Recommended cadence

Use risk-based cadence:

- before release for critical user-visible integrations
- scheduled synthetic checks for ongoing provider health and SLO target
  verification against Top K user journeys
- manual checklist for low-frequency or hard-to-automate behavior
- production monitoring for behavior that can drift after deployment, including
  error budget consumption
