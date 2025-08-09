# Developer Guide: Matching Algorithm

**Audience:** Developers contributing to the implementation, maintenance, and enhancement of the ThinkAlike Value-Based Matching Algorithm.

---

## 1. Introduction to the ThinkAlike Matching Algorithm

This guide provides a comprehensive overview of the ThinkAlike Value-Based Matching Algorithm, a core component of the platform responsible for connecting users based on shared values and ethical alignment. This algorithm is central to fulfilling ThinkAlike's mission of fostering authentic human connection and building a more humane digital world.

### 1.1 Purpose and Goals

The primary purpose of the Matching Algorithm is to:

- **Identify Value-Aligned Connections:**
  Accurately and ethically identify potential connections between ThinkAlike users who exhibit a high degree of compatibility based on their Value Profiles.

- **Prioritize Ethical Congruence:**
  Go beyond superficial similarity and prioritize matches based on shared core ethical values and a commitment to Enlightenment 2.0 principles.

- **Empower User Choice and Agency:**
  Provide users with transparent and informative Matching Percentages and visualizations, empowering them to make informed decisions about connection seeking and relationship building within the ThinkAlike ecosystem.

- **Contribute to a Value-Driven Ecosystem:**
  Foster a platform-wide emphasis on value-based connections, encouraging users to build relationships and communities grounded in shared ethical foundations.

### 1.2 Core Principles

The Matching Algorithm is designed and implemented in accordance with the following core principles, ensuring ethical rigor and alignment with ThinkAlike's values:

- **Value-Centricity:**
  Value Profiles are the primary data source and driving force behind the matching process. Shared ethical values are prioritized above other matching criteria.

- **Ethical Weighting:**
  The algorithm employs "Ethical Weighting" to prioritize connections based on ethically aligned values and subtly discourage dystopia-aligned connections, while maintaining transparency and avoiding bias.

- **Transparency and Explainability:**
  The algorithm’s logic, weighting mechanisms, and data flows are meticulously documented and designed for transparency, ensuring auditability and user understanding.

- **User Control and Customization:**
  Users retain control over their Value Profiles and can influence matching criteria through customizable profile settings and feedback mechanisms.

- **Data Privacy and Minimization:**
  The algorithm operates within the boundaries of ThinkAlike's data privacy policies, minimizing data collection and ensuring secure and ethical handling of user information.

---

## 2. Algorithm Architecture and Data Flow

The Matching Algorithm operates as a key component within ThinkAlike's backend architecture, interacting with various modules and data sources to generate value-based matches. The high-level architecture and data flow are as follows:

1. **Value Profile Data Input:**
   The algorithm receives User Value Profiles as primary input data. These Value Profiles are constructed from:

   - **Explicitly Stated Values:**
     User-defined values and preferences articulated in their profiles.
   - **Narrative-Revealed Values:**
     Implicitly inferred values derived from user interactions within Narrative Mode (Mode 1).
   - **User Activity Data:**
     Aggregated and anonymized user activity data within the ThinkAlike platform (e.g., community memberships, content interactions—used cautiously and ethically).

2. **Matching Percentage Calculation (Ethically Weighted):**
   The core of the algorithm performs a comparative analysis of User Value Profiles, calculating a **Matching Percentage Score** for each user pair. This calculation incorporates:

   - **Value Overlap Assessment:**
     Quantifying the degree of overlap and congruence between the explicitly stated and narrative-revealed values of two User Nodes.
   - **Ethical Weighting Application:**
     Applying pre-defined ethical weights to different value categories, prioritizing matches based on shared ethical principles (e.g., giving higher weight to "Transparency" or "User Empowerment" values).
   - **Similarity Scoring Metrics:**
     Utilizing appropriate similarity scoring metrics (e.g., cosine similarity, Jaccard index, custom value-based scoring functions—details to be further specified) to quantify the overall value alignment between User Profiles.

3. **Matching Output and Data Delivery:**
   The algorithm outputs a ranked list of potential matches for each user, ordered by their Matching Percentage Score. This output data includes:

   - A list of matched User Nodes (User IDs or References).
   - The Matching Percentage Score for each match.
   - **Justification Data (for DataTraceability.jsx Visualization):**
     Data structured for visualization in the `DataTraceability.jsx` component, highlighting the specific Value Nodes and connection pathways that contributed to the Matching Percentage Score, enhancing transparency and explainability for users.

