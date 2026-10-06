# Project 4: Centralized Observability Stack

> Metrics + Logs + Alerts built from scratch on EKS.

## Stack

| Component     | Tool          | Purpose                        |
|---------------|---------------|--------------------------------|
| Metrics       | Prometheus    | Collection + storage           |
| Visualization | Grafana       | Dashboards + exploration       |
| Logs          | Loki          | Log aggregation (label-based)  |
| Alerting      | Alertmanager  | Routing + silencing            |

## What you get

- Full Helm-based deployment
- Custom **SLO dashboards**
- Alert routing to Slack / PagerDuty
- Recording rules for common SLIs
- Ready-to-use Kubernetes + application dashboards

## Directory Structure

```
project4-centralized-observability/
├── helm/
│   ├── prometheus/
│   ├── grafana/
│   ├── loki/
│   └── alertmanager/
├── dashboards/
├── alerts/
└── docs/
```

## Quick Install

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts

helm upgrade --install monitoring prometheus-community/kube-prometheus-stack \
  -n monitoring --create-namespace -f helm/prometheus/values.yaml

helm upgrade --install loki grafana/loki-stack \
  -n monitoring -f helm/loki/values.yaml
```

## SLO Example

- Availability SLO: 99.9%
- Latency SLO: p99 < 300 ms
- Error budget burn rate alerts
