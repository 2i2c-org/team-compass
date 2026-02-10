# Strategic Contacts — HubSpot Guide

This document explains how to use HubSpot to track **strategic contacts** across members, collaborators, and funders.

This system is optimized for strategic communications, leadership outreach, and reliable list exports. It is **not** meant to capture every operational or technical relationship.

## What Is a Strategic Contact?

A **strategic contact** is someone who should reasonably receive executive communications, funding or partnership messages, or high-level coordination updates.

> **The test:** Would leadership expect this person to receive strategic communications?  
> If not, they are **not** a strategic contact.

## How to Export a List of Strategic Contacts

1. Go to **Contacts → Segments**
2. Open one of the saved segments:
   - All Strategic Contacts
   - Strategic Contacts of All Members
   - Strategic Contacts at Premier Members
   - Strategic Contacts of Major Collaborators
   - Strategic Contacts of All Funders
3. Use **Export segment** to download

## How to Add or Update a Strategic Contact

### Step 1 — Is this person strategic?

- **Yes** → set `Strategic Contact Status = Strategic Contact` and continue to Step 2.
- **No** → set `Strategic Contact Status = Not Strategic` and **stop here. Nothing else is needed.**

### Step 2 — Assign Coverage Category

Select **all** that apply:

- Member — Premier
- Member — General
- Collaborator
- Funder

### Step 3 — Assign Coverage Detail

Select the **specific** communities, grants, or funders where this person is strategic.

**Examples:**

| Scenario | Category | Detail |
|----------|----------|--------|
| Premier community director | Member — Premier | Member — Premier — VEDA |
| Funder program officer | Funder | Funder — Sloan |
| Grant co-PI | Collaborator | Collaborator — NSF Project Pythia |

### Step 4 — Validate before saving

Confirm the contact passes the **Core Rules** (see below). Fix any issues before saving.

## How to Add a New Coverage Detail Option

When a new member community joins, a new major grant starts, or a new funder relationship is established, the option must be added centrally.

1. Go to **Settings → Properties → Contacts**
2. Open **Strategic Coverage Detail**
3. Add a new checkbox value using this naming format:

   `<Category> — <Name>`

   Where `<Category>` is one of: `Member — Premier`, `Member — General`, `Collaborator`, or `Funder`.

   **Examples:**
   - `Member — General — New Community`
   - `Collaborator — New Grant Name`
   - `Funder — New Foundation`

4. Save the property
5. Update relevant contacts

**Rules:** Do not invent new naming patterns or add abbreviations unless they are canonical. The Category prefix must match what will be used in the Category property.

## Core Rules

When `Strategic Contact Status = Strategic Contact`:

1. **Coverage Category must not be empty.**
2. **Coverage Detail must not be empty.**
3. **Category and Detail must be consistent** — e.g., if "Funder" is selected in Category, at least one "Funder — …" value must appear in Detail.

Contacts that violate these rules are **invalid** and must be fixed.

## Reference: The Three Contact Properties

### 1. Strategic Contact Status
- **Type:** Dropdown (single select)
- **Values:** `Strategic Contact` · `Not Strategic`
- **Rule:** If set to "Not Strategic," the other two properties are ignored. If set to "Strategic Contact," the other two **must** be populated.

### 2. Strategic Coverage Category
- **Type:** Multiple checkboxes
- **Values:** `Member — Premier` · `Member — General` · `Collaborator` · `Funder`
- **Rule:** Select all categories that apply. Must align with Detail.

### 3. Strategic Coverage Detail
- **Type:** Multiple checkboxes
- **Values:** Specific entries like `Member — Premier — VEDA`, `Funder — Sloan`, `Collaborator — NSF Project Pythia`, etc.
- **Rule:** Only select entries where the person is a strategic-level contact. Do not include technical-only or delivery-only relationships.
