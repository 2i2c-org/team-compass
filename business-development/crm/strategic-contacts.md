# Strategic Contacts

This document explains to use HubSpot to track **strategic contacts** across members, collaborators, and funders.  

It defines the **three-property system**, the **rules for using it**, and **how team members should interact with it** in day-to-day work.

This system is intentionally simple and optimized for:
- Strategic communications
- Leadership outreach
- Reliable list exports

It is **not** meant to capture every operational or technical relationship.

---

## What is a Strategic Contact?

A **strategic contact** is someone who should reasonably receive:
- Executive or leadership communications
- Funding or partnership-related messages
- High-level coordination or decision-oriented updates

If leadership would *not* expect this person to receive those messages, they are **not** a strategic contact.

---

## The Three Contact Properties (Required)

All strategic contact tracking is handled using **three contact properties**.

### 1. Strategic Contact Status
**Type:** Dropdown select (single)

**Values:**
- Strategic Contact
- Not Strategic

**Purpose:**  
Determines whether the contact should *ever* appear in strategic lists.

**Rule:**
- If this is set to **Not Strategic**, the other two properties do not matter.
- If set to **Strategic Contact**, the other two properties **must** be populated.

---

### 2. Strategic Coverage Category
**Type:** Multiple checkboxes

**Values:**
- Member – Premier
- Member – General
- Collaborator
- Funder

**Purpose:**  
This property exists to make **filtering and segmentation easy**.

**Rule:**
- Select **all categories** for which this person is a strategic contact.
- This property must always align with the Detail property below.

---

### 3. Strategic Coverage Detail
**Type:** Multiple checkboxes

**Purpose:**  
Specifies **exactly which communities, grants, or funders** this person is a strategic contact for.

**Examples:**
- Member – Premier – VEDA
- Member – General – NASA Openscapes
- Collaborator – NSF Project Pythia
- Funder – Sloan

**Rule:**
- Only select entries where the person is a *strategic-level* contact.
- Do not include technical-only or delivery-only relationships.

---

## Core Rules (Non-Negotiable)

When **Strategic Contact Status = Strategic Contact**:

1. **Strategic Coverage Category must not be empty**
2. **Strategic Coverage Detail must not be empty**
3. Category and Detail must be consistent  
   - Example: If “Funder” is selected in Category, at least one “Funder – …” value must appear in Detail

Contacts that violate these rules are considered **invalid** and must be fixed.

---

# HubSpot Segments (Saved Lists)

HubSpot includes pre-built segments that allow downloading of the following lists:

- **All Strategic Contacts**
- **Strategic Contacts of All Members**
- **Strategic Contacts at Premier Members**
- **Strategic Contacts of Major Collaborators**
- **Strategic Contacts of All Funders**

These segments are the **authoritative source** for strategic outreach and reporting.

---

## Task-Specific Guidance

## How to Get a List of Strategic Contacts

Use HubSpot **Segments** (Lists):

1. Go to **Contacts → Segments**
2. Open the appropriate saved segment:
   - *All Strategic Contacts*
   - *Strategic Contacts of All Members*
   - *Strategic Contacts at Premier Members*
   - *Strategic Contacts of Major Collaborators*
   - *Strategic Contacts of All Funders*
3. Use **Export segment** to download the list if needed

Do **not** build ad-hoc filters unless you have a specific reason.

---

## How to Add or Update a Strategic Contact

When adding or editing a contact:

### Step 1 — Decide if they are strategic
Ask:
> Would leadership expect this person to receive strategic communications?

- If **yes** → set `Strategic Contact Status = Strategic Contact`
- If **no** → set `Strategic Contact Status = Not Strategic` and stop

---

### Step 2 — Assign Coverage Category
Select all applicable:
- Member – Premier
- Member – General
- Collaborator
- Funder

---

### Step 3 — Assign Coverage Detail
Select the **specific** communities, grants, or funders where this person is strategic.

Examples:
- A Premier community director →  
  `Member – Premier` + `Member – Premier – VEDA`
- A funder program officer →  
  `Funder` + `Funder – Sloan`
- A grant co-PI →  
  `Collaborator` + `Collaborator – NSF Project Pythia`

---

### Step 4 — Final check before saving
Confirm:
- Status is set correctly
- Category and Detail are both filled
- Category matches Detail

If any of these fail, fix them before saving.

---

## How to Add a New Strategic Coverage Detail Option

New communities, grants, or funders **must** be added centrally.

### When to add a new option
- A new member community joins
- A new major grant or collaboration starts
- A new funder relationship is established

---

### How to add a new option

1. Go to **Settings → Properties → Contacts**
2. Open **Strategic Coverage Detail**
3. Add a new checkbox value using the required naming format:

<Member – Premier | Member – General | Collaborator | Funder> – <Name>

**Examples:**
- `Member – General – New Community`
- `Collaborator – New Grant Name`
- `Funder – New Foundation`

4. Save the property
5. Update relevant contacts

---

### Important rules for new options
- Do **not** invent new naming patterns
- Do **not** add abbreviations unless they are canonical
- Always match the **Category** that will be used with the Detail

---

## Why This System Matters

This structure ensures:
- Reliable strategic mailing lists
- Faster executive coordination
- Fewer “who should we contact?” conversations
- Clean reporting across members, collaborators, and funders

Consistency here saves time everywhere else.
