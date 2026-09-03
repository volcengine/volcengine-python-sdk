# Unreleased Core Changes

## Features

- Every signed request now carries two additional signed headers: `X-Sdk-Invocation-Id` (one UUID per logical SDK call, stable across retries) and `X-Sdk-Request` (`attempt=<n>; max=<m>`, refreshed on every attempt).
- Retried attempts are re-signed: `Authorization`, `X-Date`, `X-Content-Sha256` and `X-Security-Token` are regenerated before each retry, and credential providers are consulted again so refreshed temporary credentials are used.

## Behavior Changes

- Custom request interceptors now run before every HTTP attempt, including retries, to match the Java SDK request lifecycle. Interceptors that must run only once per logical SDK call must set `run_on_retry = False`.
- Retry settings are no longer shared through a process-wide singleton: every `Configuration` owns its own `Retryer`, and per-request `RuntimeOption` retry overrides no longer leak into other requests, threads or `Configuration` objects.
- Each `ApiClient` snapshots the retry policy of its `Configuration` at construction. Changing `num_max_retries`, or assigning a new `backoff_strategy` / `retry_condition` object, on a `Configuration` after an `ApiClient` (or a service API object) was created from it no longer affects that client; set retry values before calling `Configuration.set_default` / creating the client, or create a new client. Built-in strategies and conditions are copied into the snapshot, so later scalar changes (`min_retry_delay_ms`, `max_retry_delay_ms`, `retry_error_codes`) do not reach existing clients either. Custom `BackoffStrategy` / `RetryCondition` instances are shared by identity, so scalar changes made on such an instance remain visible to every client holding it.
- `Configuration.retryer` returns a stable, mutable per-Configuration object. Retry scalar getters now report the effective values held by that object (`retry_error_codes` defaults to an empty set, `min_retry_delay_ms` / `max_retry_delay_ms` default to `300` / `300000`) instead of `None`.
- Per-request `RuntimeOption` scalar overrides (`min_retry_delay_ms`, `max_retry_delay_ms`, `retry_error_codes`) applied on top of a custom `BackoffStrategy` / `RetryCondition` are applied to a shallow copy of that custom object for the current request, instead of mutating the shared instance.
