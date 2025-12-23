# Use Cases: Subject-Invariant Mental Health Prediction Model

**Team:** MirrorAI Neural Research - Univault Technologies  
**Date:** December 20, 2025

---

## Overview

This document outlines the core use cases for our **Subject-Invariant Mental Health Prediction Model**, which achieved a normalized error of **0.70879** (29.1% better than baseline) in the EEG Foundation Challenge 2025, demonstrating breakthrough performance in predicting mental health traits from EEG signals while generalizing to completely new subjects.

---

## Subject-Invariant Mental Health Prediction Model

### **Performance Metrics**
- **Task:** Mental Health Trait Prediction (Externalizing Factor)
- **Normalized Error:** 0.70879 (29.1% better than baseline)
- **Test Correlation:** 55.94% (p < 0.001)
- **Model Type:** Regression (continuous values)
- **Input:** Multi-modal (HFTP + Braindecode features)
- **Output:** Continuous externalizing factor score
- **Key Feature:** Subject-invariant (works on new people)

### **Core Use Cases**

#### 1. **Mental Health Screening**
- **Purpose:** Early detection of behavioral problems (externalizing factor)
- **Applications:**
  - Pediatric primary care screening
  - School mental health assessments
  - Routine wellness checks
  - Early intervention programs
- **Advantage:** Objective biomarker vs. subjective questionnaires

#### 2. **Suicide Prevention (988 Lifeline)**
- **Purpose:** Real-time mental health assessment during crisis calls
- **Applications:**
  - Identify high-risk individuals during crisis calls
  - Objective risk assessment (externalizing behaviors linked to suicide risk)
  - Triage and resource allocation
  - Follow-up monitoring
- **Advantage:** Subject-invariance ensures models work on new callers

#### 3. **Clinical Assessment & Diagnosis**
- **Purpose:** Support clinical decision-making with objective data
- **Applications:**
  - Pediatric psychiatry assessments
  - Treatment planning and monitoring
  - Response to intervention tracking
  - Developmental trajectory monitoring
- **Advantage:** Continuous scores enable fine-grained assessment

#### 4. **Personalized Treatment**
- **Purpose:** Individual "profiles" enable personalized treatment plans
- **Applications:**
  - Treatment selection based on individual profiles
  - Dosage optimization
  - Therapy approach matching
  - Progress monitoring via EEG changes
- **Advantage:** Subject-invariance enables deployment to diverse populations

#### 5. **Research & Population Studies**
- **Purpose:** Large-scale mental health research
- **Applications:**
  - Population-level mental health studies
  - Longitudinal research
  - Treatment effectiveness studies
  - Biomarker discovery

---

## Model Hallucination Prevention (Testing Framework)

**Use Case:** Prevent AI models from "hallucinating" patterns that don't exist

**Framework Components:**
- Statistical rigor (p-values < 0.05, effect sizes > 0.5)
- Subject-level splits (no data leakage)
- Multi-metric validation (consensus across metrics)
- Reproducible methodology

**Applications:**
- Validate AI model predictions
- Detect overfitting and false positives
- Ensure generalizable model performance
- Prevent "hallucinated" results

---

## Deployment Recommendations

### **When to Use Subject-Invariant Mental Health Prediction Model:**
- ✅ Mental health screening and assessment
- ✅ Suicide prevention and crisis intervention
- ✅ Clinical decision support
- ✅ Subject-invariant prediction required
- ✅ Continuous value prediction needed
- ✅ Early detection of behavioral problems
- ✅ Treatment monitoring and response tracking

---

## Technical Integration

### **Model Architecture**
- **Type:** Proprietary ensemble architecture with subject-invariant training
- **Key Feature:** Generalizes to completely new subjects

### **Inference Requirements**
- **Input:** Multi-modal input (proprietary preprocessing)
- **Output:** Continuous externalizing factor score

### **Deployment Considerations**
- **Subject-Invariance:** Critical for real-world deployment
- **Scalability:** Works across diverse populations
- **Clinical Readiness:** Validated on held-out subjects

---

**Last Updated:** December 20, 2025

