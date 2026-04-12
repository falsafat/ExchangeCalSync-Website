---
title: Privacy Policy
---

# Privacy Policy — ExchangeCalSync

**Last updated: April 12, 2026**

ExchangeCalSync ("the App") is a macOS menu-bar application that synchronizes calendar events from a Microsoft Exchange Server into Apple Calendar. Your privacy is important to us. This policy explains how the App handles your data.

## Data Collection

**ExchangeCalSync does not collect, transmit, or share any personal data with the developer or any third party.**

All data processed by the App stays entirely on your device.

## Data Stored Locally

The App stores the following data **locally on your Mac only**:

- **Exchange username & password** — stored in the macOS Keychain (encrypted), used to authenticate with your Exchange server.
- **Sync state & event mappings** — stored in a SQLite database in Application Support, used to track which events have been synced.
- **Application logs** — stored in Application Support, used for debugging. PII is automatically redacted.

## Network Communication

The App connects **only** to the Exchange server URL you provide during setup. All connections use HTTPS (TLS 1.2 or higher). The App does not contact any other servers, analytics services, or tracking endpoints.

## Calendar Access

The App requests access to Apple Calendar via the EventKit framework to create and manage synced events. Calendar data is never transmitted outside your device.

## Keychain Access

Your Exchange credentials are stored in the macOS Keychain, which is encrypted and protected by your Mac's login password. The App never displays, logs, or transmits your password.

## Data Retention

All data remains on your device for as long as the App is installed. Uninstalling the App removes all associated data from Application Support. Keychain items can be removed via the Keychain Access utility or from within the App's settings.

## Children's Privacy

The App is not directed at children under 13 and does not knowingly collect data from children.

## Changes to This Policy

If this policy changes, the updated version will be posted at this URL with a new "Last updated" date.

## Contact

If you have questions about this privacy policy, please open an issue at:
[https://github.com/falsafat/ExchangeCalSync/issues](https://github.com/falsafat/ExchangeCalSync/issues)