4. **Integration with Verification System:**
   The Matching Algorithm is tightly integrated with the Verification System to ensure ethical compliance and transparency:
   - **Algorithm Logic Documentation:**
     The complete logic, weighting mechanisms, and scoring functions of the Matching Algorithm are meticulously documented within the Verification System, ensuring auditability and transparency.
   - **Bias Detection and Mitigation Modules:**
     The Verification System incorporates bias detection and mitigation modules that continuously monitor the Matching Algorithm for potential biases across different user demographics and data sets, triggering alerts and providing data insights for ethical refinement.
   - **Ethical Lineage Tracking:**
     All updates and modifications to the Matching Algorithm code are rigorously tracked and versioned within the Verification System, maintaining a clear "ethical lineage" and facilitating ongoing ethical review and accountability.

---

## 2.1 Resonance Score Calculation: Algorithmic Implementation

The ThinkAlike Matching Algorithm operationalizes the resonance logic as defined in the [Resonance Logic Protocol](../realms/resonance_network/resonance_logic_protocol.md). Each factor is implemented as follows:

### Glyph Coherence (30%)
- **Algorithm:** Sequence and set matching of glyph IDs, weighted by glyph rarity and order. High-density or rare glyph matches amplify the score.
- **Data:** `user.glyph_profile` (array of glyph objects with metadata).

### Trait Affinity (20%)
- **Algorithm:** Jaccard or cosine similarity on symbolic trait vectors.
- **Data:** `user.value_profile.traits`.

### Archetype Orbit (15%)
- **Algorithm:** Graph proximity or categorical distance between user archetype assignments. Harmonic resonance is recognized for complementary archetypes.
- **Data:** `user.archetype_roles`.

### Narrative Echo (15%)
- **Algorithm:** Symbolic motif extraction and overlap scoring from narrative logs. Uses NLP and symbolic pattern matching.
- **Data:** `user.narrative_fragments`, `user.onboarding_choices`.

### Temporal Phase Sync (10%)
- **Algorithm:** Time-windowed event matching (e.g., overlapping life events, onboarding timestamps).
- **Data:** `user.event_timeline`.

### Trust Lineage (10%)
- **Algorithm:** Graph traversal for shared trusted connections or community membership.
- **Data:** `user.trust_network`.

Each layer's score is normalized and multiplied by its weight. The final resonance score is the weighted sum of all layers.

---

## 2.2 Data Structures Consumed

- **Value Profile:** Central structure, includes traits, values, archetypes, glyphs, and narrative elements.
- **Resonance Profile:** Aggregates all symbolic, narrative, and temporal data for scoring.
- **Chrona/Timeline:** Used for temporal and trust lineage calculations.

---

## 2.3 Ethical Weighting in Practice

- **Weights:** The weights from the Resonance Logic Protocol (e.g., 30% for glyph coherence) are applied as multipliers in the scoring function.
- **Implementation:**
  - Weighted sum: `score = Σ (layer_score × layer_weight)`
  - All weights and their rationale are versioned and auditable.

---

## 2.4 Verification System Integration

- **Bias Detection:** Matching results and demographic breakdowns are sent to the Verification System for bias analysis.
- **Ethical Compliance:** All algorithm updates are logged and reviewed; ethical lineage is tracked.
- **Feedback Loop:** The Verification System can trigger reweighting or flag problematic matches.

---

## 2.5 Transparency & Traceability Data

- **Traceability Output:** For each match, output a breakdown of which factors contributed most, with references to the user’s Value Profile and narrative.
- **UI Integration:** Data is formatted for `DataTraceability.jsx` to visualize the matching rationale for users.

---

## 2.6 Agent Roles and Visualization Cues

- **Agents:** Harmonia, Eos Lumina, Aura Matchmaker (planned), Echo Lysithea, and others mediate, explain, and safeguard the matching process. See [Agent Ecosystem Design](../seed/framework/agent_ecosystem_design.md).
- **Visualization:** Each resonance factor may be visualized in the UI (e.g., glyph pulses, constellation arcs, narrative threads) to enhance user understanding and trust.

---

## 2.7 Legacy References and Migration Notes

