# Project CodeGuard: Security Rules for AI Coding Agents

This project is an AI model-agnostic security framework and ruleset (internally nicknamed "Project CodeGuard" when developed at Cisco) that embeds secure-by-default practices into AI coding workflows (generation and review). It ships core security rules, translators for popular coding agents, and validators to test rule compliance.


## Why Project CodeGuard?

AI coding agents are transforming software engineering, but this speed can introduce security vulnerabilities. Is your AI coding agent implementation introducing security vulnerabilities?

- ❌ Skipping input validation
- ❌ Hardcoding secrets and credentials
- ❌ Using weak cryptographic algorithms
- ❌ Relying on unsafe functions
- ❌ Missing authentication/authorization checks
- ❌ Missing any other security best practice

Project CodeGuard solves this by embedding security best practices directly into AI coding agent workflows. 

**During and After Code Generation.**

These rules can be used for: 
- preventing vulnerabilities from being introduced during code generation
- automated code review by AI agents


## Security Coverage

Our rules cover essential security domains:

- **🔐 Cryptography**: Safe algorithms (including post-quantum cryptography), secure key management, certificate validation
- **🛡️ Input Validation**: SQL injection prevention, XSS protection, command injection defense
- **🔑 Authentication**: MFA best practices, OAuth/OIDC, secure session management
- **⚡ Authorization**: RBAC/ABAC, access control, IDOR prevention
- **📦 Supply Chain**: Dependency security, SBOM generation, vulnerability management
- **☁️ Cloud Security**: IaC hardening, container security, Kubernetes best practices
- **📱 Platform Security**: Mobile apps, web services, API security
- **🔍 Data Protection**: Privacy, encryption at rest/transit, secure storage

## Quick Start

Get started in minutes:

1. **Download the rules** from our [releases page](https://github.com/project-codeguard/rules/releases)
2. **Copy to your project** - Place AI agent and IDE specific rules in your repository
3. **Start coding** - AI assistants will automatically follow security best practices

- Additional details in the [Get Started →](getting-started.md)


## How It Works

1. **Security rules** are written in a unified markdown format
2. **Conversion tools** translate rules to IDE and AI agent formats
3. **AI assistants** reference these rules when generating or reviewing code
4. **Secure code** is produced automatically without developer intervention

## Community

- **📋 Issues**: [Report bugs or request features](https://github.com/project-codeguard/rules/issues)
- **💬 Discussions**: [Join the conversation](https://github.com/project-codeguard/rules/discussions)
- **🤝 Contributing**: [Learn how to contribute](https://github.com/project-codeguard/rules/blob/main/CONTRIBUTING.md)

Copyright © 2025 Cisco Systems, Inc. Licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
