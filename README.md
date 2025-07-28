
# 🚀 Maru Cloud Hosting – Onboarding MVP

This is a serverless, event-driven onboarding prototype for **Maru Cloud Hosting**, built using the **AWS Serverless Application Model (SAM)**.

It provisions the following infrastructure:
- **API Gateway** for tenant registration endpoint
- **Lambda function** to emit onboarding events
- **Amazon EventBridge** to route onboarding events
- **AWS Step Functions** to orchestrate provisioning
- **Provisioning Lambda** to prepare tenant folder & metadata

---

## 📁 Project Structure

```

maru-onboarding-sam/
├── template.yaml                    # Main SAM template
├── statemachines/
│   └── onboarding.asl.json         # Step Function definition
├── functions/
│   ├── register\_tenant/            # Lambda to trigger onboarding
│   │   └── app.py
│   └── provision\_tenant/           # Lambda to setup tenant
│       └── app.py
├── events/                         # Optional test events
│   └── register-test-event.json
├── README.md

````

---

## 🔄 Flow

1. `GET /register?user_id=tenant123` via API Gateway
2. `register_tenant` Lambda emits a custom EventBridge event
3. EventBridge rule triggers a Step Function
4. Step Function invokes `provision_tenant` Lambda
5. Lambda logs tenant provisioning (can be extended to create S3/DynamoDB)

---

## 🧪 Test It Locally

### Build & Deploy
```bash
sam build
sam deploy --guided
````

### Trigger Registration via curl

```bash
curl "https://<api-id>.execute-api.<region>.amazonaws.com/Prod/register?user_id=tenant123"
```

---

## ✅ Extend This

* Add S3 folder creation (`sites/{tenantId}/`)
* Add DynamoDB table (`MaruTenantRegistry`)
* Register subdomain via SaaS CloudFront Manager
* Integrate AppConfig for tenant-specific feature flags
* Add CI/CD pipeline (GitHub Actions or CodePipeline)

---

## 📜 License

MIT © MaruCloudHosting

---

## 🙌 Contributors

Built by the Maru Cloud Hosting Team — for scalable, serverless SaaS platforms.

```

---

Would you like me to generate the Git commands to push this into a new GitHub repository?
```
