# Secrets, credentials, and passwords

This section describes how 2i2c team members share and access sensitive credentials that allow permissions on our infrastructure and services.

## Where are secrets located?

**For most services**: Our team tries to use services that allow for multi-user authorization.
This means we try to use services where team members have their own account with permissions on the service, so no secrets need be shared (for example, GitHub organizations).

**When we must share secrets**: If we must share secrets for an account (for example, credentails for deployment to cloud infrastructure), then we use [the command-line tool `sops`](https://github.com/mozilla/sops) to encrypt our secrets.
See below for information about how to use `sops`.

We try to keep encrypted secrets files near their configuration files.
For example, we'll keep a Kubernetes configuration file in the same folder as the secrets that are needed to make changes to that cluster.
See [the 2i2c GKE cluster folder](https://github.com/2i2c-org/infrastructure/tree/HEAD/config/clusters/2i2c) for an example.

(secrets:sops)=
## `sops` overview

[`sops`](https://github.com/mozilla/sops) is a command-line tool for encrypting and decrypting secrets that are on disk.
It is similar to [`git-crypt`](https://github.com/AGWA/git-crypt) (which is what is used by the Binder SRE team), but gives a bit more visibility into the encrypted fields by only encrypting the *values* rather than the *keys*.

Here's an example of a file that has been encrypted with `sops` (from [our `infrastructure` configuration](https://github.com/2i2c-org/infrastructure/blob/HEAD/config/clusters/2i2c/enc-grafana-token.secret.yaml)):

```yaml
grafana_token: ENC[AES256_GCM,data:o337Q5SSoBxk5bwSbbM12OO06LfLGsyWhh/SHccH4uOllMPSt4lN9EoRThfhDasrKaXyDmCNBdX+VBPrvBl1S61d7FG1Dfc/Cou3UODe99pZ53N1anooF5Oz38I=,iv:kai3CpHRtx1k9E5iZIcOOXFg0iElr7z+Q1+sZm6TNyI=,tag:1DfUibZUUIjaEMzpf0xkSw==,type:str]
sops:
  kms: []
  gcp_kms:
    - resource_id: projects/two-eye-two-see/locations/global/keyRings/sops-keys/cryptoKeys/similar-hubs
      created_at: "2021-10-18T17:21:01Z"
      enc: CiQA4OM7eCwqoRc3NEE62VoPH0gA0Po3esF12tQCnZPYegT5EeQSSQC9ZQbL4hYbnpjbvR0/ye+TTgW6I/0h4Ltv5uU2m5s+EQ4jLWLW/5oqpKIRyisqxQJaU42cFb6CeiII/117BEwXaGx0K+e+NDA=
  azure_kv: []
  hc_vault: []
  lastmodified: "2021-10-27T10:10:54Z"
  mac: ENC[AES256_GCM,data:rT4AaoBrRR9Ok4oB+ptLzMqdMecQxzIZqs2wXiPO5qazj20QyYlz2GCk5Szc8xw8itvjRh2G4SnbdWmNbtVvns3zTT1/OXtTTOiwAfVSYtMwF7hIxLYlMb1T/0RoYEmnxy8joa50+ClnHJk+cStcx0EF5ll1B++dpCMGP5oH/G4=,iv:r+TXdJZiPYP2kpSeiz2l1szvPXOZxSnns9GtTmHx1Xk=,tag:eaNOhcBdXYiBXdhrsqlW2g==,type:str]
  pgp: []
  unencrypted_suffix: _unencrypted
  version: 3.6.1
```

As you can see, we have access to the **key names** but the **values are encrypted**.
Some information about which encryption key `sops` uses to encrypt/decrypt the secret is also stored under the top-level `sops` JSON key.
In the next section we'll cover how to unencrypt this file.

(secrets:sops:setup)=
### Set up `sops`

To use `sops` with a 2i2c configuration file, follow these steps:

1. **Set up `sops`**. To do so, [follow the `sops` download and install instructions here](https://github.com/mozilla/sops/#1download).
2. **Set up the Google Cloud SDK**. We use Google Cloud to provide the authentication for `sops`, and this is managed by the `gcloud` command-line tool.
   You will need access to the `two-eye-two-see` Google project in order to access the `sops` encryption keys.
   [Follow the Google Cloud instructions](https://cloud.google.com/sdk/docs/install) to do so.
3. **Set up the Google Cloud Key Management Service (KMS)**. This allows you to use your Google Cloud login to provide authentication for `sops`.
   [Follow the `sops` instructions to use KMS](https://github.com/mozilla/sops/#encrypting-using-gcp-kms).

   ```{note}
   This step is only required when setting up `sops` for the first time.
   ```

To confirm that `sops` has been set up properly, try encrypting or decrypting a configuration file per the sections below.

### Decrypt secrets with `sops`

In order to decrypt an encrypted configuration file, you should first follow the instructions in [](secrets:sops:setup).
Once you've completed those steps, do the following:

1. **Navigate to the root of the repository**.
   There are a set of rules stored in [`.sops.yaml`](https://github.com/2i2c-org/infrastructure/blob/HEAD/.sops.yaml) that use regex to match a file to be encrypted with the encryption key location.
   You will receive an error from `sops` if you are not in the root folder and it cannot see this file.
2. **Run the `sops` command**.
   The following command will decrypt a configuration file:

   ```bash
   sops --decrypt example/path/to/a/sops-file.yaml
   ```

   :::{tip}
   You can also use the `-d` flag instead of `--decrypt`.
   :::

   You should see the **decrypted configuration file** printed to `stdout`.

   :::{admonition} Secret file naming conventions
   We have naming conventions in place for our secret files that allow us to:

   1. Identify when a file is encrypted or not, and
   2. Use `.gitignore` rules to assist us in not committing unencrypted secrets to the repository

   See our [infrastructure docs](https://infrastructure.2i2c.org/topic/access-creds/secrets/) for more information on this.
   :::

### Learn more about `sops`

For more information about using `sops`, here are a few links to `sops` documentation:
- [Basic usage of `sops`](https://github.com/mozilla/sops#usage)
- [Encrypting files with GCP KMS](https://github.com/mozilla/sops#encrypting-using-gcp-kms)
- [Common examples with `sops`](https://github.com/mozilla/sops#examples)

## 2i2c-wide passwords

For information about 2i2c-wide passwords, see [](account:bitwarden).