- This guide synthesizes and supersedes technical content from legacy files such as `matching_algorithm_guide.md` (archive), `resonance_matching_protocol.md`, and `glyphic_identity_matrix.md`. See [resonance_logic_protocol.md](../realms/resonance_network/resonance_logic_protocol.md) for conceptual details.
- Legacy files are now marked as "Reviewed – Content Integrated" and should reference this canonical guide for implementation.

---

## 3. Ethical Weighting Implementation Details

A key innovation of the ThinkAlike Matching Algorithm is its implementation of "Ethical Weighting." This section provides developers with specific guidance on how to implement ethical weighting effectively and ethically within the algorithm.

- **Define Value Categories and Ethical Weights:**

  - **Establish Value Taxonomy:**
    Clearly define a taxonomy of core values relevant to Enlightenment 2.0 principles and the ThinkAlike project mission. This taxonomy should encompass categories such as "Transparency," "User Empowerment," "Data Privacy," "Community," "Ethical AI," "Social Justice," etc. (Refer to the [Ethical Guidelines](../ethics/ethical_guidelines.md) and [Manifesto](../seed/core/scintilla_conscientiae_harmonicae_nascentis.md) for a comprehensive list of core values).
  - **Assign Ethical Weights to Value Categories:**
    Assign numerical "ethical weights" to each value category, reflecting their relative importance in the ThinkAlike ethical framework. Values that are deemed more central to Enlightenment 2.0 principles and user well-being should be assigned higher weights. These weights should be carefully considered, transparently documented within the Verification System, and potentially subject to community review and feedback.
    _Example (Illustrative - Weights are for example only and need careful deliberation):_

    ```python
    value_weights = {
      "Transparency": 0.9,  # High ethical weight - Core Enlightenment 2.0 principle
      "User Empowerment": 0.9, # High ethical weight - Core Enlightenment 2.0 principle
      "Data Privacy": 0.8,    # High ethical weight - User Rights and Ethical Data Handling
      "Ethical AI": 0.8,       # High ethical weight - Responsible Technology Development
      "Community": 0.7,       # Medium ethical weight - Important for ThinkAlike vision
      "Authenticity": 0.7,    # Medium ethical weight - Important for ThinkAlike vision
      "Innovation": 0.5,      # Lower ethical weight - Less directly related to core ethical principles, but still relevant
      "Efficiency": 0.3       # Lower ethical weight - Primarily a technical/practical consideration
    }
    ```

  - **Document Rationale for Ethical Weights:**
    Meticulously document the rationale and ethical reasoning behind the assigned weights for each value category within the Verification System. This documentation should explain _why_ certain values are prioritized over others and justify the specific numerical weights assigned, ensuring transparency and auditability of the ethical weighting scheme.

- **Implement Weighting in Matching Algorithm Logic:**

  - **Modify Similarity Scoring Functions:**
    Adapt the similarity scoring functions within the Matching Algorithm to incorporate ethical weights. This could involve:
    - **Weighted Summation:**
      Calculate the overall Matching Percentage as a weighted summation of value alignment scores, where each value category's contribution to the overall score is multiplied by its corresponding ethical weight.
    - **Hierarchical Weighting:**
      Implement a hierarchical weighting scheme where matches based on higher-weighted ethical values are prioritized more strongly in the ranking and presentation of match results. \* **Algorithmic Bias Mitigation Techniques:**
      Integrate bias mitigation techniques into the weighting scheme to prevent unintended biases from being amplified by the ethical weights. Ensure that the weighting scheme does not disproportionately disadvantage or exclude any user groups based on demographic factors or other protected characteristics.

- **Ensure Transparency and User Understanding of Ethical Weighting:**
  - **Explain Ethical Weighting in User Documentation (Onboarding Manual, User Guides):**
    Clearly explain the concept of "Ethical Weighting" in user-facing documentation, **particularly in the Onboarding Manual (Mode 1 Narrative) and User Guides for Matching Mode and Community Mode, ensuring users understand _why_ and _how_ value alignment is prioritized in ThinkAlike's connection and community building processes.**

---

_End of Matching Algorithm Guide segment_

---

## Document Details

- Title: ThinkAlike Project - Developer Guide: Matching Algorithm
- Type: Developer Guide / Architectural Specification
- Version: 1.0 (Adopted from Archive)
- Last Updated: 2025-05-31
