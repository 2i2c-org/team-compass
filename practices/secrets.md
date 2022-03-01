# Secrets, credientials, and passwords

This section describes how 2i2c team members share and access sensitive credentials that allow permissions on our infrastructure and services.

## Where are secrets located?

**For more services**: Our team tries to use services that allow for multi-user authorization.
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

Here's an example of a file that has been encrypted with `sops` (from [our `infrastructure` configuration](https://github.com/2i2c-org/infrastructure/blob/master/config/clusters/2i2c/enc-grafana-token.secret.yaml)):

```yaml
auth0:
    domain: ENC[AES256_GCM,data:aEi/GvnxpyGsvinhZ5sXXto=,iv:SR6sgQronhovtuUpQnSuIO2KFo9eTSP9tgFqg+QBJ8I=,tag:6yzNIPmFEWilI1qajTH1WQ==,type:str]
    client_id: ENC[AES256_GCM,data:aHw7KJCg4Hn2RiLIiONQXnc48/JFsCCnW0WFVLtCFgM=,iv:FFxe1kNtBh5ljroqCTW3wicQzyDszSCSyYx4Boe2Dns=,tag:a/m2QDTrcKpurKq0IZPjOw==,type:str]
    client_secret: ENC[AES256_GCM,data:B+fw9jZUc2b0Mb9CD/Pas+aZLPd3Rp1GI6Wrq0wXYcE5HvMEOXhXOqzl9nEKhbR/cVAh5YZt+xlI8G2zOraWbQ==,iv:nDIxzcuQ5Noxp7HyYsL02hBRDLi9An5MN8IEdLnLffA=,tag:T4GgBUkzfSV5UC8RX8yT2g==,type:str]
secret_key: ENC[AES256_GCM,data:ZT5kb64zUJIEKhUQSKgCRF8HcEnvK59KCtVs6TEO+O3S5qWBJIJY9kivlYU8a93XRN9cxIi9YlG4EfLoFR5JUw==,iv:V5OKGcKfG6s4EKdonrosvFJPltujSp5z4SZ8th9SkYs=,tag:jqQcK4+HO+i8SLerABYxeQ==,type:str]
sops:
    kms: []
    gcp_kms:
        - resource_id: projects/two-eye-two-see/locations/global/keyRings/sops-keys/cryptoKeys/similar-hubs
          created_at: "2021-04-20T11:50:21Z"
          enc: CiQA4OM7eLU3yaaPc6QnzaG3oPhN+OtaG+JCEd57CTIQcOSi+RUSSQBy9hCYh5zsV6u1djsUJPdj+2rwIb3aj0ZWkmZC+XtgXRrGTcI9BuUnnk25yyzi0HWr3CBZxARltajdQHydZCXlY+O28vsySkg=
    azure_kv: []
    hc_vault: []
    age: []
    lastmodified: "2021-06-11T06:36:56Z"
    mac: ENC[AES256_GCM,data:oW0k09Gd65XK0OxRcX9jPaDMatFPrE42A6rdIHvKNQBmM2MY+VECKLbDzci1Ob9VZsp91ss0psn0im28z9G/Fjf6adRwXjtnI7k5KkEwkwivxpnk9RX+ZyPkFn4ccnhbHEciRU4NVS1upFJLCGDs9EBZ6FTXzMEx5aL2jUlLXYA=,iv:oaIR4rwUgcLpEFo19kziEuNJwf407NHPQVsM2pPRvxY=,tag:zozw57Qc1CYVj6TLkiyPlQ==,type:str]
    pgp: []
    unencrypted_suffix: _unencrypted
    version: 3.7.1
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

To confirm that `sops` has been set up properly, try encrypting or decrypting a configuration file per the sections below.

### Decrypt secrets with `sops`

In order to decrypt an encrypted configuration file, you should first follow the instructions in [](secrets:sops:setup).
Once you've completed those steps, do the following:

1. **Navigate to the root of the repository**.
   There are a set of rules stored in [`.sops.yaml`](https://github.com/2i2c-org/infrastructure/blob/master/.sops.yaml) that use regex to match a file to be encrypted with the encryption key location.
   You will receive an error from `sops` if you are not in the root folder and it cannot see this file.
2. **Run the `sops` command**.
   The following command will decrypt a configuration file (in this case, the configuration file in the `infrastructure` repository):

   ```bash
   sops --decrypt config/secrets.yaml
   ```

   :::{tip}
   You can also use the `-d` flag instead of `--decrypt`.
   :::

   You should see the **decrypted configuration file** printed to `stdout`.

   :::{admonition} Decrypt the file in-place
   If you'd like to decrypt a configuration file in-place, use the `--in-place` or `-i` flag.
   This will **overwrite** the configuration file with a decrypted version.
   :::

### Learn more about `sops`

For more information about using `sops`, here are a few links to `sops` documentation:
- [Basic usage of `sops`](https://github.com/mozilla/sops#usage)
- [Encrypting files with GCP KMS](https://github.com/mozilla/sops#encrypting-using-gcp-kms)
- [Common examples with `sops`](https://github.com/mozilla/sops#examples)
