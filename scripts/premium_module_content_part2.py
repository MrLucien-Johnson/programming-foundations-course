MODULES = {
    "azure/01-azure-foundations": {
        "goals": [
            "Explain the relationship among an Entra tenant, management groups, subscriptions, resource groups, and resources",
            "Choose an Azure region and paired-region strategy using latency, compliance, and service availability",
            "Create and inspect a resource group safely with Azure CLI",
        ],
        "why": "Azure's hierarchy determines ownership, policy scope, billing, and blast radius. Getting it right before deployment prevents tangled permissions and expensive cleanup.",
        "ideas": [
            "**Scope hierarchy** — management group → subscription → resource group → resource; settings commonly inherit downward.",
            "**Resource groups are lifecycle boundaries** — group resources that are deployed, owned, and removed together.",
            "**Regions and availability zones solve different failures** — zones isolate datacentres within a region; paired regions support regional recovery planning.",
            "**Shared responsibility remains workload-specific** — Microsoft secures the cloud; you still secure identities, data, configuration, and code.",
        ],
        "example": """### Lab: establish a safe Azure scope

```bash
az login
az account list --output table
az account set --subscription "<subscription-id>"
az group create --name rg-learning-web --location uksouth \
  --tags owner=student environment=lab
az group show --name rg-learning-web --output table
```

Record the selected tenant, subscription, region, tags, and cleanup owner. Remove the lab when finished with `az group delete --name rg-learning-web --yes --no-wait`.""",
        "practice": [
            "Draw the Azure hierarchy for a company with production and sandbox subscriptions.",
            "Compare two candidate regions with `az account list-locations --output table` and document the decision.",
            "Create a tagged lab resource group, inspect its resource ID, then delete it.",
        ],
        "mistakes": [
            "Treating a resource group as a network or identity security boundary",
            "Deploying before confirming the active subscription and tenant",
            "Choosing a region without checking required service and SKU availability",
        ],
        "stretch": "Design a management-group hierarchy that separates platform, production, and sandbox policy scope.",
        "quiz": [
            ("Which Azure scope directly contains resources?", ["Tenant", "Resource group", "Region pair", "Availability zone"], 1),
            ("Why group resources by lifecycle?", ["They can be deployed and removed together", "It creates a new tenant", "It guarantees zero cost", "It replaces RBAC"], 0),
            ("What does an availability zone primarily isolate?", ["Subscriptions", "Identity providers", "Datacentre failures within a region", "Billing accounts"], 2),
            ("Which command selects the CLI subscription?", ["az group use", "az account set", "az tenant deploy", "az region select"], 1),
            ("Under shared responsibility, who configures application access?", ["Only Microsoft", "The customer", "The hardware vendor", "Nobody"], 1),
        ],
    },
    "azure/02-entra-id-and-rbac": {
        "goals": [
            "Distinguish Entra authentication from Azure RBAC authorization",
            "Assign a least-privilege role at the narrowest practical scope",
            "Prefer managed identities over application secrets for Azure-hosted workloads",
        ],
        "why": "Most damaging cloud incidents begin with excessive or persistent credentials. Entra ID and Azure RBAC let teams prove identity and constrain what that identity can do.",
        "ideas": [
            "**Authentication is who; authorization is what** — Entra verifies identities, while RBAC role assignments grant actions at a scope.",
            "**A role assignment has three parts** — security principal, role definition, and scope.",
            "**Inheritance expands reach** — subscription-level access flows into every child resource group unless constrained.",
            "**Managed identity removes secret distribution** — Azure issues and rotates workload credentials for supported services.",
        ],
        "example": """### Lab: grant read-only access to one resource group

```bash
RG_ID=$(az group show -n rg-learning-web --query id -o tsv)
USER_ID=$(az ad signed-in-user show --query id -o tsv)
az role assignment create \
  --assignee-object-id "$USER_ID" \
  --assignee-principal-type User \
  --role Reader --scope "$RG_ID"
az role assignment list --scope "$RG_ID" --all --output table
```

Use `az role assignment delete` after the exercise. For an App Service, enable a workload identity with `az webapp identity assign --resource-group rg-learning-web --name <app-name>`.""",
        "practice": [
            "Map Reader, Contributor, and User Access Administrator to concrete allowed and denied tasks.",
            "Create a Reader assignment at resource-group scope and verify it with the CLI.",
            "Explain how a managed identity reaches Key Vault without embedding a client secret.",
        ],
        "mistakes": [
            "Granting Owner when a data-plane or Reader role is enough",
            "Confusing an Entra directory role with an Azure resource role",
            "Putting service-principal secrets in source code or pipeline logs",
        ],
        "stretch": "Create a custom-role design that permits restart and status checks but not deletion or role assignment.",
        "quiz": [
            ("What does Azure RBAC decide?", ["Which identity signed in", "What an identity may do at a scope", "Which region is paired", "How DNS resolves"], 1),
            ("What are the parts of a role assignment?", ["Principal, role, scope", "VNet, subnet, NSG", "Tenant, zone, disk", "Metric, log, trace"], 0),
            ("Why use a managed identity?", ["It creates public access", "Azure manages workload credentials", "It bypasses RBAC", "It grants Owner automatically"], 1),
            ("Which scope is least broad for one application's resources?", ["Management group", "Subscription", "Resource group", "Tenant"], 2),
            ("Which role can normally view resources without changing them?", ["Owner", "Reader", "Contributor", "Global Administrator"], 1),
        ],
    },
    "azure/03-vnet-networking": {
        "goals": [
            "Plan non-overlapping VNet and subnet CIDR ranges",
            "Explain routes, network security groups, private endpoints, and Azure DNS roles",
            "Test network reachability without assuming that a public IP is required",
        ],
        "why": "A VNet is the connectivity and isolation foundation for Azure workloads. Address mistakes and permissive rules become difficult to repair after environments are connected.",
        "ideas": [
            "**VNets are regional private networks** — subnets divide address space; peering connects VNets without transitive routing by default.",
            "**NSGs are stateful filters** — inbound and outbound rules apply by priority to subnets or network interfaces.",
            "**Routes choose paths; NSGs permit traffic** — a valid route does not imply authorization.",
            "**Private endpoints bring PaaS privately into a VNet** — private DNS must resolve the service name to the endpoint address.",
        ],
        "example": """### Lab: create a VNet and restricted application subnet

```bash
az network vnet create -g rg-learning-web -n vnet-web \
  --address-prefix 10.40.0.0/16 \
  --subnet-name snet-app --subnet-prefix 10.40.1.0/24
az network nsg create -g rg-learning-web -n nsg-app
az network nsg rule create -g rg-learning-web --nsg-name nsg-app \
  -n allow-https --priority 100 --direction Inbound \
  --protocol Tcp --destination-port-ranges 443 \
  --source-address-prefixes 10.40.0.0/16 --access Allow
az network vnet subnet update -g rg-learning-web --vnet-name vnet-web \
  -n snet-app --network-security-group nsg-app
```

Inspect effective rules before troubleshooting the application: `az network nsg rule list -g rg-learning-web --nsg-name nsg-app -o table`.""",
        "practice": [
            "Allocate three non-overlapping `/24` subnets inside a `/16` VNet.",
            "Write an NSG rule set that allows HTTPS from a trusted source and denies unnecessary administration ports.",
            "Draw DNS resolution for a Storage private endpoint.",
        ],
        "mistakes": [
            "Using overlapping CIDRs that later block peering or VPN connectivity",
            "Opening SSH or RDP to the entire internet",
            "Creating a private endpoint without configuring or linking private DNS",
        ],
        "stretch": "Design a hub-and-spoke topology with Azure Firewall, shared DNS, and explicit spoke routes.",
        "quiz": [
            ("Are Azure VNet peerings transitive by default?", ["Yes, always", "No", "Only across zones", "Only for IPv6"], 1),
            ("What does an NSG primarily control?", ["DNS records", "Allowed inbound and outbound flows", "Subscription billing", "Disk encryption keys"], 1),
            ("Why must connected VNets avoid overlapping CIDRs?", ["Peering cannot route ambiguous addresses", "NSGs require public IPs", "Azure DNS stops globally", "Tags become invalid"], 0),
            ("What commonly accompanies a private endpoint?", ["A public load balancer", "A private DNS zone/link", "A second tenant", "An Owner assignment"], 1),
            ("A route to a VM exists. Does that guarantee traffic is allowed?", ["Yes", "No; NSGs or firewalls may still deny it", "Only on weekends", "Only for UDP"], 1),
        ],
    },
    "azure/04-compute-options": {
        "goals": [
            "Select among Virtual Machines, VM Scale Sets, Container Apps, Functions, and AKS",
            "Recognize the operational trade-off between control and managed abstractions",
            "Create and inspect a minimal VM while controlling access and cost",
        ],
        "why": "Azure offers multiple valid compute models. Choosing the least operationally demanding model that satisfies workload constraints keeps teams focused on application value.",
        "ideas": [
            "**VMs maximize control and responsibility** — you patch the OS, harden access, and plan availability.",
            "**Scale Sets provide a uniform VM fleet** — instances scale from an image and health model.",
            "**Container Apps and Functions reduce infrastructure work** — they suit HTTP, event, and job workloads with platform constraints.",
            "**AKS is justified by Kubernetes needs** — it adds cluster, networking, and workload operational complexity.",
        ],
        "example": """### Lab: create an inexpensive Linux VM without public inbound access

```bash
az vm create -g rg-learning-web -n vm-lab \
  --image Ubuntu2204 --size Standard_B1s \
  --admin-username azureuser --generate-ssh-keys \
  --public-ip-address '""'
az vm show -g rg-learning-web -n vm-lab \
  --show-details --query "{state:powerState,privateIp:privateIps}" -o yaml
az vm deallocate -g rg-learning-web -n vm-lab
```

Use Bastion, VPN, or a controlled run-command path rather than adding a broad public SSH rule.""",
        "practice": [
            "Create a decision table for VM, Functions, Container Apps, and AKS using control, scaling, and operations.",
            "Deploy, inspect, deallocate, and delete a lab VM.",
            "Estimate whether a steady service or bursty event handler benefits from consumption pricing.",
        ],
        "mistakes": [
            "Selecting AKS merely because the application ships as a container",
            "Leaving lab VMs allocated after use",
            "Treating automatic scaling as a substitute for load testing and resource limits",
        ],
        "stretch": "Draft a VM Scale Set design with health probes, zone distribution, and immutable image rollout.",
        "quiz": [
            ("Which option gives the most OS control?", ["Azure Functions", "Virtual Machines", "Container Apps", "Logic Apps"], 1),
            ("What is a VM Scale Set designed to manage?", ["A uniform autoscaling VM fleet", "Only DNS zones", "SQL schemas", "Entra users"], 0),
            ("Which workload naturally fits Functions?", ["A persistent custom hypervisor", "A short event-triggered handler", "A stateful legacy appliance", "A desktop GUI"], 1),
            ("What does `az vm deallocate` help stop?", ["Only logs", "Compute charges for the allocated VM", "The subscription", "RBAC inheritance"], 1),
            ("When is AKS a stronger choice?", ["When Kubernetes APIs and ecosystem are actual requirements", "For every static page", "To avoid all operations", "When no containers exist"], 0),
        ],
    },
    "azure/05-storage-and-blobs": {
        "goals": [
            "Choose Blob, Files, Queue, or Table storage for a workload",
            "Configure redundancy, access tiers, lifecycle rules, and public-access controls",
            "Upload and verify a blob using identity-based authorization",
        ],
        "why": "Storage choices affect durability, recovery, performance, security, and recurring cost. Secure defaults matter because a single anonymous container can expose an entire dataset.",
        "ideas": [
            "**A storage account is the namespace and policy boundary** for Blob, Files, Queues, and Tables.",
            "**Redundancy matches failure tolerance** — LRS, ZRS, GRS, and GZRS protect against different scopes at different prices.",
            "**Blob tiers and lifecycle policies manage economics** — hot, cool, cold, and archive trade access cost for storage cost.",
            "**Use Entra ID and RBAC for data operations** instead of long-lived account keys where possible.",
        ],
        "example": """### Lab: create private Blob storage and upload with Entra credentials

```bash
ACCOUNT="stlab$RANDOM$RANDOM"
az storage account create -g rg-learning-web -n "$ACCOUNT" \
  -l uksouth --sku Standard_ZRS --kind StorageV2 \
  --allow-blob-public-access false --min-tls-version TLS1_2
az storage container create --account-name "$ACCOUNT" \
  --name uploads --auth-mode login
printf 'hello azure\n' > /tmp/azure-lab.txt
az storage blob upload --account-name "$ACCOUNT" \
  --container-name uploads --name hello.txt \
  --file /tmp/azure-lab.txt --auth-mode login
az storage blob list --account-name "$ACCOUNT" \
  --container-name uploads --auth-mode login -o table
```""",
        "practice": [
            "Match object, shared-file, message, and key-value needs to Azure Storage services.",
            "Create a private container and prove anonymous access is unavailable.",
            "Write a lifecycle policy that moves old logs to cool storage and later deletes them.",
        ],
        "mistakes": [
            "Sharing storage account keys as application configuration",
            "Choosing geo-redundancy without understanding failover and data residency",
            "Moving frequently read objects to archive and incurring retrieval delay and cost",
        ],
        "stretch": "Add soft delete, versioning, and a private endpoint, then document the restore and DNS paths.",
        "quiz": [
            ("Which service stores unstructured objects?", ["Azure Blob Storage", "Azure Files only", "Azure Queue only", "Entra ID"], 0),
            ("What does ZRS replicate across?", ["Tenants", "Availability zones in a region", "Every Azure region", "Subscriptions"], 1),
            ("Which authorization avoids account keys?", ["Anonymous access", "Entra ID with Azure RBAC", "Public container access", "HTTP without TLS"], 1),
            ("What is Archive tier optimized for?", ["Constant low-latency reads", "Rarely accessed data tolerant of rehydration delay", "VM boot disks", "Message queues"], 1),
            ("Why enable blob versioning or soft delete?", ["To aid recovery from overwrite or deletion", "To create VNets", "To remove encryption", "To grant Owner"], 0),
        ],
    },
    "azure/06-app-service": {
        "goals": [
            "Deploy a web application to an App Service plan",
            "Use deployment slots and application settings for safer releases",
            "Configure health checks, logs, managed identity, and scale intentionally",
        ],
        "why": "App Service provides managed web hosting without requiring VM or cluster administration, while still supporting release, networking, identity, and observability controls.",
        "ideas": [
            "**The plan supplies compute; the app supplies runtime configuration** — plan tier determines scaling and feature availability.",
            "**Deployment slots separate validation from production** — mark environment-specific settings as slot settings before swap.",
            "**Application settings become environment variables** — secrets should be Key Vault references, not literal values in source.",
            "**Health checks and autoscale need meaningful signals** — a process being alive is weaker than a dependency-aware readiness check.",
        ],
        "example": """### Lab: deploy and inspect a Linux web app

```bash
az appservice plan create -g rg-learning-web -n plan-web \
  --is-linux --sku B1
az webapp create -g rg-learning-web -p plan-web -n <globally-unique-app> \
  --runtime "PYTHON:3.12"
az webapp config appsettings set -g rg-learning-web -n <app-name> \
  --settings APP_ENV=lab
az webapp log config -g rg-learning-web -n <app-name> \
  --application-logging filesystem --level information
az webapp log tail -g rg-learning-web -n <app-name>
```

On tiers supporting slots, create one with `az webapp deployment slot create ... --slot staging`, validate it, then swap deliberately.""",
        "practice": [
            "Deploy a hello application and locate its default hostname and outbound addresses.",
            "Create a staging-slot checklist covering migrations, settings, health, and rollback.",
            "Enable a managed identity and describe a Key Vault reference flow.",
        ],
        "mistakes": [
            "Swapping a slot before marking environment-specific settings as sticky",
            "Storing production secrets directly in application settings or source",
            "Scaling instances without checking database, connection, and session behavior",
        ],
        "stretch": "Add VNet integration for outbound private access and explain how it differs from a private endpoint for inbound access.",
        "quiz": [
            ("What determines App Service compute capacity?", ["The App Service plan", "The resource-group name", "The DNS TXT record", "The Entra tenant name"], 0),
            ("Why use a deployment slot?", ["To validate a release before swapping traffic", "To replace all backups", "To create a VNet", "To disable TLS"], 0),
            ("Where should an app obtain a sensitive setting?", ["Committed `.env` file", "Key Vault through managed identity", "Public blob", "Container image label"], 1),
            ("What should a health endpoint represent?", ["Only that DNS exists", "Whether the instance can serve meaningful traffic", "The billing currency", "The Git branch"], 1),
            ("Does adding instances automatically fix a database bottleneck?", ["Always", "No; dependencies need capacity and connection planning", "Only in Free tier", "Only without logs"], 1),
        ],
    },
    "azure/07-azure-sql-and-data": {
        "goals": [
            "Differentiate Azure SQL Database, Managed Instance, and SQL on Azure VMs",
            "Configure identity, network access, backups, and service tiers for a database",
            "Test connectivity without exposing the server broadly",
        ],
        "why": "Managed databases remove much routine infrastructure work, but schema, identity, query performance, network exposure, and recovery objectives remain application responsibilities.",
        "ideas": [
            "**Choose the least infrastructure needed** — SQL Database suits cloud applications; Managed Instance adds broader SQL Server compatibility; VMs retain OS control.",
            "**Logical servers are management endpoints** — databases have independent compute and storage characteristics.",
            "**Private connectivity and Entra authentication reduce exposure** — firewall exceptions should be narrow and temporary.",
            "**Backups are useful only with recovery objectives** — understand point-in-time retention, geo-restore, and restore testing.",
        ],
        "example": """### Lab: create a small Azure SQL database

```bash
az sql server create -g rg-learning-web -n <unique-sql-server> \
  -l uksouth -u sqladmin -p '<strong-temporary-password>'
az sql db create -g rg-learning-web -s <unique-sql-server> \
  -n appdb --service-objective Basic --backup-storage-redundancy Local
az sql db show -g rg-learning-web -s <unique-sql-server> \
  -n appdb --query "{status:status,tier:currentServiceObjectiveName}" -o yaml
az sql db list-usages -g rg-learning-web -s <unique-sql-server> \
  -n appdb -o table
```

For a real workload, configure an Entra administrator, private endpoint, and private DNS rather than leaving broad public firewall rules.""",
        "practice": [
            "Compare managed database options for a new API and a lift-and-shift SQL Server application.",
            "Write RPO and RTO targets, then map them to a restore strategy.",
            "Inspect query performance recommendations and identify one index or query hypothesis.",
        ],
        "mistakes": [
            "Adding a `0.0.0.0/0`-style broad firewall range for convenience",
            "Assuming platform backups eliminate the need to test restores",
            "Scaling compute before investigating slow queries and indexes",
        ],
        "stretch": "Design failover-group behavior for two regions, including connection endpoints and failover criteria.",
        "quiz": [
            ("Which option generally requires the most OS administration?", ["Azure SQL Database", "Managed Instance", "SQL Server on Azure VM", "Serverless SQL Database"], 2),
            ("What does point-in-time restore address?", ["Recovery to an earlier database state", "VNet peering", "Role inheritance", "Image deployment"], 0),
            ("Why prefer a private endpoint?", ["It provides private network reachability to the service", "It disables authentication", "It removes backups", "It grants public access"], 0),
            ("Before increasing database compute, what should you inspect?", ["Query plans, waits, and indexes", "Resource-group color", "DNS TTL only", "Git tags"], 0),
            ("Which pair describes recovery requirements?", ["CPU and RAM", "RPO and RTO", "CIDR and ASN", "RBAC and NSG"], 1),
        ],
    },
    "azure/08-monitor-and-insights": {
        "goals": [
            "Distinguish Azure Monitor metrics, Log Analytics logs, Application Insights telemetry, and alerts",
            "Write a useful KQL query for an application symptom",
            "Create an actionable alert with an owner and response note",
        ],
        "why": "Telemetry shortens the time from user impact to diagnosis. Azure Monitor is most valuable when signals are tied to service objectives and a clear response.",
        "ideas": [
            "**Metrics are numeric time series; logs are rich records** — use each according to the question.",
            "**Application Insights correlates requests, dependencies, exceptions, and traces** through distributed operation identifiers.",
            "**KQL transforms evidence into answers** — filter early, summarize deliberately, and preserve timestamps and dimensions.",
            "**Actionable alerts need symptom, threshold, duration, recipient, and runbook** — otherwise they become noise.",
        ],
        "example": """### Lab: query failed requests and inspect resource metrics

```kusto
requests
| where timestamp > ago(30m)
| where success == false
| summarize failures=count(), p95=percentile(duration, 95)
    by operation_Name, bin(timestamp, 5m)
| order by timestamp desc
```

```bash
RESOURCE_ID=$(az webapp show -g rg-learning-web -n <app-name> --query id -o tsv)
az monitor metrics list --resource "$RESOURCE_ID" \
  --metric Http5xx --interval PT5M --output table
az monitor app-insights component show -g rg-learning-web \
  --app <insights-name> -o table
```""",
        "practice": [
            "Write KQL that finds the most common exception type in the last hour.",
            "Define a latency or error-rate alert using a user-visible threshold and evaluation window.",
            "Build a small incident dashboard with traffic, errors, latency, and saturation.",
        ],
        "mistakes": [
            "Alerting on every individual error without rate, duration, or impact context",
            "Logging secrets, access tokens, or unnecessary personal data",
            "Keeping high-volume debug telemetry forever without sampling or retention policy",
        ],
        "stretch": "Add an availability test and correlate a failed probe to dependency telemetry and a deployment event.",
        "quiz": [
            ("Which language queries Log Analytics data?", ["SQL only", "KQL", "HCL", "Bicep only"], 1),
            ("What does Application Insights dependency telemetry show?", ["Calls to downstream services", "Only subscription invoices", "VNet CIDR allocation", "Role definitions"], 0),
            ("What makes an alert actionable?", ["A symptom, threshold, owner, and response", "A random metric", "No recipient", "Infinite sensitivity"], 0),
            ("Which signal best represents request latency distribution?", ["A percentile such as p95", "Resource-group count", "Tag length", "Tenant ID"], 0),
            ("Why control telemetry retention?", ["To balance investigation, compliance, and cost", "To disable all metrics", "To create zones", "To avoid RBAC"], 0),
        ],
    },
    "azure/09-governance-and-cost": {
        "goals": [
            "Apply tags, Azure Policy, locks, budgets, and management groups at appropriate scopes",
            "Interpret Azure Cost Management data before optimizing",
            "Separate preventive governance from monitoring and financial alerts",
        ],
        "why": "Cloud self-service scales only when guardrails make ownership, compliance, and cost visible without forcing every safe decision through a central team.",
        "ideas": [
            "**Policy evaluates resource state** — deny, audit, modify, or deploy-if-not-exists effects enforce standards.",
            "**Tags describe ownership and allocation** — policy can require or inherit them, but tags are not access controls.",
            "**Locks protect against accidental changes** — `CanNotDelete` and `ReadOnly` do not replace authorization.",
            "**Budgets alert; they do not automatically stop spend** — pair alerts with accountable review and approved automation.",
        ],
        "example": """### Lab: inspect cost and add a deletion guard

```bash
SCOPE=$(az group show -n rg-learning-web --query id -o tsv)
az tag update --resource-id "$SCOPE" --operation merge \
  --tags owner=student cost-center=training environment=lab
az lock create --name protect-lab --lock-type CanNotDelete \
  --resource-group rg-learning-web \
  --notes "Remove only during documented cleanup"
az policy assignment list --scope "$SCOPE" --output table
az consumption usage list --start-date 2026-08-01 \
  --end-date 2026-08-07 --output table
```

Remove the lock before intentional teardown: `az lock delete --name protect-lab --resource-group rg-learning-web`.""",
        "practice": [
            "Define required `owner`, `environment`, `service`, and `cost-center` tags.",
            "Compare an Audit policy with a Deny policy and plan a safe rollout from compliance reporting.",
            "Create a budget design with 50%, 80%, and forecasted-100% notifications.",
        ],
        "mistakes": [
            "Rolling out Deny broadly before evaluating existing resources and exemptions",
            "Assuming a budget hard-caps or shuts down Azure services",
            "Using tags as if they prevent unauthorized resource access",
        ],
        "stretch": "Design a policy initiative for allowed regions, required tags, secure transport, and diagnostic settings.",
        "quiz": [
            ("Which Policy effect blocks a noncompliant creation?", ["Audit", "Deny", "Disabled", "Append-only log"], 1),
            ("Do Azure budgets automatically cap all spending?", ["Yes", "No; they primarily generate alerts", "Only for VNets", "Only for tags"], 1),
            ("What does a `CanNotDelete` lock prevent?", ["Reading metrics", "Deletion while allowing authorized updates", "All billing", "User sign-in"], 1),
            ("Are tags an authorization mechanism?", ["Yes", "No", "Only in production", "Only on VMs"], 1),
            ("Why begin policy rollout with Audit?", ["To understand impact before enforcement", "To delete every resource", "To bypass RBAC", "To stop telemetry"], 0),
        ],
    },
    "azure/10-capstone-azure-app": {
        "goals": [
            "Deploy a small Azure web application with managed identity, private data, and telemetry",
            "Demonstrate a staged release, failure signal, rollback, and cleanup path",
            "Present architecture and operational evidence rather than only a successful URL",
        ],
        "why": "A capstone proves that identity, compute, data, networking, monitoring, governance, and cost decisions work together as an operable service.",
        "ideas": [
            "**Build the smallest complete service** — App Service or Container Apps, Storage or Azure SQL, and Application Insights are enough.",
            "**Identity replaces embedded secrets** — grant the app's managed identity only its required data role.",
            "**Production readiness is observable** — health, failures, latency, deploy version, and cost ownership must be visible.",
            "**A capstone includes teardown** — reproducible cleanup is part of responsible cloud engineering.",
        ],
        "example": """### Capstone: deploy, observe, and prove

```bash
az group create -n rg-capstone-web -l uksouth \
  --tags owner=student environment=capstone
az appservice plan create -g rg-capstone-web -n plan-capstone \
  --is-linux --sku B1
az webapp create -g rg-capstone-web -p plan-capstone \
  -n <unique-app-name> --runtime "NODE:20-lts"
PRINCIPAL_ID=$(az webapp identity assign -g rg-capstone-web \
  -n <unique-app-name> --query principalId -o tsv)
az webapp config appsettings set -g rg-capstone-web \
  -n <unique-app-name> --settings RELEASE_SHA="$(git rev-parse --short HEAD)"
```

Add private storage, assign `Storage Blob Data Contributor` at container or account scope, enable Application Insights, then capture a healthy request and a controlled failure. Document rollback and run `az group delete -n rg-capstone-web --yes --no-wait` after assessment.""",
        "practice": [
            "Create an architecture diagram showing trust boundaries, identities, ingress, and data flow.",
            "Run a five-minute demonstration: deploy, health check, telemetry query, staged update, and rollback.",
            "Record resource inventory, estimated cost, role assignments, and cleanup evidence.",
        ],
        "mistakes": [
            "Using Owner permissions or storage keys to make the demo work quickly",
            "Showing only the happy-path homepage with no operational evidence",
            "Leaving paid resources, public endpoints, or test data after the capstone",
        ],
        "stretch": "Provision the capstone declaratively with Bicep or Terraform and add a private endpoint plus custom-domain TLS.",
        "quiz": [
            ("What makes the capstone operationally complete?", ["A URL only", "Identity, telemetry, release, rollback, cost, and cleanup evidence", "An Owner role", "A screenshot of the portal"], 1),
            ("How should the app access Azure Storage?", ["An account key in Git", "Managed identity with a narrow data role", "Anonymous public access", "A user's password"], 1),
            ("Why expose a release SHA in telemetry?", ["To correlate behavior with a deployment", "To replace TLS", "To create a tenant", "To reduce storage durability"], 0),
            ("What should the architecture diagram include?", ["Only product logos", "Trust boundaries and data flow", "Passwords", "Every Azure SKU"], 1),
            ("What is the final capstone operation?", ["Leave resources running", "Verify cleanup and residual cost", "Disable logging first", "Make storage public"], 1),
        ],
    },
    "gcp/01-gcp-foundations": {
        "goals": [
            "Explain the GCP resource hierarchy from organization and folders to projects and resources",
            "Select a region or zone based on availability, latency, residency, and service support",
            "Initialize `gcloud`, choose a project explicitly, and inspect enabled services",
        ],
        "why": "Projects are GCP's central boundary for APIs, IAM, quotas, and billing. Deliberate project and location choices keep experiments isolated and production governable.",
        "ideas": [
            "**Organization → folders → projects → resources** provides inheritance for IAM and organization policies.",
            "**Projects are durable isolation boundaries** — every project has a name, immutable project ID, and numeric project number.",
            "**Regions contain zones** — regional services can survive zonal failure; multi-region services trade control for broader placement.",
            "**APIs are enabled per project** — permission alone is insufficient when the service API is disabled.",
        ],
        "example": """### Lab: establish explicit GCP context

```bash
gcloud auth login
gcloud projects list
gcloud config configurations create cloud-course
gcloud config set project <project-id>
gcloud config set compute/region europe-west1
gcloud config set compute/zone europe-west1-b
gcloud services list --enabled
gcloud auth list
```

Confirm the project printed by `gcloud config list --format='text(core.project)'` before creating or deleting anything.""",
        "practice": [
            "Draw a folder and project hierarchy for platform, production, development, and sandbox teams.",
            "Compare two regions for service availability and data-residency requirements.",
            "Create a named CLI configuration and verify project, account, region, and zone.",
        ],
        "mistakes": [
            "Confusing a project's display name with its globally unique project ID",
            "Running commands against the previously active project",
            "Assuming all services and machine types exist in every region or zone",
        ],
        "stretch": "Design a project-factory checklist covering billing attachment, APIs, labels, logging, and baseline IAM.",
        "quiz": [
            ("What is the normal parent of a GCP resource such as a VM?", ["A project", "A billing export table", "A zone pair", "A service account key"], 0),
            ("Which project identifier is globally unique and immutable?", ["Display name", "Project ID", "Folder name", "Label value"], 1),
            ("Where are service APIs enabled?", ["Per project", "Per laptop only", "Per subnet", "Per user password"], 0),
            ("What does a GCP region contain?", ["Organizations", "Zones", "Billing accounts", "IAM roles"], 1),
            ("Which command shows active gcloud configuration?", ["gcloud config list", "gcloud vm login", "gcloud iam assume", "gcloud region use"], 0),
        ],
    },
    "gcp/02-iam-and-org-policy": {
        "goals": [
            "Model GCP IAM as principal, role, resource, and inherited policy",
            "Use predefined roles and service-account impersonation instead of broad basic roles and keys",
            "Explain how organization policies constrain configurations independently of IAM",
        ],
        "why": "GCP IAM controls who can act, while organization policy constrains which configurations are allowed. Both are needed to reduce privilege and enforce guardrails at scale.",
        "ideas": [
            "**Allow policies bind principals to roles on resources** and inherit down the resource hierarchy.",
            "**Predefined roles are usually safer than basic Owner/Editor/Viewer roles** because they express narrower service permissions.",
            "**Service accounts are workload identities** — short-lived tokens and impersonation avoid downloadable keys.",
            "**Organization policies set constraints** such as allowed regions or disabled service-account key creation; they do not grant API permissions.",
        ],
        "example": """### Lab: grant a service account a narrow project role

```bash
PROJECT_ID=$(gcloud config get-value project)
gcloud iam service-accounts create app-runtime \
  --display-name="Application runtime"
gcloud projects add-iam-policy-binding "$PROJECT_ID" \
  --member="serviceAccount:app-runtime@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/logging.logWriter"
gcloud projects get-iam-policy "$PROJECT_ID" \
  --flatten="bindings[].members" \
  --filter="bindings.members:app-runtime" \
  --format="table(bindings.role)"
```

For administration, test impersonation with `gcloud ... --impersonate-service-account=<service-account-email>` rather than creating a JSON key.""",
        "practice": [
            "Translate three job tasks into predefined roles at project or resource scope.",
            "Inspect inherited and direct IAM bindings for a project.",
            "Compare an IAM denial with an organization-policy constraint in a troubleshooting note.",
        ],
        "mistakes": [
            "Granting `roles/editor` to every human or workload",
            "Creating long-lived service-account keys when attached identity or impersonation works",
            "Expecting organization policy to grant a caller missing IAM permission",
        ],
        "stretch": "Design a conditional IAM binding that expires or applies only to a named resource.",
        "quiz": [
            ("What does an IAM role contain?", ["A collection of permissions", "A VPC route", "A billing invoice", "A DNS zone"], 0),
            ("What is a service account?", ["A workload identity", "A human billing user", "A subnet", "An organization folder"], 0),
            ("Why prefer impersonation over a service-account key?", ["It uses short-lived credentials", "It grants Owner automatically", "It disables audit logs", "It makes the service public"], 0),
            ("Does organization policy grant API access?", ["Yes", "No; it constrains configurations", "Only for Compute Engine", "Only at folder scope"], 1),
            ("Where does a project normally inherit IAM from?", ["Its folders and organization", "Its VM disks", "Cloud NAT", "A load balancer"], 0),
        ],
    },
    "gcp/03-vpc-networking": {
        "goals": [
            "Explain GCP's global VPC and regional subnet model",
            "Configure routes, hierarchical or VPC firewall rules, Cloud NAT, and private service access appropriately",
            "Use GCP flow and connectivity tools to diagnose a path",
        ],
        "why": "Unlike many cloud networks, a GCP VPC is global while its subnets are regional. Understanding this model prevents accidental exposure and incorrect multi-region designs.",
        "ideas": [
            "**A GCP VPC is global; subnets are regional** — one VPC can contain non-overlapping subnets in many regions.",
            "**Firewall rules are stateful and apply to VM network interfaces** using targets such as service accounts or secure network tags.",
            "**Routes select next hops** — system-generated subnet routes, custom static routes, and dynamic Cloud Router routes can coexist.",
            "**Cloud NAT gives outbound internet access without inbound public IPs**; Private Google Access reaches Google APIs from private addresses.",
        ],
        "example": """### Lab: custom-mode VPC with private VM egress design

```bash
gcloud compute networks create app-vpc --subnet-mode=custom
gcloud compute networks subnets create app-eu \
  --network=app-vpc --region=europe-west1 \
  --range=10.60.0.0/20 --enable-private-ip-google-access
gcloud compute firewall-rules create allow-internal-app \
  --network=app-vpc --direction=INGRESS --action=ALLOW \
  --rules=tcp:8080 --source-ranges=10.60.0.0/20 \
  --target-service-accounts=app-runtime@$(gcloud config get-value project).iam.gserviceaccount.com
gcloud compute routes list --filter="network:app-vpc"
```

Add Cloud Router and Cloud NAT for controlled outbound access; do not assign public VM addresses merely for package downloads.""",
        "practice": [
            "Plan two regional subnets in one global custom-mode VPC without overlap.",
            "Create a firewall rule targeted to a service account rather than all instances.",
            "Trace private VM access to Google APIs, the internet through Cloud NAT, and another region.",
        ],
        "mistakes": [
            "Describing a GCP VPC as regional or creating one VPC per zone by habit",
            "Using broad `0.0.0.0/0` SSH rules and mutable network tags",
            "Assuming Cloud NAT accepts unsolicited inbound internet connections",
        ],
        "stretch": "Design Shared VPC host and service projects with centrally managed subnets and delegated workload administration.",
        "quiz": [
            ("What is the scope of a GCP VPC network?", ["Zonal", "Regional", "Global", "Per VM"], 2),
            ("What is the scope of a GCP subnet?", ["Global", "Regional", "Organizational", "Per billing account"], 1),
            ("What does Cloud NAT primarily provide?", ["Outbound translation for private resources", "Inbound load balancing", "IAM inheritance", "DNS registration"], 0),
            ("Private Google Access helps private VMs reach what?", ["Google APIs and services", "Any inbound internet client", "Only other tenants", "Physical routers only"], 0),
            ("Which firewall target is stable for workload identity?", ["Service account", "Ephemeral external IP", "User password", "Billing label"], 0),
        ],
    },
    "gcp/04-compute-engine": {
        "goals": [
            "Create a hardened Compute Engine VM with suitable machine, disk, identity, and network settings",
            "Explain instance templates, managed instance groups, health checks, and autoscaling",
            "Choose Spot VMs only for interruption-tolerant work",
        ],
        "why": "Compute Engine offers low-level flexibility, but that flexibility includes patching, image, identity, firewall, availability, and lifecycle responsibilities.",
        "ideas": [
            "**Machine families optimize different constraints** — general purpose, compute, memory, accelerator, and cost profiles differ.",
            "**Instance templates make VM configuration repeatable** and underpin managed instance groups.",
            "**Managed instance groups repair and scale identical instances** using health checks and autoscaling signals.",
            "**Shielded VM, OS Login, and least-privilege service accounts improve the baseline** without embedded SSH keys or broad API scopes.",
        ],
        "example": """### Lab: create a private, low-cost VM

```bash
gcloud compute instances create vm-lab \
  --zone=europe-west1-b \
  --machine-type=e2-micro \
  --subnet=app-eu --no-address \
  --service-account=app-runtime@$(gcloud config get-value project).iam.gserviceaccount.com \
  --scopes=cloud-platform \
  --shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring \
  --labels=environment=lab,owner=student
gcloud compute instances describe vm-lab --zone=europe-west1-b \
  --format="yaml(status,networkInterfaces,serviceAccounts)"
gcloud compute instances stop vm-lab --zone=europe-west1-b
```""",
        "practice": [
            "Compare E2, N2, and memory-optimized machines for three workload profiles.",
            "Create and inspect a private VM, then stop and delete it.",
            "Sketch a regional managed instance group with health checks and an autoscaling target.",
        ],
        "mistakes": [
            "Using the default service account with broad historical permissions",
            "Assigning external IPs and public SSH rules to every VM",
            "Running stateful or non-checkpointed work on Spot VMs",
        ],
        "stretch": "Build an instance template and rolling-update plan with canary percentage, surge, and unavailable limits.",
        "quiz": [
            ("What makes VM creation repeatable for a managed instance group?", ["Instance template", "Billing export", "DNS policy", "IAM condition only"], 0),
            ("What does a managed instance group health check support?", ["Autohealing unhealthy instances", "Creating projects", "Encrypting IAM", "Changing invoices"], 0),
            ("Which workloads fit Spot VMs?", ["Interruption-tolerant batch jobs", "A single critical database with no replica", "Uncheckpointed long transactions", "Hardware license servers only"], 0),
            ("Why use `--no-address`?", ["To avoid an external VM IP", "To remove the internal IP", "To disable all routes", "To create a load balancer"], 0),
            ("What should the attached service account have?", ["Only required roles", "Project Owner", "No identity ever", "A downloaded key on disk"], 0),
        ],
    },
    "gcp/05-gcs-and-data": {
        "goals": [
            "Create a secure Cloud Storage bucket with location, class, and protection features chosen intentionally",
            "Use uniform bucket-level access and IAM instead of object ACLs",
            "Select appropriate managed GCP data services for relational, analytical, and document workloads",
        ],
        "why": "Cloud Storage is simple to start but its global namespace, IAM, lifecycle, retention, and egress choices have long-term security and cost consequences.",
        "ideas": [
            "**Bucket names are globally unique and bucket location is effectively permanent** — choose location before uploading data.",
            "**Uniform bucket-level access centralizes authorization in IAM** and disables object ACL complexity.",
            "**Storage classes reflect access patterns** — Standard, Nearline, Coldline, and Archive differ in minimum duration and retrieval economics.",
            "**Choose data engines by access pattern** — Cloud SQL for relational transactions, Firestore for documents, and BigQuery for analytics.",
        ],
        "example": """### Lab: create a protected bucket and lifecycle rule

```bash
BUCKET="gs://$(gcloud config get-value project)-course-data"
gcloud storage buckets create "$BUCKET" \
  --location=europe-west1 \
  --uniform-bucket-level-access \
  --public-access-prevention
printf 'event_id,value\n1,42\n' > /tmp/events.csv
gcloud storage cp /tmp/events.csv "$BUCKET/raw/events.csv"
gcloud storage ls --long "$BUCKET/raw/"
gcloud storage buckets describe "$BUCKET" \
  --format="yaml(location,storageClass,iamConfiguration)"
```

Add versioning with `gcloud storage buckets update "$BUCKET" --versioning` before testing overwrite recovery.""",
        "practice": [
            "Create a private bucket, upload an object, and verify public access prevention.",
            "Design a lifecycle rule for temporary exports and a retention policy for regulated records.",
            "Match an order database, event document store, and analytics warehouse to Cloud SQL, Firestore, and BigQuery.",
        ],
        "mistakes": [
            "Using `allUsers` IAM bindings to solve application access",
            "Choosing a bucket location without considering compute location and egress",
            "Treating retention policies as ordinary lifecycle deletion rules",
        ],
        "stretch": "Configure a customer-managed encryption key design and document the impact if the KMS key is disabled.",
        "quiz": [
            ("Why enable uniform bucket-level access?", ["To centralize authorization in IAM", "To add object ACLs", "To make every object public", "To change the project ID"], 0),
            ("Can a bucket location be freely changed in place?", ["Yes", "No; migration is normally required", "Only by renaming", "Only through IAM"], 1),
            ("Which service fits analytical SQL over large datasets?", ["BigQuery", "Cloud DNS", "Cloud NAT", "Secret Manager"], 0),
            ("What does public access prevention do?", ["Blocks public IAM/ACL exposure", "Disables encryption", "Removes authentication", "Creates signed URLs forever"], 0),
            ("Why use object versioning?", ["To recover prior object generations", "To create VPC routes", "To change storage location", "To grant Editor"], 0),
        ],
    },
    "gcp/06-cloud-run": {
        "goals": [
            "Deploy a stateless container to Cloud Run with deliberate ingress and authentication",
            "Configure revisions, traffic splitting, concurrency, scaling, and resource limits",
            "Use a service identity and Secret Manager without embedding credentials",
        ],
        "why": "Cloud Run turns a container into an autoscaling HTTPS service while preserving revision and identity controls. It is often a better fit than managing VMs or Kubernetes for stateless services.",
        "ideas": [
            "**A deployment creates an immutable revision** — configuration and image changes can receive percentages of traffic.",
            "**Scale-to-zero and request-based autoscaling fit bursty services** — minimum instances trade cost for reduced cold starts.",
            "**Ingress and IAM are separate controls** — network reachability does not automatically grant invocation.",
            "**Concurrency and CPU/memory settings affect latency, throughput, and cost** — measure rather than relying on defaults.",
        ],
        "example": """### Lab: deploy an authenticated Cloud Run service

```bash
gcloud services enable run.googleapis.com artifactregistry.googleapis.com
gcloud run deploy hello-api \
  --source=. --region=europe-west1 \
  --service-account=app-runtime@$(gcloud config get-value project).iam.gserviceaccount.com \
  --no-allow-unauthenticated \
  --ingress=all --concurrency=40 --max-instances=5 \
  --set-env-vars=APP_ENV=lab
URL=$(gcloud run services describe hello-api --region=europe-west1 \
  --format='value(status.url)')
curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" "$URL/health"
gcloud run revisions list --service=hello-api --region=europe-west1
```""",
        "practice": [
            "Deploy an authenticated service and invoke it with an identity token.",
            "Create a new revision and shift 10% of traffic to it before full promotion.",
            "Load test two concurrency settings and compare latency and instance count.",
        ],
        "mistakes": [
            "Using `--allow-unauthenticated` without an explicit public API requirement",
            "Writing durable application state to the container filesystem",
            "Setting unlimited scaling without protecting downstream database capacity",
        ],
        "stretch": "Connect Cloud Run to a private database through Direct VPC egress and retrieve credentials from Secret Manager.",
        "quiz": [
            ("What does each Cloud Run deployment create?", ["An immutable revision", "A new organization", "A VM SSH key", "A global subnet"], 0),
            ("How is private invocation commonly enforced?", ["Cloud Run IAM with an identity token", "A bucket ACL", "A public IP", "A billing label"], 0),
            ("What happens to durable files written only inside an instance?", ["They are safely replicated", "They can disappear with the instance", "They move to BigQuery", "They become secrets"], 1),
            ("Why cap maximum instances?", ["To protect downstream systems and cost", "To disable revisions", "To create public access", "To replace monitoring"], 0),
            ("What supports a canary release?", ["Revision traffic percentages", "Project renaming", "Cloud NAT ports", "Bucket retention"], 0),
        ],
    },
    "gcp/07-gke-intro": {
        "goals": [
            "Explain the GKE control plane, node, and Kubernetes workload responsibility split",
            "Create credentials for a cluster and deploy a minimal workload",
            "Choose Autopilot or Standard based on required control and operations",
        ],
        "why": "GKE provides managed Kubernetes, not operation-free Kubernetes. Teams still own workloads, policy, access, observability, upgrades, and often parts of node and network management.",
        "ideas": [
            "**Google manages the GKE control plane; responsibility for workloads remains yours** and differs between Autopilot and Standard.",
            "**Autopilot manages nodes and enforces workload resource expectations**; Standard provides deeper node and system control.",
            "**Workload Identity Federation for GKE maps Kubernetes service accounts to Google identities** without node-wide keys.",
            "**Regional clusters and maintenance policies improve availability and upgrade control** but do not fix unhealthy applications.",
        ],
        "example": """### Lab: deploy to an Autopilot cluster

```bash
gcloud container clusters create-auto course-cluster \
  --region=europe-west1 --release-channel=regular
gcloud container clusters get-credentials course-cluster \
  --region=europe-west1
kubectl create deployment web --image=nginx:1.27
kubectl set resources deployment web \
  --requests=cpu=100m,memory=128Mi \
  --limits=cpu=250m,memory=256Mi
kubectl expose deployment web --port=80 --type=ClusterIP
kubectl get pods,service -o wide
```

Delete the cluster after the lab with `gcloud container clusters delete course-cluster --region=europe-west1`.""",
        "practice": [
            "Compare GKE Autopilot and Standard for a stateless API and a privileged node agent.",
            "Deploy a resource-bounded workload and inspect its events and assigned node.",
            "Describe how a Kubernetes service account obtains a Google API identity.",
        ],
        "mistakes": [
            "Creating a cluster when Cloud Run would satisfy the workload",
            "Using node service-account permissions for every pod",
            "Ignoring release channels, maintenance windows, and version skew",
        ],
        "stretch": "Configure Workload Identity Federation for one pod and prove it can access one bucket but not list all projects.",
        "quiz": [
            ("What does Autopilot primarily manage beyond the control plane?", ["Node infrastructure", "Application code", "Database schema", "Organization policy"], 0),
            ("Who owns application readiness probes?", ["The workload team", "Google billing", "Cloud DNS", "The container registry"], 0),
            ("Why set resource requests?", ["Scheduling and capacity decisions need them", "They create IAM roles", "They expose a public IP", "They disable quotas"], 0),
            ("What avoids sharing node identity with all pods?", ["Workload Identity Federation for GKE", "A public service", "Basic roles", "Static node keys"], 0),
            ("When is Standard stronger than Autopilot?", ["When deep node control is required", "When no Kubernetes features are needed", "For a single static file", "To remove all operations"], 0),
        ],
    },
    "gcp/08-ops-and-logging": {
        "goals": [
            "Use Cloud Logging, Cloud Monitoring, Error Reporting, and Trace for distinct questions",
            "Write Logs Explorer filters and log-based metrics",
            "Build an actionable alert and control telemetry routing and retention",
        ],
        "why": "Google Cloud Observability turns distributed service behavior into searchable evidence, but useful signals require structured fields, correlation, retention, and response design.",
        "ideas": [
            "**Structured logs preserve severity and fields** so filters do not depend on brittle text parsing.",
            "**Metrics describe trends; logs explain events; traces connect latency across calls** — incidents often need all three.",
            "**Log sinks route matching entries** to buckets, BigQuery, Pub/Sub, or other supported destinations.",
            "**SLO-based alerts favor user impact** over noisy infrastructure thresholds.",
        ],
        "example": """### Lab: query failures and inspect metrics

```bash
gcloud logging read \
  'resource.type="cloud_run_revision"
   resource.labels.service_name="hello-api"
   severity>=ERROR' \
  --freshness=1h --limit=20 \
  --format='table(timestamp,severity,jsonPayload.message)'

gcloud monitoring metrics list \
  --filter='metric.type:run.googleapis.com/request_count' --limit=5
```

In Logs Explorer, refine with `httpRequest.status>=500`, then create a counter metric grouped by service and response code before alerting on a sustained rate.""",
        "practice": [
            "Emit a structured log with severity, request ID, release, and safe error code.",
            "Create a logs filter for one service's 5xx responses in the last hour.",
            "Design an alert policy with threshold, duration, notification channel, and runbook.",
        ],
        "mistakes": [
            "Logging credentials, identity tokens, or full sensitive request bodies",
            "Alerting on one error instead of a sustained user-impact rate",
            "Exporting all logs without estimating destination storage and query cost",
        ],
        "stretch": "Define an availability SLO and burn-rate alerts for fast and slow budget consumption.",
        "quiz": [
            ("Why emit structured logs?", ["Fields can be reliably filtered and aggregated", "They disable IAM", "They create VPC routes", "They are always free"], 0),
            ("What connects latency across service calls?", ["Cloud Trace", "Cloud Billing", "Cloud DNS", "Organization Policy"], 0),
            ("What does a log sink do?", ["Routes matching logs to a destination", "Restarts VMs", "Grants Owner", "Creates subnets"], 0),
            ("Which alert best reflects user impact?", ["Sustained error-rate or SLO burn", "One debug line", "Any CPU sample", "Project-name length"], 0),
            ("What should never appear in logs?", ["Access tokens", "Safe request IDs", "Release versions", "HTTP status codes"], 0),
        ],
    },
    "gcp/09-billing-and-cost": {
        "goals": [
            "Relate billing accounts, projects, budgets, quotas, labels, and detailed exports",
            "Analyze cost before choosing rightsizing, scheduling, commitment, or storage actions",
            "Explain why budgets and quotas are guardrails rather than universal hard stops",
        ],
        "why": "GCP costs follow architecture and usage. Attribution, exports, and accountable alerts make optimization evidence-based rather than a sequence of risky guesses.",
        "ideas": [
            "**A billing account pays for linked projects** while IAM on billing and projects remains separate.",
            "**Budgets notify on actual or forecasted spend** but generally do not cap usage automatically.",
            "**Billing export to BigQuery enables SKU-level analysis** and joins cost with labels and business metadata.",
            "**Commit only after measuring stable demand** — committed use discounts exchange flexibility for a term commitment.",
        ],
        "example": """### Lab: inspect project billing and labelled resources

```bash
PROJECT_ID=$(gcloud config get-value project)
gcloud billing projects describe "$PROJECT_ID"
gcloud billing budgets list --billing-account=<billing-account-id>
gcloud compute instances list \
  --format='table(name,zone,machineType.basename(),status,labels)'
gcloud storage buckets list \
  --format='table(name,location,storageClass)'
```

Enable detailed billing export to BigQuery, then query cost by `project.id`, `service.description`, `sku.description`, and credits before recommending changes.""",
        "practice": [
            "Define budget thresholds for actual and forecasted spend with named recipients.",
            "Identify idle VMs, unattached disks, stale snapshots, and oversized log retention.",
            "Write a BigQuery billing-export query plan grouped by project, service, SKU, and label.",
        ],
        "mistakes": [
            "Assuming a budget automatically shuts down resources",
            "Buying commitments from a short or highly variable usage sample",
            "Deleting resources based only on low CPU without checking memory, latency, or business schedule",
        ],
        "stretch": "Design a Pub/Sub budget-notification workflow with approvals and resource-specific safe actions.",
        "quiz": [
            ("What does a billing account do?", ["Pays for linked projects", "Contains VPC subnets", "Authenticates every workload", "Stores container images"], 0),
            ("Do budgets normally hard-stop GCP spend?", ["Yes", "No; they send alerts unless automation acts", "Only on Cloud Run", "Only with labels"], 1),
            ("Why export billing data to BigQuery?", ["For detailed cost analysis", "To create VM images", "To replace IAM", "To configure DNS"], 0),
            ("When are commitments most appropriate?", ["After measuring predictable baseline usage", "Before any workload exists", "For unknown spikes only", "To avoid all monitoring"], 0),
            ("Which metadata improves cost attribution?", ["Consistent labels", "Public IPs", "Service-account keys", "Firewall priorities"], 0),
        ],
    },
    "gcp/10-capstone-gcp-service": {
        "goals": [
            "Ship a Cloud Run service using Artifact Registry, a dedicated identity, private data, and observability",
            "Demonstrate authenticated invocation, revision rollout, rollback, and cost controls",
            "Produce reproducible deployment and cleanup evidence",
        ],
        "why": "The capstone validates that GCP projects, IAM, networking, managed compute, storage, operations, and billing controls form one secure service.",
        "ideas": [
            "**Use a dedicated project or clearly labelled lab scope** to isolate APIs, IAM, quotas, and billing.",
            "**Build once and deploy an immutable image digest** so the tested artifact is the released artifact.",
            "**The runtime service account receives only required roles** and humans deploy through auditable identities.",
            "**Release evidence includes telemetry and rollback** rather than only an HTTP 200 response.",
        ],
        "example": """### Capstone: build and release a small API

```bash
REGION=europe-west1
PROJECT_ID=$(gcloud config get-value project)
gcloud artifacts repositories create capstone \
  --repository-format=docker --location="$REGION"
gcloud builds submit \
  --tag "$REGION-docker.pkg.dev/$PROJECT_ID/capstone/api:v1"
gcloud run deploy capstone-api \
  --image "$REGION-docker.pkg.dev/$PROJECT_ID/capstone/api:v1" \
  --region="$REGION" \
  --service-account="app-runtime@$PROJECT_ID.iam.gserviceaccount.com" \
  --no-allow-unauthenticated --max-instances=5
gcloud run services describe capstone-api --region="$REGION" \
  --format='yaml(status.url,status.traffic)'
```

Attach private Cloud Storage access, emit structured logs, deploy `v2` as a no-traffic revision, test it by tag, then shift traffic and demonstrate rollback.""",
        "practice": [
            "Present a diagram of project, caller, Cloud Run revision, service account, storage, and telemetry.",
            "Prove denied anonymous invocation and successful identity-token invocation.",
            "Capture release, error query, traffic rollback, billing alert, and cleanup output.",
        ],
        "mistakes": [
            "Making the service or bucket public to bypass IAM troubleshooting",
            "Deploying mutable `latest` without recording the image digest",
            "Leaving Artifact Registry images, revisions, buckets, or billable resources unreviewed",
        ],
        "stretch": "Add a global external Application Load Balancer with managed TLS, a custom domain, and Cloud Armor policy.",
        "quiz": [
            ("Why use a dedicated runtime service account?", ["To scope workload permissions", "To bypass audit logs", "To make invocation public", "To replace the project"], 0),
            ("What makes the deployed artifact reproducible?", ["An immutable image digest", "The `latest` tag alone", "A local container only", "A screenshot"], 0),
            ("How do you prove private invocation?", ["Anonymous is denied and an identity token succeeds", "The URL exists", "The bucket is public", "The service has no logs"], 0),
            ("What enables quick Cloud Run rollback?", ["Revision traffic management", "Project deletion", "DNS removal", "Service-account keys"], 0),
            ("What belongs in final evidence?", ["Architecture, IAM, telemetry, rollout, cost, and cleanup", "Only homepage HTML", "An Owner binding", "A password file"], 0),
        ],
    },
    "kubernetes/01-k8s-mental-model": {
        "goals": [
            "Explain desired-state reconciliation across the API server, controllers, scheduler, nodes, and kubelet",
            "Use declarative manifests and labels to inspect cluster objects",
            "Separate cluster, namespace, and workload responsibilities",
        ],
        "why": "Kubernetes is a control system, not a collection of imperative container commands. Its reconciliation model explains both normal behavior and most troubleshooting paths.",
        "ideas": [
            "**The API server stores declared intent** and validates requests; etcd persists cluster state.",
            "**Controllers reconcile actual state toward desired state** repeatedly rather than running a one-time script.",
            "**The scheduler chooses a node; kubelet realizes pod state on that node** through the container runtime.",
            "**Labels identify sets; namespaces scope names and policy** but are not complete security boundaries by themselves.",
        ],
        "example": """### Lab: observe reconciliation

```bash
kubectl cluster-info
kubectl create namespace course
kubectl create deployment web --image=nginx:1.27 \
  --replicas=2 --namespace=course
kubectl get deployment,replicaset,pods -n course \
  --show-labels --watch
```

In another terminal, delete one pod:

```bash
kubectl delete pod -n course \
  $(kubectl get pod -n course -o jsonpath='{.items[0].metadata.name}')
```

The ReplicaSet controller creates a replacement because the Deployment still declares two replicas.""",
        "practice": [
            "Trace a Deployment request from `kubectl` to a running container.",
            "Delete a managed pod and record the controller events that follow.",
            "Label two objects and select them with `kubectl get ... -l key=value`.",
        ],
        "mistakes": [
            "Editing containers inside pods as if they were durable servers",
            "Assuming a namespace alone provides strong tenant isolation",
            "Treating `kubectl` output as the source of truth instead of the API objects",
        ],
        "stretch": "Inspect owner references from Pod to ReplicaSet to Deployment and explain garbage collection.",
        "quiz": [
            ("What repeatedly moves actual state toward desired state?", ["Controllers", "Container image tags", "DNS clients", "Ingress rules"], 0),
            ("What component selects a node for an unscheduled pod?", ["Scheduler", "kubelet", "CoreDNS", "Service"], 0),
            ("What does kubelet primarily manage?", ["Pods assigned to its node", "Cloud billing", "Git branches", "All cluster IAM"], 0),
            ("What identifies a flexible set of objects?", ["Labels and selectors", "Namespace names only", "Container ports", "UID ranges"], 0),
            ("Is a namespace a complete hard security boundary?", ["Yes", "No; add RBAC, network, and policy controls", "Only for DNS", "Only for StatefulSets"], 1),
        ],
    },
    "kubernetes/02-pods-and-workloads": {
        "goals": [
            "Describe pods as co-scheduled containers sharing network and selected volumes",
            "Choose Deployment, StatefulSet, DaemonSet, Job, or CronJob by workload behavior",
            "Configure resource requests, limits, probes, and restart behavior",
        ],
        "why": "A pod is Kubernetes' scheduling unit, but controllers make applications resilient. Correct workload type and runtime contract determine whether recovery and scaling behave safely.",
        "ideas": [
            "**Containers in one pod share an IP and localhost** and should have a tight lifecycle reason to be co-located.",
            "**Deployments suit replaceable replicas; StatefulSets add stable identity; DaemonSets place per-node agents**.",
            "**Jobs finish; CronJobs schedule Jobs** — they are better than keeping a server alive for batch work.",
            "**Requests guide scheduling, limits constrain use, and probes communicate health stages**.",
        ],
        "example": """### Lab: create a resource-aware Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata: {name: api, namespace: course}
spec:
  replicas: 2
  selector: {matchLabels: {app: api}}
  template:
    metadata: {labels: {app: api}}
    spec:
      containers:
        - name: api
          image: nginx:1.27
          resources:
            requests: {cpu: 100m, memory: 128Mi}
            limits: {cpu: 500m, memory: 256Mi}
          readinessProbe:
            httpGet: {path: /, port: 80}
            initialDelaySeconds: 2
```

```bash
kubectl apply -f deployment.yaml
kubectl describe pod -n course -l app=api
```""",
        "practice": [
            "Match five sample workloads to Deployment, StatefulSet, DaemonSet, Job, or CronJob.",
            "Add startup, readiness, and liveness probes with different purposes.",
            "Cause an OOM limit failure in a disposable lab and inspect status and events.",
        ],
        "mistakes": [
            "Running unrelated processes in one pod",
            "Omitting requests and making scheduling and capacity unpredictable",
            "Using a liveness probe that restarts a healthy but temporarily unready application",
        ],
        "stretch": "Add topology spread constraints so replicas distribute across zones without making scheduling impossible.",
        "quiz": [
            ("What do containers in one pod share?", ["A network namespace and selected volumes", "A container image", "Every process ID always", "A node forever"], 0),
            ("Which controller fits one log agent per node?", ["DaemonSet", "Deployment", "Job", "Ingress"], 0),
            ("What does a readiness probe control?", ["Whether a pod receives Service traffic", "Whether the image builds", "Whether the cluster bills", "Whether a PVC exists"], 0),
            ("What do resource requests influence?", ["Scheduling and reserved capacity", "Image tags", "Service DNS", "RBAC verbs"], 0),
            ("Which workload should run to completion?", ["Job", "Deployment", "DaemonSet", "Service"], 0),
        ],
    },
    "kubernetes/03-services-and-ingress": {
        "goals": [
            "Use Services to provide stable discovery over changing pod endpoints",
            "Choose ClusterIP, NodePort, LoadBalancer, or headless service behavior",
            "Route HTTP with Ingress while distinguishing controller, resource, DNS, and TLS responsibilities",
        ],
        "why": "Pods are replaceable and their IPs change. Services and ingress create stable traffic paths, but only when selectors, ports, controllers, and application readiness agree.",
        "ideas": [
            "**A Service selector produces EndpointSlices** containing ready matching pod addresses.",
            "**ClusterIP is the default internal virtual IP**; LoadBalancer asks an integration to provision external or internal load balancing.",
            "**Ingress is an HTTP routing API, not the data plane** — an installed ingress controller implements it.",
            "**`port`, `targetPort`, and container port describe different hops** and mismatches cause silent-looking failures.",
        ],
        "example": """### Lab: expose and diagnose an internal Service

```yaml
apiVersion: v1
kind: Service
metadata: {name: api, namespace: course}
spec:
  selector: {app: api}
  ports:
    - name: http
      port: 80
      targetPort: 8080
  type: ClusterIP
```

```bash
kubectl apply -f service.yaml
kubectl get service,endpointslice -n course
kubectl run curl -n course --rm -it --restart=Never \
  --image=curlimages/curl -- http://api.course.svc.cluster.local/health
```

If EndpointSlices are empty, compare the Service selector with pod labels and readiness.""",
        "practice": [
            "Create a ClusterIP Service and resolve its DNS name from another pod.",
            "Break and repair a selector while watching EndpointSlices.",
            "Write an Ingress rule for `/api` with a TLS secret and named backend port.",
        ],
        "mistakes": [
            "Creating an Ingress resource without an ingress controller",
            "Confusing Service `port` with `targetPort`",
            "Debugging DNS first when the Service has no ready endpoints",
        ],
        "stretch": "Compare Ingress with Gateway API roles and resources for a multi-team platform.",
        "quiz": [
            ("What gives clients a stable address for changing pods?", ["Service", "ReplicaSet only", "ConfigMap", "Namespace"], 0),
            ("What lists Service backend addresses?", ["EndpointSlices", "Secrets", "ResourceQuotas", "StorageClasses"], 0),
            ("What implements an Ingress resource?", ["An ingress controller", "The YAML file itself", "kubelet alone", "etcd clients"], 0),
            ("What does `targetPort` name?", ["The backend pod port", "The public DNS zone", "The node count", "The TLS issuer"], 0),
            ("Why might a matching pod be absent from ready endpoints?", ["Its readiness probe fails", "Its image has a tag", "It has a namespace", "It uses TCP"], 0),
        ],
    },
    "kubernetes/04-configmaps-secrets": {
        "goals": [
            "Inject non-sensitive and sensitive configuration into pods",
            "Explain ConfigMap and Secret update behavior for volumes and environment variables",
            "Protect secrets with encryption, RBAC, external stores, and safe delivery practices",
        ],
        "why": "Separating configuration from images enables repeatable promotion. Kubernetes Secret objects improve handling conventions, but base64 encoding alone does not make secret data secure.",
        "ideas": [
            "**ConfigMaps hold non-secret configuration; Secrets mark sensitive values** for stricter access and tooling.",
            "**Environment variable values are captured at process start**; projected volumes can update eventually, but applications must reload them.",
            "**Base64 is encoding, not encryption** — protect etcd, transport, RBAC, backups, and operator access.",
            "**External secret managers reduce secret sprawl** when integrated with workload identity and rotation.",
        ],
        "example": """### Lab: mount configuration and reference a Secret

```bash
kubectl create configmap api-config -n course \
  --from-literal=LOG_LEVEL=info
kubectl create secret generic api-secret -n course \
  --from-literal=DATABASE_PASSWORD='replace-in-a-real-secret-manager'
kubectl set env deployment/api -n course \
  --from=configmap/api-config
kubectl set env deployment/api -n course \
  --from=secret/api-secret
kubectl rollout status deployment/api -n course
```

Avoid putting literal secrets in shell history for real systems; use a secrets operator, encrypted Git workflow, or secure stdin/file process.""",
        "practice": [
            "Mount a ConfigMap as files and observe update behavior.",
            "Rotate a disposable Secret and deliberately restart the consuming Deployment.",
            "Use `kubectl auth can-i get secrets --as=<identity> -n course` to review access.",
        ],
        "mistakes": [
            "Committing plaintext Secret manifests or literal creation commands to shared history",
            "Assuming base64-encoded Secret data is encrypted",
            "Expecting an environment variable to change inside an already running process",
        ],
        "stretch": "Integrate an external secret manager with workload identity and demonstrate rotation without storing secret material in Git.",
        "quiz": [
            ("Is base64 encryption?", ["Yes", "No; it is reversible encoding", "Only in etcd", "Only for TLS"], 1),
            ("What should a ConfigMap contain?", ["Non-sensitive configuration", "Private keys", "Passwords", "Long-lived tokens"], 0),
            ("When does a pod normally read a Secret environment variable?", ["At container start", "On every API request", "Only at image build", "After DNS lookup"], 0),
            ("What limits who can read Secret objects?", ["RBAC", "A Service selector", "A readiness probe", "A StorageClass"], 0),
            ("What improves secret rotation and central control?", ["An external secret manager with workload identity", "A public ConfigMap", "A hard-coded image layer", "A NodePort"], 0),
        ],
    },
    "kubernetes/05-storage-and-pv": {
        "goals": [
            "Explain PersistentVolume, PersistentVolumeClaim, StorageClass, and CSI driver roles",
            "Select access mode, volume mode, capacity, reclaim policy, and binding behavior",
            "Protect stateful data during workload and namespace lifecycle changes",
        ],
        "why": "Containers are disposable, but application data may not be. Kubernetes storage separates workload claims from infrastructure provisioning while preserving provider-specific constraints.",
        "ideas": [
            "**A PVC requests storage; a PV represents supplied storage** and binding connects compatible objects.",
            "**StorageClasses define dynamic provisioning and policy** such as type, expansion, reclaim behavior, and binding mode.",
            "**Access modes describe attachment semantics** but actual multi-writer support depends on the storage system.",
            "**StatefulSet volumeClaimTemplates give each replica stable storage identity**; they do not create database replication.",
        ],
        "example": """### Lab: request and mount persistent storage

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata: {name: app-data, namespace: course}
spec:
  accessModes: [ReadWriteOnce]
  resources:
    requests: {storage: 1Gi}
---
apiVersion: v1
kind: Pod
metadata: {name: writer, namespace: course}
spec:
  containers:
    - name: writer
      image: busybox:1.36
      command: ["sh", "-c", "date >> /data/history; sleep 3600"]
      volumeMounts: [{name: data, mountPath: /data}]
  volumes:
    - name: data
      persistentVolumeClaim: {claimName: app-data}
```

```bash
kubectl apply -f storage-lab.yaml
kubectl get pvc,pv -n course
kubectl describe pvc app-data -n course
```""",
        "practice": [
            "Inspect the default StorageClass and its provisioner, reclaim policy, and binding mode.",
            "Delete and recreate the pod, then verify persisted data.",
            "Document snapshot, restore, and expansion procedures for the chosen CSI driver.",
        ],
        "mistakes": [
            "Assuming ReadWriteOnce means only one pod under every topology",
            "Deleting a PVC without checking PV reclaim policy and backups",
            "Treating a single persistent disk as a highly available database",
        ],
        "stretch": "Deploy a StatefulSet with per-replica claims and test a CSI snapshot restore into a new claim.",
        "quiz": [
            ("What does a PVC represent?", ["A workload's storage request", "A running disk driver", "A pod IP", "A network policy"], 0),
            ("What commonly provisions PVs dynamically?", ["StorageClass and CSI driver", "Ingress controller", "ServiceAccount", "ConfigMap"], 0),
            ("Does a StatefulSet automatically replicate database data?", ["Yes", "No", "Only with ClusterIP", "Only with a Secret"], 1),
            ("What can cause data deletion after a claim is removed?", ["A Delete reclaim policy", "A readiness probe", "A label selector", "A headless Service"], 0),
            ("What should be tested in addition to snapshots?", ["Restore", "Only creation", "Only compression", "Node labels"], 0),
        ],
    },
    "kubernetes/06-deployments-rollouts": {
        "goals": [
            "Perform and observe a rolling Deployment update",
            "Tune surge, unavailable, readiness, and progress-deadline settings",
            "Pause, resume, and roll back using revision evidence",
        ],
        "why": "A Deployment makes replacement automated, but safe release behavior depends on capacity, readiness, application compatibility, and an observable rollback decision.",
        "ideas": [
            "**A Deployment manages ReplicaSets** and gradually shifts desired replicas during a rolling update.",
            "**`maxSurge` and `maxUnavailable` trade temporary capacity for availability**.",
            "**Readiness gates traffic, while `minReadySeconds` and progress deadlines detect unhealthy rollout behavior**.",
            "**Rollback restores a pod template revision** but cannot automatically reverse incompatible database or external changes.",
        ],
        "example": """### Lab: update, observe, and undo

```bash
kubectl set image deployment/api -n course \
  api=ghcr.io/example/api:2.0.0 --record
kubectl rollout status deployment/api -n course --timeout=2m
kubectl rollout history deployment/api -n course
kubectl get rs,pods -n course -l app=api

# If health or error signals regress:
kubectl rollout undo deployment/api -n course
kubectl rollout status deployment/api -n course
```

Use immutable image digests in production and record the change reason through your delivery system.""",
        "practice": [
            "Set `maxSurge: 1` and `maxUnavailable: 0`, then watch pod replacement.",
            "Deploy an intentionally failing readiness probe and inspect rollout status and events.",
            "Rollback and verify both Kubernetes state and an application-level request.",
        ],
        "mistakes": [
            "Using the mutable `latest` tag and losing artifact identity",
            "Calling a rollout successful before readiness and service metrics stabilize",
            "Assuming pod rollback reverses a destructive database migration",
        ],
        "stretch": "Implement a canary with a second Deployment and weighted traffic through a capable gateway or service mesh.",
        "quiz": [
            ("What object stores a Deployment revision's pod template?", ["ReplicaSet", "Service", "ConfigMap", "Node"], 0),
            ("What does `maxUnavailable: 0` require during rollout?", ["No desired replica may be unavailable", "No surge is allowed", "No image pull occurs", "No probes run"], 0),
            ("What command restores a prior Deployment revision?", ["kubectl rollout undo", "kubectl delete node", "kubectl expose", "kubectl auth reconcile"], 0),
            ("Does rollback reverse a database migration?", ["Always", "No; it needs a compatible data strategy", "Only for StatefulSets", "Only if DNS is enabled"], 1),
            ("Why use an image digest?", ["It identifies immutable content", "It increases replicas", "It grants RBAC", "It creates TLS"], 0),
        ],
    },
    "kubernetes/07-autoscaling-basics": {
        "goals": [
            "Explain Horizontal Pod Autoscaler, Vertical Pod Autoscaler, and node autoscaler responsibilities",
            "Configure an HPA using meaningful requests and metrics",
            "Recognize stabilization, startup, capacity, and downstream bottlenecks",
        ],
        "why": "Autoscaling turns demand signals into capacity changes, but missing requests, lagging metrics, slow startup, and constrained dependencies can make scaling unstable or ineffective.",
        "ideas": [
            "**HPA changes replica count from observed metrics**; CPU utilization is measured relative to container requests.",
            "**VPA recommends or changes pod resources** and can conflict with HPA when both act on the same CPU or memory signal.",
            "**Node autoscaling supplies schedulable infrastructure** when pods remain pending for supported capacity reasons.",
            "**Scaling is a feedback loop** — tolerance, stabilization windows, startup delay, quotas, and maximums prevent runaway behavior.",
        ],
        "example": """### Lab: create and inspect an HPA

```bash
kubectl set resources deployment/api -n course \
  --requests=cpu=100m,memory=128Mi \
  --limits=cpu=500m,memory=256Mi
kubectl autoscale deployment api -n course \
  --cpu-percent=60 --min=2 --max=10
kubectl get hpa -n course --watch
kubectl describe hpa api -n course
```

This requires a functioning resource metrics pipeline such as Metrics Server. Generate controlled load and observe replicas, pending pods, latency, and dependency saturation together.""",
        "practice": [
            "Create an HPA and explain how a 100m request affects displayed CPU utilization.",
            "Load test until replicas increase, then observe scale-down stabilization.",
            "List reasons pods can remain Pending even when an HPA asks for more replicas.",
        ],
        "mistakes": [
            "Enabling CPU HPA without CPU requests",
            "Setting a high maximum that overwhelms a fixed-size database",
            "Expecting HPA to add cluster nodes or fix a slow-starting application by itself",
        ],
        "stretch": "Scale on a custom queue-depth metric and derive a target from per-replica processing capacity.",
        "quiz": [
            ("What does HPA change?", ["Workload replica count", "Node kernel", "Container image", "PVC reclaim policy"], 0),
            ("CPU utilization for HPA is relative to what?", ["CPU requests", "CPU limits only", "Node count", "Image size"], 0),
            ("What can add nodes for unschedulable pods?", ["A node autoscaler", "HPA alone", "A Service", "A ConfigMap"], 0),
            ("Why set a maximum replica count?", ["To bound cost and downstream load", "To disable metrics", "To encrypt Secrets", "To assign nodes manually"], 0),
            ("What reduces rapid scale-down oscillation?", ["A stabilization window", "Deleting requests", "Using `latest`", "A NodePort"], 0),
        ],
    },
    "kubernetes/08-observability-on-k8s": {
        "goals": [
            "Collect and correlate Kubernetes events, logs, metrics, and traces",
            "Use `kubectl` diagnostics without relying on interactive changes inside containers",
            "Define workload golden signals and alert from user impact",
        ],
        "why": "Kubernetes adds scheduling and control-plane layers to application failures. Effective observability connects platform state to request behavior instead of collecting disconnected dashboards.",
        "ideas": [
            "**Events explain recent control-plane decisions** but have limited retention and are not a durable audit stream.",
            "**Container logs should flow to a node-level collector** because local pod files disappear.",
            "**Metrics expose trends and saturation; traces preserve request causality** across services.",
            "**Labels enable correlation but unbounded values cause metric-cardinality and cost problems**.",
        ],
        "example": """### Lab: triage a failing workload

```bash
kubectl get pods -n course -o wide
kubectl describe pod -n course <pod-name>
kubectl logs -n course <pod-name> --all-containers --since=10m
kubectl logs -n course <pod-name> --previous
kubectl get events -n course \
  --sort-by=.metadata.creationTimestamp
kubectl top pods -n course
```

Start with the user symptom, then correlate pod restarts, readiness, resource saturation, recent revisions, application errors, and dependency traces.""",
        "practice": [
            "Diagnose CrashLoopBackOff, ImagePullBackOff, and Pending scenarios from evidence.",
            "Define traffic, errors, latency, and saturation signals for one Service.",
            "Propagate a request ID or trace context through two sample services.",
        ],
        "mistakes": [
            "Using only `kubectl logs` and ignoring events, prior containers, and metrics",
            "Adding pod UID, request ID, or customer ID as an unbounded metric label",
            "Alerting on platform noise with no user impact or response action",
        ],
        "stretch": "Instrument an application with OpenTelemetry and correlate one trace with Kubernetes metadata and logs.",
        "quiz": [
            ("Which command shows logs from the previous crashed container?", ["kubectl logs --previous", "kubectl get service", "kubectl rollout pause", "kubectl auth can-i"], 0),
            ("What are Kubernetes events best for?", ["Recent scheduling and controller decisions", "Long-term application analytics", "Secret storage", "Image signing"], 0),
            ("Why avoid high-cardinality metric labels?", ["They increase series count and cost", "They disable pods", "They remove traces", "They create PVs"], 0),
            ("Which signal follows one request across services?", ["Trace", "Node label", "ResourceQuota", "StorageClass"], 0),
            ("Where should container logs be retained?", ["An external durable logging system", "Only inside the pod filesystem", "A ConfigMap", "An image layer"], 0),
        ],
    },
    "kubernetes/09-security-basics": {
        "goals": [
            "Apply least-privilege RBAC, service accounts, and namespace policy",
            "Use Pod Security Standards, security contexts, and NetworkPolicies",
            "Reduce supply-chain risk with immutable, scanned, and verifiable images",
        ],
        "why": "A Kubernetes cluster combines powerful APIs, shared nodes, network reachability, and software supply chains. Security must constrain identities, workloads, traffic, and artifacts together.",
        "ideas": [
            "**RBAC controls API verbs on resources** — test effective access and avoid wildcard cluster roles.",
            "**Pod Security Standards restrict risky workload settings** such as privilege, host namespaces, root, and added capabilities.",
            "**NetworkPolicy changes pod traffic from broadly reachable toward explicit allowance** when the CNI enforces it.",
            "**Image security starts before admission** — pin digests, scan dependencies, sign artifacts, and enforce trusted sources.",
        ],
        "example": """### Lab: create a read-only workload identity

```bash
kubectl create serviceaccount viewer -n course
kubectl create role pod-reader -n course \
  --verb=get,list,watch --resource=pods
kubectl create rolebinding viewer-reads-pods -n course \
  --role=pod-reader --serviceaccount=course:viewer
kubectl auth can-i list pods \
  --as=system:serviceaccount:course:viewer -n course
kubectl auth can-i delete pods \
  --as=system:serviceaccount:course:viewer -n course
kubectl label namespace course \
  pod-security.kubernetes.io/enforce=restricted --overwrite
```""",
        "practice": [
            "Create a Role that can read ConfigMaps but cannot read Secrets.",
            "Harden a pod with non-root user, read-only root filesystem, dropped capabilities, and seccomp.",
            "Apply default-deny ingress and egress, then add only required DNS and service flows.",
        ],
        "mistakes": [
            "Binding workloads or developers to `cluster-admin`",
            "Assuming a NetworkPolicy works without CNI enforcement",
            "Running unpinned images as root with privilege or host mounts",
        ],
        "stretch": "Enforce signed images from an approved registry with an admission policy and document the break-glass process.",
        "quiz": [
            ("What does Kubernetes RBAC govern?", ["API actions on resources", "Container network packets", "Image vulnerabilities", "Disk encryption"], 0),
            ("Which namespace label can enforce a Pod Security profile?", ["pod-security.kubernetes.io/enforce", "app.kubernetes.io/name", "service.beta/name", "storage.kubernetes.io/class"], 0),
            ("What does a default-deny NetworkPolicy require next?", ["Explicit allow policies for necessary flows", "Cluster-admin", "Public NodePorts", "Deleting DNS"], 0),
            ("Why pin an image digest?", ["To identify immutable image content", "To grant registry access", "To add replicas", "To create a Secret"], 0),
            ("Should a pod normally use the default service account token?", ["Only when API access is required and scoped", "Always", "It grants no access ever", "Only for public ingress"], 0),
        ],
    },
    "kubernetes/10-capstone-k8s-app": {
        "goals": [
            "Deploy a production-shaped application with declarative workload, service, config, security, and availability controls",
            "Demonstrate rollout, autoscaling or capacity behavior, diagnostics, and rollback",
            "Package manifests and operational evidence for repeatable review",
        ],
        "why": "The capstone proves that individual Kubernetes objects form a resilient and diagnosable application contract rather than an assortment of YAML files.",
        "ideas": [
            "**Start from an application contract** — image, ports, configuration, health, resources, identity, storage, and traffic.",
            "**Safe delivery needs readiness and immutable artifacts** before replicas can protect availability.",
            "**Secure defaults are visible in manifests** — non-root, restricted capabilities, scoped identity, and allowed network paths.",
            "**Operations are part of done** — dashboards, failure triage, rollback, backup if stateful, and cleanup.",
        ],
        "example": """### Capstone: apply and verify an application bundle

```bash
kubectl create namespace capstone
kubectl label namespace capstone \
  pod-security.kubernetes.io/enforce=restricted
kubectl apply -n capstone -f k8s/
kubectl rollout status deployment/api -n capstone --timeout=3m
kubectl get deploy,pod,service,endpointslice,hpa,pvc -n capstone
kubectl wait -n capstone --for=condition=Ready pod \
  -l app=api --timeout=2m
kubectl run smoke -n capstone --rm -i --restart=Never \
  --image=curlimages/curl -- http://api/health
```

Deploy a bad revision in the lab, identify it through readiness and logs, roll it back, and preserve the command output as evidence.""",
        "practice": [
            "Submit manifests for Namespace, Deployment, Service, configuration, identity, policy, and optional storage/ingress.",
            "Demonstrate healthy traffic, failed rollout diagnosis, and successful rollback.",
            "Run server-side dry-run, manifest validation, access checks, and namespace cleanup.",
        ],
        "mistakes": [
            "Submitting generated YAML that cannot be applied in dependency order",
            "Leaving probes, requests, limits, security context, and image version unspecified",
            "Calling the capstone complete without a controlled failure and recovery demonstration",
        ],
        "stretch": "Package the application as a Helm chart or Kustomize bases/overlays and test it in a second namespace.",
        "quiz": [
            ("What should gate Service traffic during a rollout?", ["Readiness", "Image size", "Namespace age", "PVC name"], 0),
            ("What proves manifests are operable?", ["Apply, smoke test, failure diagnosis, and rollback evidence", "YAML syntax alone", "A public NodePort", "Cluster-admin access"], 0),
            ("Why include requests and limits?", ["For scheduling, capacity, and containment", "To create DNS", "To configure RBAC", "To encrypt etcd"], 0),
            ("What should identify the deployed artifact?", ["An immutable image tag or digest", "`latest` only", "A pod name", "A node IP"], 0),
            ("What closes a temporary capstone environment?", ["Verified cleanup", "Leaving the namespace", "Disabling probes", "Deleting logs first"], 0),
        ],
    },
    "terraform/01-iac-why-terraform": {
        "goals": [
            "Explain infrastructure as code as a reviewed desired-state workflow",
            "Describe Terraform configuration, state, planning, and provider APIs",
            "Import or recreate infrastructure without treating generated code as unquestioned truth",
        ],
        "why": "Infrastructure as code makes changes reviewable, repeatable, and auditable. Terraform adds dependency-aware planning, but safe use still depends on state discipline and human review.",
        "ideas": [
            "**Configuration declares desired infrastructure** while providers translate resource operations to platform APIs.",
            "**Terraform compares configuration, prior state, and refreshed remote objects** to propose a plan.",
            "**Idempotent convergence is the goal** — repeated applies should settle with no changes when inputs and remote systems are stable.",
            "**IaC is a team process** — version control, review, testing, promotion, and recovery matter more than syntax alone.",
        ],
        "example": """### Lab: inspect the Terraform workflow locally

```hcl
terraform {
  required_version = ">= 1.8"
}

resource "terraform_data" "course" {
  input = {
    owner       = "student"
    environment = "lab"
  }
}
```

```bash
terraform fmt -check
terraform init
terraform validate
terraform plan -out=tfplan
terraform show tfplan
terraform apply tfplan
terraform plan -detailed-exitcode
```

A final exit code of `0` means no diff; `2` means a non-empty plan; `1` means an error.""",
        "practice": [
            "Explain each workflow step from configuration change through reviewed apply.",
            "Create a local `terraform_data` resource and reach a no-change second plan.",
            "Compare Terraform with an imperative provisioning script for rollback, drift, and review.",
        ],
        "mistakes": [
            "Treating an approved plan as optional before production apply",
            "Editing state by hand or committing it to Git",
            "Assuming declarative configuration makes every change nondestructive",
        ],
        "stretch": "Import a disposable existing resource into a resource block and verify a no-change plan.",
        "quiz": [
            ("What does Terraform configuration express?", ["Desired infrastructure state", "Only shell command order", "Cloud invoices", "Application logs"], 0),
            ("What inputs inform a typical plan?", ["Configuration, state, and remote refresh", "Only Git history", "Only billing", "Only environment names"], 0),
            ("What should a stable second plan show?", ["No changes", "Forced replacement", "State deletion", "Provider removal"], 0),
            ("Does declarative IaC guarantee every change is safe?", ["Yes", "No; plans can include destructive actions", "Only with local state", "Only without providers"], 1),
            ("Why keep IaC in version control?", ["Review, history, collaboration, and audit", "To store secrets", "To avoid validation", "To bypass policy"], 0),
        ],
    },
    "terraform/02-providers-and-resources": {
        "goals": [
            "Declare providers with explicit source and compatible version constraints",
            "Configure resources and data sources without hard-coded credentials",
            "Reason about references, dependency graph, aliases, and replacement behavior",
        ],
        "why": "Providers are executable plugins that control real infrastructure. Their versions, credentials, regions, schemas, and dependency relationships must be deliberate and reviewable.",
        "ideas": [
            "**`required_providers` records source and version compatibility** while the lock file selects checksummed versions.",
            "**Resources manage lifecycle; data sources read existing information** without owning it.",
            "**References create implicit dependencies**; `depends_on` is for hidden behavioral dependencies, not routine ordering.",
            "**Provider aliases support multiple regions or accounts** and must be passed explicitly into modules.",
        ],
        "example": """### Lab: declare and inspect a provider

```hcl
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "lab" {
  name     = "rg-tf-course"
  location = "UK South"
}
```

```bash
az login
terraform init
terraform providers
terraform validate
terraform plan
```

Use ambient CLI, workload identity, or CI federation; do not put client secrets in provider blocks.""",
        "practice": [
            "Pin a provider compatibility range and inspect `.terraform.lock.hcl`.",
            "Reference a resource attribute from another resource to create an implicit dependency.",
            "Create an aliased second-region provider and pass it to a small module.",
        ],
        "mistakes": [
            "Leaving provider origin or version unconstrained",
            "Hard-coding cloud credentials in `.tf` files",
            "Adding `depends_on` everywhere instead of using attribute references",
        ],
        "stretch": "Upgrade one provider with `terraform init -upgrade`, review schema-driven plan changes, and document the lock-file diff.",
        "quiz": [
            ("What does a resource block do?", ["Manages an object's lifecycle", "Only reads logs", "Stores provider binaries in state", "Creates Git branches"], 0),
            ("What does a data source normally do?", ["Reads existing information", "Owns deletion of the remote object", "Encrypts state", "Runs CI"], 0),
            ("Where is the selected provider version recorded?", [".terraform.lock.hcl", "terraform.tfstate only", ".gitignore", "README.md"], 0),
            ("What usually creates a dependency between resources?", ["An attribute reference", "Alphabetical order", "File order", "A comment"], 0),
            ("How should CI authenticate to cloud providers?", ["Short-lived federated identity", "A committed client secret", "A developer password", "Anonymous access"], 0),
        ],
    },
    "terraform/03-state-and-backends": {
        "goals": [
            "Explain why Terraform state maps resource addresses to remote objects",
            "Configure a remote backend with locking, encryption, access control, and recovery",
            "Use supported state commands for moves, imports, and removals",
        ],
        "why": "State is operationally sensitive and often contains secrets. A reliable backend prevents conflicting writes, enables team workflows, and makes recovery possible.",
        "ideas": [
            "**State is Terraform's ownership and identity record** — losing it does not delete infrastructure, but destroys Terraform's mapping.",
            "**A backend stores state and may coordinate locking**; backend capabilities differ by implementation.",
            "**State can expose sensitive values despite `sensitive = true`** — encrypt it and restrict read access.",
            "**Refactors need address migration** through `moved` blocks or `terraform state mv` to avoid accidental replacement.",
        ],
        "example": """### Lab: migrate state to a protected backend

```hcl
terraform {
  backend "s3" {
    bucket       = "company-terraform-state"
    key          = "training/app/terraform.tfstate"
    region       = "eu-west-2"
    encrypt      = true
    use_lockfile = true
  }
}
```

```bash
terraform init -migrate-state
terraform state list
terraform state show terraform_data.course
terraform state pull > /tmp/state-backup.json
```

Protect the bucket with versioning, least-privilege IAM, public-access blocking, and tested recovery. Never commit the backup.""",
        "practice": [
            "Document backend encryption, locking, versioning, access, and disaster recovery.",
            "Use a `moved` block to rename a resource address without recreation.",
            "Practice importing a disposable object and reconciling configuration to a no-change plan.",
        ],
        "mistakes": [
            "Sharing local state files through Git or chat",
            "Assuming `sensitive` prevents a value from existing in state",
            "Using `terraform state rm` as if it deletes the real cloud resource",
        ],
        "stretch": "Restore a prior backend object version in an isolated exercise and verify it against remote infrastructure.",
        "quiz": [
            ("What does state map?", ["Terraform addresses to remote objects", "Users to passwords", "Logs to traces", "Regions to invoices"], 0),
            ("Why use backend locking?", ["To prevent concurrent state writes", "To freeze cloud APIs", "To encrypt Git", "To stop all plans"], 0),
            ("Can sensitive values still exist in state?", ["Yes", "No", "Only in comments", "Only after destroy"], 0),
            ("What supports an address-only refactor?", ["A `moved` block", "Deleting state", "Changing provider credentials", "Skipping plan"], 0),
            ("What does `terraform state rm` do?", ["Stops Terraform managing the object without deleting it", "Deletes the remote object", "Locks the backend", "Formats configuration"], 0),
        ],
    },
    "terraform/04-variables-outputs": {
        "goals": [
            "Design typed, validated input variables with safe defaults",
            "Use locals to name transformations and outputs as module interfaces",
            "Pass secrets without exposing them in source, plans, logs, or state unnecessarily",
        ],
        "why": "Inputs and outputs are Terraform's public interface. Strong types and validation catch mistakes early, while disciplined secret handling limits accidental disclosure.",
        "ideas": [
            "**Type constraints define shape, not just documentation** — objects and collections make module contracts explicit.",
            "**Validation rejects invalid intent before provider calls** and preconditions can assert relationships using resource context.",
            "**Locals reduce repetition but do not create configurable inputs**.",
            "**`sensitive` redacts common CLI display; it does not encrypt values or remove them from state**.",
        ],
        "example": """### Lab: create a validated module interface

```hcl
variable "environment" {
  type        = string
  description = "Deployment environment"
  validation {
    condition     = contains(["dev", "stage", "prod"], var.environment)
    error_message = "environment must be dev, stage, or prod."
  }
}

variable "tags" {
  type    = map(string)
  default = {}
}

locals {
  common_tags = merge(var.tags, { environment = var.environment })
}

output "resource_id" {
  value       = terraform_data.course.id
  description = "Stable identifier for downstream automation"
}
```

```bash
terraform plan -var='environment=dev'
terraform output -json
```""",
        "practice": [
            "Add numeric range and allowed-value validations to two variables.",
            "Replace duplicated naming and tags with readable locals.",
            "Mark a disposable value sensitive and inspect plan, state implications, and JSON output handling.",
        ],
        "mistakes": [
            "Using `type = any` when a stable object contract is known",
            "Putting production secrets in committed `.tfvars` files",
            "Changing an output casually when downstream automation depends on its name and type",
        ],
        "stretch": "Build an object variable with optional attributes and cross-field validation for a service configuration.",
        "quiz": [
            ("What catches an invalid variable value early?", ["A validation block", "A backend lock", "A provider alias", "A state move"], 0),
            ("What are locals best for?", ["Named expressions and transformations", "Runtime user input", "Remote state locking", "Provider installation"], 0),
            ("Does `sensitive = true` encrypt state?", ["Yes", "No", "Only with local state", "Only for outputs"], 1),
            ("What makes a module input contract clearer?", ["Specific type constraints", "`any` everywhere", "Undocumented defaults", "Shell environment only"], 0),
            ("Who may consume outputs?", ["Parent modules and automation", "Only providers", "Only backends", "Only comments"], 0),
        ],
    },
    "terraform/05-modules": {
        "goals": [
            "Build a focused reusable module with a stable input and output contract",
            "Call and version local or registry modules safely",
            "Refactor resources into a module without unintended destruction",
        ],
        "why": "Modules encode an infrastructure capability and its safe defaults. Good modules reduce repetition without hiding critical decisions or creating a universal abstraction.",
        "ideas": [
            "**The root module composes; child modules encapsulate a coherent capability** such as a network or service.",
            "**A module interface should be small, typed, documented, and opinionated** while exposing necessary decisions.",
            "**Module sources should be versioned or pinned** so reviewed code cannot change silently.",
            "**Moving existing resources into modules requires state-address migration** with `moved` blocks.",
        ],
        "example": """### Lab: call a small local module

```hcl
module "labels" {
  source = "./modules/labels"

  application = "payments"
  environment = "dev"
  extra_tags  = { owner = "platform" }
}

output "labels" {
  value = module.labels.values
}
```

```bash
terraform fmt -recursive
terraform init
terraform validate
terraform plan
terraform providers
```

Inside `modules/labels`, include `variables.tf`, `main.tf`, `outputs.tf`, and a README with examples and compatibility requirements.""",
        "practice": [
            "Extract one cohesive resource group into a child module with typed inputs.",
            "Add a `moved` block from the old root address to the module address and confirm no replacement.",
            "Write a minimal example that exercises the module's default and optional behavior.",
        ],
        "mistakes": [
            "Building one giant module that exposes every provider argument",
            "Using an unpinned Git branch as a production module source",
            "Copying resources into a module without moving their state addresses",
        ],
        "stretch": "Publish the module contract with semantic versioning and a migration note for one intentional breaking change.",
        "quiz": [
            ("What should a child module represent?", ["A cohesive infrastructure capability", "Every company resource", "Only one variable file", "A backend lock"], 0),
            ("Why pin a remote module version?", ["To make consumed code reproducible", "To disable outputs", "To avoid state", "To create credentials"], 0),
            ("What prevents recreation during module refactoring?", ["State address migration with `moved`", "Renaming files only", "Skipping refresh", "Deleting the backend"], 0),
            ("What belongs in a module interface?", ["Typed inputs and useful outputs", "Provider credentials", "Local state", "Every possible knob"], 0),
            ("What command formats nested modules?", ["terraform fmt -recursive", "terraform state push", "terraform force-unlock", "terraform output -raw"], 0),
        ],
    },
    "terraform/06-workspaces-environments": {
        "goals": [
            "Explain what CLI workspaces isolate and what they do not",
            "Choose between workspaces, separate roots, and separate accounts or subscriptions",
            "Prevent accidental cross-environment credentials, state, and promotion",
        ],
        "why": "Environment isolation is a state, identity, network, and ownership decision. CLI workspaces provide multiple state instances for one configuration but are not a complete security boundary.",
        "ideas": [
            "**A CLI workspace selects a separate state instance in the same backend configuration**.",
            "**Workspaces share configuration and usually backend access** — they do not inherently isolate credentials or permissions.",
            "**Separate root configurations and cloud accounts provide stronger blast-radius boundaries** for materially different environments.",
            "**Promote reviewed code and immutable versions, not a mutated state file** between environments.",
        ],
        "example": """### Lab: observe workspace-specific state

```bash
terraform workspace new dev
terraform apply -auto-approve -var='environment=dev'
terraform workspace new stage
terraform plan -var='environment=stage'
terraform workspace list
terraform workspace show
```

In configuration, avoid silently deriving critical account selection from `terraform.workspace`. Make provider credentials and target account explicit in CI, and store production state under separately protected access where risk requires it.""",
        "practice": [
            "Create dev and stage workspaces for a local disposable resource and compare state lists.",
            "Threat-model who can read and write each environment's backend and cloud account.",
            "Choose an environment layout for sandbox, staging, and production and justify the isolation.",
        ],
        "mistakes": [
            "Assuming a workspace creates a cloud account or permission boundary",
            "Applying while the wrong workspace or provider credentials are active",
            "Using many conditional expressions until environments no longer share one coherent design",
        ],
        "stretch": "Design separate production and non-production roots that consume the same versioned modules through independent pipelines.",
        "quiz": [
            ("What does a CLI workspace primarily separate?", ["Terraform state instances", "Cloud accounts automatically", "Provider binaries", "Git repositories"], 0),
            ("Do workspaces inherently isolate credentials?", ["Yes", "No", "Only for AWS", "Only with outputs"], 1),
            ("What offers a stronger production blast-radius boundary?", ["A separate account and protected state/root", "A longer workspace name", "A local variable", "A comment"], 0),
            ("What should be promoted across environments?", ["Reviewed code and versioned artifacts", "A copied state file", "Developer credentials", "Manual console drift"], 0),
            ("What must be checked before apply?", ["Workspace, credentials, target, and plan", "Only file count", "Only output names", "Only provider logo"], 0),
        ],
    },
    "terraform/07-plan-apply-destroy": {
        "goals": [
            "Read plan actions, replacements, unknown values, and dependency effects",
            "Apply the exact reviewed saved plan",
            "Use lifecycle and destroy operations without masking unsafe design",
        ],
        "why": "Terraform's safety comes from understanding and approving a concrete change set. Automatic apply without plan integrity can turn a small configuration edit into a large outage.",
        "ideas": [
            "**Plan symbols communicate lifecycle** — create, update, destroy, and replace must be reviewed with context.",
            "**A saved plan binds the reviewed actions and variable values** but may contain sensitive information and can become stale.",
            "**Replacement can cascade through references** and create downtime when names, quotas, or lifecycle do not allow overlap.",
            "**Destroy is an intentional graph operation** — production protection needs policy, access control, backups, and lifecycle safeguards.",
        ],
        "example": """### Lab: save, inspect, and apply one plan

```bash
terraform fmt -check
terraform validate
terraform plan -out=tfplan -detailed-exitcode
# exit 0: no changes, 1: error, 2: changes
terraform show -no-color tfplan
terraform apply tfplan
terraform plan -detailed-exitcode
```

For a disposable lab only:

```bash
terraform plan -destroy -out=destroy.tfplan
terraform show destroy.tfplan
terraform apply destroy.tfplan
```

Treat plan files as sensitive artifacts and never reuse them after unrelated remote changes.""",
        "practice": [
            "Identify create, in-place update, replacement, and delete actions in sample plans.",
            "Trigger a safe replacement in a lab and note ordering and downtime implications.",
            "Add `prevent_destroy` to a critical sample resource and test the resulting plan failure.",
        ],
        "mistakes": [
            "Piping an unreviewed plan directly into automatic production apply",
            "Assuming `create_before_destroy` always works despite unique names or quotas",
            "Using `-target` as a normal deployment workflow and leaving an incomplete graph",
        ],
        "stretch": "Write a plan-review checklist that flags deletes, replacements, IAM, public exposure, cost, and unknown values.",
        "quiz": [
            ("Why apply a saved plan?", ["To apply the exact reviewed change set", "To skip provider authentication", "To remove state", "To avoid validation"], 0),
            ("What does a `-/+`-style action indicate?", ["Replacement", "Read-only refresh", "Output only", "Backend migration"], 0),
            ("Can `create_before_destroy` always avoid downtime?", ["Yes", "No; quotas and uniqueness may prevent overlap", "Only for outputs", "Only without state"], 1),
            ("What does `prevent_destroy` do?", ["Rejects plans that destroy the protected resource", "Backs up the resource", "Blocks all updates", "Encrypts state"], 0),
            ("Why avoid routine `-target` use?", ["It can produce an intentionally incomplete graph operation", "It formats too much", "It deletes providers", "It disables outputs"], 0),
        ],
    },
    "terraform/08-testing-and-policy": {
        "goals": [
            "Layer formatting, validation, linting, native tests, plans, and integration checks",
            "Write a Terraform test with assertions",
            "Use policy as code to block dangerous plan characteristics",
        ],
        "why": "Syntax-valid infrastructure can still be insecure, expensive, or functionally wrong. Layered tests and policy catch different defect classes before or after real APIs are touched.",
        "ideas": [
            "**Static checks are fast and broad** — formatting, validation, linting, and security scanning should run before cloud tests.",
            "**`terraform test` executes run blocks and assertions** using plan or apply modes according to the test design.",
            "**Plan inspection tests proposed values and actions** without pretending every unknown value is final.",
            "**Policy as code enforces organizational boundaries** such as allowed regions, encryption, tags, and prohibited public exposure.",
        ],
        "example": """### Lab: assert a module contract

```hcl
# tests/defaults.tftest.hcl
run "plan_defaults" {
  command = plan

  variables {
    environment = "dev"
  }

  assert {
    condition     = output.labels["environment"] == "dev"
    error_message = "The environment label must match the input."
  }
}
```

```bash
terraform fmt -check -recursive
terraform init -backend=false
terraform validate
terraform test
```

Add a policy/scanner check that rejects public access or missing encryption, and maintain explicit, reviewed exceptions.""",
        "practice": [
            "Write tests for a default, an override, and an invalid input.",
            "Run a linter and security scanner, then classify findings rather than blindly suppressing them.",
            "Draft a policy rule that denies public storage unless an approved exception exists.",
        ],
        "mistakes": [
            "Treating `terraform validate` as proof that infrastructure is secure",
            "Writing only apply-based tests and leaking costly fixtures after failures",
            "Adding broad policy suppressions with no owner, reason, or expiry",
        ],
        "stretch": "Create an ephemeral integration test that applies, probes a real endpoint, and always destroys through a controlled cleanup job.",
        "quiz": [
            ("What does `terraform validate` primarily check?", ["Configuration syntax and internal consistency", "Live application behavior", "Every security policy", "Cloud cost"], 0),
            ("Where do native test assertions live?", ["`.tftest.hcl` files", "State lock files", "Provider binaries", "Backend logs"], 0),
            ("What can policy as code evaluate?", ["Plan and configuration against guardrails", "Only Markdown", "Only billing exports", "Only Git authors"], 0),
            ("Why layer tests?", ["Different checks catch different defect classes", "To make plans larger", "To avoid cleanup", "To store secrets"], 0),
            ("What must policy exceptions include?", ["Narrow scope, reason, owner, and review/expiry", "Wildcard access", "No documentation", "State content"], 0),
        ],
    },
    "terraform/09-ci-for-terraform": {
        "goals": [
            "Build a CI workflow for format, validation, tests, plan review, and controlled apply",
            "Use workload identity federation and protected environments instead of static cloud keys",
            "Prevent concurrent state writes and preserve auditable plan evidence",
        ],
        "why": "CI turns Terraform from a developer command into a controlled team delivery process. Identity, plan integrity, serialization, and approvals determine whether automation is safer than laptops.",
        "ideas": [
            "**Pull requests should produce readable plans without applying production changes**.",
            "**Apply from a trusted branch and protected environment** using the reviewed commit and controlled approval.",
            "**OIDC federation exchanges CI identity for short-lived cloud credentials** instead of storing long-lived secrets.",
            "**Concurrency controls complement backend locking** by preventing avoidable competing runs for the same environment.",
        ],
        "example": """### Lab: shape a safe GitHub Actions plan job

```yaml
permissions:
  contents: read
  id-token: write
  pull-requests: write
concurrency:
  group: terraform-production
  cancel-in-progress: false
steps:
  - uses: actions/checkout@v4
  - uses: hashicorp/setup-terraform@v3
  - run: terraform fmt -check -recursive
  - run: terraform init -input=false
  - run: terraform validate
  - run: terraform test
  - run: terraform plan -input=false -out=tfplan
  - run: terraform show -no-color tfplan > plan.txt
```

Configure the cloud's OIDC trust outside this snippet. Store the plan as a restricted, short-retention artifact and apply only after verifying the commit and environment approval.""",
        "practice": [
            "Create separate PR plan and protected-branch apply workflows.",
            "Configure or diagram OIDC trust claims restricted to repository, branch, and environment.",
            "Test two queued runs and confirm concurrency plus backend locking prevent overlap.",
        ],
        "mistakes": [
            "Storing cloud access keys as long-lived repository secrets",
            "Applying after merge by generating a different unreviewed plan with changed inputs",
            "Posting plans publicly even though values and structure may be sensitive",
        ],
        "stretch": "Add drift detection that opens a review signal without automatically overwriting intentional emergency changes.",
        "quiz": [
            ("What should a pull-request Terraform job normally produce?", ["Checks and a reviewable plan", "A production apply", "A state deletion", "A force unlock"], 0),
            ("Why use OIDC federation in CI?", ["To obtain short-lived scoped credentials", "To make state public", "To skip IAM", "To remove audit logs"], 0),
            ("What does CI concurrency reduce?", ["Competing runs against one environment", "Provider checksums", "Variable validation", "Output values"], 0),
            ("Why restrict plan artifacts?", ["They can contain sensitive infrastructure data", "They are executable cloud accounts", "They replace state", "They create users"], 0),
            ("What should gate production apply?", ["Trusted branch, reviewed plan/commit, and protected approval", "Any fork pull request", "A formatting failure", "A public secret"], 0),
        ],
    },
    "terraform/10-capstone-module": {
        "goals": [
            "Deliver a reusable Terraform module with documentation, tests, examples, and version constraints",
            "Consume the module from a separate root with remote state and a reviewed plan",
            "Demonstrate safe update, drift handling, and cleanup",
        ],
        "why": "The capstone proves not only HCL fluency but the full infrastructure product lifecycle: interface design, validation, state, testing, delivery, operations, and consumer experience.",
        "ideas": [
            "**Choose one bounded capability** such as a secure storage bucket, network, or small web-service foundation.",
            "**The module is a product** — inputs, outputs, defaults, compatibility, examples, tests, and upgrade notes form its contract.",
            "**The consumer root owns environment concerns** including backend, credentials, provider configuration, and promotion.",
            "**Evidence matters** — show clean checks, reviewed plan, apply, functional verification, no-change plan, and destroy or retention decision.",
        ],
        "example": """### Capstone: verify a reusable module and consumer

```bash
terraform fmt -check -recursive
terraform -chdir=modules/secure-storage init -backend=false
terraform -chdir=modules/secure-storage validate
terraform -chdir=modules/secure-storage test

terraform -chdir=examples/basic init
terraform -chdir=examples/basic plan -out=tfplan
terraform -chdir=examples/basic show -no-color tfplan
terraform -chdir=examples/basic apply tfplan
terraform -chdir=examples/basic plan -detailed-exitcode
```

The module should enforce private access and encryption, emit useful identifiers, and document migration and destruction behavior. Run a reviewed destroy for disposable infrastructure.""",
        "practice": [
            "Publish module files, README, example, tests, changelog, and compatibility constraints.",
            "Use a separate consumer root and remote backend to prove real composition.",
            "Demonstrate invalid-input failure, successful apply, functional check, no-change plan, and cleanup.",
        ],
        "mistakes": [
            "Embedding backend configuration or environment credentials inside the child module",
            "Claiming reusability without a second consumer example or tests",
            "Destroying retained data during demonstration without backup and explicit approval",
        ],
        "stretch": "Tag a semantic release, consume that exact version from another repository, and complete a backward-compatible upgrade.",
        "quiz": [
            ("What belongs in the child module?", ["A bounded capability and stable interface", "Environment backend credentials", "Production state", "CI cloud keys"], 0),
            ("What belongs in the consumer root?", ["Backend, providers, environment inputs, and composition", "Provider binaries in Git", "Module test fixtures only", "Hard-coded secrets"], 0),
            ("What proves idempotence after apply?", ["A no-change plan", "A second forced replacement", "Deleting state", "Changing credentials"], 0),
            ("What should tests include?", ["Defaults, overrides, invalid input, and key guarantees", "Only formatting", "Only README links", "Only destroy"], 0),
            ("What completes disposable capstone evidence?", ["Verified cleanup and residual-resource review", "An unreviewed destroy", "A local state commit", "A wildcard role"], 0),
        ],
    },
}
