# Canary Analysis Strategy

## Metrics used for automatic decision

1. **Success Rate** ≥ 95%
2. **p99 Latency** < 500ms
3. **Error budget** consumption rate

If any metric fails for 3 consecutive intervals → **automatic rollback**.

## Manual gates

Production promotions still require a human approval step after successful canary analysis.
