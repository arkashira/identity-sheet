# Breakeven Analysis – identity‑sheet

| Item | Value | Notes |
|------|-------|-------|
| **Compute cost per active user** | **$0.02 / mo** | 1 m CPU‑hour/month on AWS Fargate (shared across 1000 users) |
| **Storage cost per active user** | **$0.01 / mo** | 5 GB per user on S3 (infrequent access) |
| **Bandwidth cost per active user** | **$0.01 / mo** | 1 GB egress per user (average) |
| **Total variable cost per active user** | **$0.04 / mo** | Sum of above |

---

## Pricing Tiers

| Tier | Price / mo | Core Features | Add‑ons |
|------|------------|---------------|---------|
| **Starter** | **$5** | • Unlimited sheets<br>• Identity‑based refs<br>• 10 GB storage<br>• Email support | • None |
| **Pro** | **$15** | • All Starter<br>• 100 GB storage<br>• Advanced audit logs<br>• Priority email support | • API access (per‑user) |
| **Enterprise** | **$50** | • All Pro<br>• Unlimited storage<br>• SSO & SAML<br>• Dedicated account manager | • Custom integrations |

---

## Customer Acquisition Cost (CAC)

| Channel | CAC estimate |
|---------|--------------|
| Paid ads | $30 |
| Partner referrals | $15 |
| Organic (content) | $10 |
| **Average CAC** | **$18** |

---

## Lifetime Value (LTV)

| Tier | Avg. churn (mo) | LTV |
|------|-----------------|-----|
| Starter | 12 mo | $5 × 12 = $60 |
| Pro | 18 mo | $15 × 18 = $270 |
| Enterprise | 24 mo | $50 × 24 = $1,200 |

*Assumes 10 % monthly churn for Starter, 5 % for Pro, 4 % for Enterprise.*

---

## Break‑Even Users Count

| Tier | Monthly revenue per user | Monthly cost per user | Net margin per user | Break‑even users |
|------|--------------------------|-----------------------|---------------------|------------------|
| Starter | $5 | $0.04 | $4.96 | **≈ 4 000** |
| Pro | $15 | $0.04 | $14.96 | **≈ 1 300** |
| Enterprise | $50 | $0.04 | $49.96 | **≈ 400** |

*Break‑even defined as cumulative net margin = 0.*

---

## Path to $10 K MRR

| Tier | Users needed | Monthly revenue |
|------|--------------|-----------------|
| Starter | 2 000 | $10 000 |
| Pro | 667 | $10 000 |
| Enterprise | 200 | $10 000 |

*Optimal mix (based on projected conversion rates 70 % Starter, 25 % Pro, 5 % Enterprise):*

- 1 400 Starter → $7 000  
- 400 Pro → $6 000  
- 100 Enterprise → $5 000  

Total = **$18 000 MRR** (overshoot, but realistic for early growth).  

**Key take‑away:**  
- **Starter** is the most scalable path to quick breakeven.  
- **Pro** users drive higher LTV and margin, so focus on upsell.  
- **Enterprise** is a high‑margin anchor; aim for 5–10% of the user base.