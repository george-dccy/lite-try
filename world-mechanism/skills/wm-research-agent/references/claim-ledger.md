# Claim Ledger

## Required fields

### claim_id
Stable identifier, e.g. H01-F03.

### claim
The exact sentence or proposition the work may use.

### label
One of:
- F
- I
- H
- R

### scope
- date / period;
- geography;
- population;
- platform / product;
- conditions.

### support
Source ids that directly support the claim.

### confidence
- high
- medium
- low

### allowed_wording
The strongest wording evidence justifies.

### do_not_strengthen_to
A stronger statement that would exceed the evidence.

### notes
Conflicts, caveats, or production implications.

---

## Example

claim_id: H01-F04  
claim: North American railroads adopted Standard Railway Time on November 18, 1883.  
label: F  
scope: North American railroad operations, 1883  
confidence: high  
allowed_wording: "North American railroads switched to Standard Railway Time for rail operations on November 18, 1883."  
do_not_strengthen_to: "The U.S. federal government created time zones in 1883."

---

## Interpretation rule

Interpretations need source grounding but should remain visibly interpretive.

Example:

> “Standard time reduced cross-network coordination cost.”

This may be a strong synthesis, but it is not the same type of claim as:

> “The Standard Time Act passed in 1918.”

Do not give both the same rhetorical status.
