# Unreleased Core Changes

## Compatibility

- Custom request interceptors now run before every HTTP attempt, including retries, to match the Java and PHP SDK request lifecycle. Interceptors with non-idempotent logical-request-only behavior must set `run_on_retry = False`.
- `Configuration.retryer` once again returns a stable, mutable per-Configuration object. Retry scalar getters now report the effective values held by that object, while each ApiClient keeps an isolated retry policy snapshot created at client construction.
