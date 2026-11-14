---
title: "What about logging & monitoring?"
space: "Customer Guide"
url: "https://docs.frappe.io/customer-guide/security/logging-monitoring"
updated: "2026-07-02"
---

## Visibility Is Essential to Security

Security is not only about preventing incidents - it is also about being able to detect, investigate, and respond when something unusual occurs.



For this reason, modern cloud platforms rely heavily on monitoring and logging systems that provide visibility into the health, performance, and behavior of systems.



Frappe Cloud incorporates monitoring and logging systems that allow the platform team to observe infrastructure activity, detect anomalies, and respond to operational events.



These systems form a critical part of the platform’s operational security model.



---



## Infrastructure Monitoring

Infrastructure monitoring systems track the health and performance of servers and application environments across the platform.



Monitoring systems collect metrics related to:



- CPU usage 
- Memory usage 
- Disk capacity 
- Network activity 
- Application performance 
- Database queries





These metrics help identify abnormal behavior that may indicate system issues, performance degradation, or potential security concerns.



Automated alerts notify the engineering team when certain thresholds are exceeded or when abnormal conditions are detected.



---



## Log Collection and Analysis

Operational logs provide detailed records of system events.



Frappe Cloud collects logs from multiple sources within the platform, including:



- Application logs 
- System logs 
- Deployment logs 
- Database performance logs 
- Error logs 
- Scheduler and background job logs





These logs are aggregated and analyzed using centralized logging systems.



Centralized logging allows engineers to quickly investigate issues, trace operational events, and identify patterns that may indicate security risks.



---



## Customer-Visible Logs

Customers also have access to several logs through the Frappe Cloud dashboard.



These may include:



- Application error logs 
- Background job logs 
- Slow query logs 
- Deployment logs





Access to these logs helps customers troubleshoot issues within their application environments and maintain visibility into system activity.



---



## Monitoring Tools

Frappe Cloud uses a combination of monitoring tools to observe infrastructure and application behavior.



These systems typically include tools such as:



- **Prometheus** for metrics collection 
- **Grafana** for visualization and dashboards 
- **ElasticSearch and Kibana** for log aggregation and analysis 
- **Alertmanager** for alert routing and incident notifications





These tools provide the operational visibility required to maintain platform reliability and security.



---



## Incident Detection

Monitoring systems continuously analyze operational signals to detect issues such as:



- Resource exhaustion 
- Infrastructure failures 
- Application errors 
- Unusual traffic patterns 
- Performance anomalies





When abnormal conditions are detected, alerts are generated so that engineers can investigate and respond.



This early detection capability helps prevent small issues from escalating into larger service disruptions.



---



## Operational Accountability

Logs also provide an important accountability mechanism.



Operational records allow engineers to review historical events and understand:



- What actions were taken 
- When those actions occurred 
- Which systems were affected





This transparency supports incident investigation and helps improve operational processes over time.



---



## Continuous Improvement

Monitoring and logging systems are not only used for troubleshooting. They also provide insights that help improve the platform.



Operational data allows engineering teams to:



- Identify recurring issues 
- Improve system performance 
- Strengthen reliability 
- Enhance security protections





Over time, this feedback loop contributes to a more resilient and secure cloud platform.



---