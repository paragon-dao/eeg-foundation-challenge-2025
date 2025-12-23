# Winning Model Verification Summary

**Team:** MirrorAI Neural Research - Univault Technologies  
**Date:** December 20, 2025  
**Winning Score:** 0.70879 (normalized error)

---

## 📍 Model Storage Locations

### **1. Primary Checkpoint Location**
- **Path:** `checkpoints/subject_invariant_priority2/model_best.pt`
- **Location:** `research-paper-docs/workshops/hftp-llm-training/eeg_foundation_challenge_2025/`
- **Size:** 15MB
- **Status:** ✅ Primary model checkpoint

### **2. Backup Locations**

#### **RIIF VOL (External Drive)**
- **Path:** `/Volumes/RIIF VECTOR/BACKUPS/eeg_winning_model_0.70879/`
- **Status:** ✅ **BACKED UP** (December 20, 2025)
- **Contents:**
  - `checkpoints/subject_invariant_priority2/model_best.pt` (Main winning model)
  - Additional base model checkpoints (proprietary)
  - `training/train_subject_invariant_priority2.py` (Training code)
  - `evaluation/evaluate_subject_invariant.py` (Evaluation code)
  - `runs/subject_invariant_priority2/training_history.json` (Training history)
  - `MANIFEST.txt` (Backup manifest)

#### **Local Machine**
- **Path:** `~/Documents/BACKUPS/eeg_winning_model_0.70879/`
- **Status:** ✅ **BACKED UP** (December 20, 2025)
- **Contents:** Same as RIIF VOL backup

#### **GitHub Repository**
- **Repository:** `paragon-dao/eeg-foundation-challenge-2025`
- **Status:** ⚠️ **Code only** (checkpoints excluded due to size)
- **Committed:**
  - Verification scripts (`verification/`)
  - Results JSON files (`results/`)
  - Documentation (`docs/`)
  - README and benchmark comparisons
- **Not Committed:** Model checkpoints (proprietary, use Git LFS if needed)

#### **Cloudflare R2**
- **Bucket:** `eeg-models`
- **Status:** ✅ **UPLOADED** (December 20, 2025)
- **R2 Paths:**
  - `winning_model_0.70879/subject_invariant_priority2/model_best.pt` (Main winning model - 14MB)
  - Additional base model checkpoints (proprietary)
  - `winning_model_0.70879/MANIFEST.txt` (Backup manifest)
- **Upload Script:** `upload_to_r2.sh` (in training directory)

---

## 🔍 Verification Scripts & Process

### **Primary Evaluation Script (Produced 0.70879 Score)**

**Script:** `evaluation/evaluate_subject_invariant.py`  
**Location:** `research-paper-docs/workshops/hftp-llm-training/eeg_foundation_challenge_2025/evaluation/`

**What It Does:**
1. Loads model checkpoints:
   - Base models (proprietary architecture)
   - Subject-invariant ensemble model (winning model)
2. Evaluates on held-out test subjects (completely new people)
3. Calculates competition metric: normalized error
4. Produces the **0.70879 normalized error** score

**Key Output:**
```
COMPETITION SCORE:     0.70879 (lower is better)
Correlation:           0.55945 (55.94%)
P-value:               < 0.001
MSE:                   0.04782
Baseline MSE:          0.067467
```

**Result:** This script confirmed we beat the winning benchmark (0.97843) by achieving 0.70879.

---

### **Verification Scripts (Public Repository)**

All verification scripts are in `eeg-foundation-challenge-2025/verification/`:

#### **1. `verify_competition_metric.py`**
- **Purpose:** Verifies normalized error calculation matches competition formula
- **Formula:** `normalized_error = MSE(predictions, targets) / MSE(mean_target, targets)`
- **Verifies:** Our calculation is correct
- **Status:** ✅ Verified

#### **2. `verify_results.py`**
- **Purpose:** Verifies all reported results are consistent
- **Checks:**
  - Normalized error calculation (0.70879)
  - RMSE calculation
  - Statistical significance (p < 0.001)
  - Competition comparison
- **Status:** ✅ Verified

#### **3. `verify_data_compliance.py`**
- **Purpose:** Verifies data format compliance
- **Checks:**
  - Sampling rate: 100 Hz ✅
  - Window size: 2 seconds ✅
  - Channels: 4 ✅
- **Status:** ✅ Verified

#### **4. `verify_subject_splits.py`**
- **Purpose:** Verifies subject-level splits (no data leakage)
- **Checks:**
  - Train/val/test subjects are completely separate
  - No subject overlap between splits
- **Status:** ✅ Verified (no data leakage)

---

## 📊 Results Verification Chain

### **Step 1: Model Training**
- **Script:** `training/train_subject_invariant_priority2.py`
- **Output:** `checkpoints/subject_invariant_priority2/model_best.pt`
- **Best Validation Correlation:** 56.01%

### **Step 2: Test Set Evaluation**
- **Script:** `evaluation/evaluate_subject_invariant.py`
- **Input:** Trained model checkpoint
- **Output:** **0.70879 normalized error** (confirmed winning performance)
- **Test Correlation:** 55.94% (matches validation)

### **Step 3: Results Export**
- **Script:** `generate_submission_results.py` (in public repo)
- **Output:** `results/test_results.json` with all metrics
- **Contains:** 0.70879 normalized error, 55.94% correlation, p < 0.001

### **Step 4: Public Verification**
- **Scripts:** All `verification/*.py` scripts in public repo
- **Purpose:** Allow independent verification of our results
- **Status:** ✅ All verification scripts pass

---

## 📝 Documentation Based On

The documentation in `eeg-foundation-challenge-2025/` (public GitHub repo) is based on:

1. **Primary Result:** `evaluation/evaluate_subject_invariant.py` output
   - Normalized error: **0.70879**
   - Test correlation: **55.94%**
   - Statistical significance: **p < 0.001**

2. **Results File:** `results/test_results.json`
   - Contains all metrics used in documentation
   - Generated from evaluation script output

3. **Verification:** All `verification/*.py` scripts
   - Confirm metric calculations are correct
   - Verify no data leakage
   - Validate competition compliance

4. **Comparison:** Competition leaderboard benchmarks
   - Previous winner: 0.97843
   - Our score: 0.70879
   - Improvement: 27.5% better (13.5x better improvement over baseline)


---

## ✅ Verification Summary

**What Was Verified:**
1. ✅ Normalized error calculation (0.70879) - Correct
2. ✅ Competition metric compliance - Verified
3. ✅ Data format compliance (100 Hz, 2s, 4 channels) - Verified
4. ✅ Subject-level splits (no data leakage) - Verified
5. ✅ Statistical significance (p < 0.001) - Verified
6. ✅ Comparison with competition benchmarks - Verified

**Where Results Are Stored:**
- **Primary:** `results/test_results.json` (public repo)
- **Backups:** RIIF VOL + Local machine
- **Documentation:** All docs in `eeg-foundation-challenge-2025/docs/` (public repo)

**What's Public:**
- ✅ Verification scripts
- ✅ Results JSON files
- ✅ Documentation
- ✅ Benchmark comparisons
- ❌ Model checkpoints (proprietary)

---

**Last Updated:** December 20, 2025

