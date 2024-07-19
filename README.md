# Pulumi IaC Project

This repository contains Infrastructure as Code (IaC) configurations using Pulumi.

At the moment, the project is focused on managing DNS records in CloudFlare.

The records itself are TXT records that are used to verify ownership of a domain by Bluesky.

## Prerequisites

- [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/)
- [CloudFlare Account](https://dash.cloudflare.com/sign-up)
- [Pulumi Access Token](https://app.pulumi.com/account/tokens)
- [CloudFlare API Token](https://dash.cloudflare.com/profile/api-tokens)
- [CloudFlare Zone ID](https://dash.cloudflare.com/)

## Usage

1. Clone the repository
2. Create a new stack using `pulumi stack init <stack-name>`
3. Update GitHub Actions workflow files: `.github/workflows/pull_request.yml` and `.github/workflows/push.yml` with the stack name
4. Set the required environment variables in GitHub Secrets
   - `PULUMI_ACCESS_TOKEN` - Pulumi Access Token
   - `CLOUDFLARE_API_TOKEN` - CloudFlare API Token
5. Update `records` in `__main__.py` with BlueSky account DID's configured to use your domain.
6. Commit and push the changes to the repository, create MR
7. Observe the pipeline execution and validate the changes shown as preview
8. Once validated, merge the MR to main branch
9. Observe the pipeline execution and validate the changes in the CloudFlare dashboard

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
