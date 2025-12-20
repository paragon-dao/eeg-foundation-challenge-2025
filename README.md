# EEG Foundation Challenge 2025 - Challenge 2 Submission

**Team:** MirrorAI Neural Research - Univault Technologies  
**Challenge:** Challenge 2 - Subject Invariant Representation  
**Date:** December 20, 2025  
**Status:** ✅ Benchmark Surpasses Winning Solution (Independent Evaluation)  
**Competition Website:** [EEG Foundation Challenge 2025](https://eeg2025.github.io/)

---

## About This Challenge

This submission is part of the **[EEG Foundation Challenge 2025: From Cross-Task to Cross-Subject EEG Decoding](https://eeg2025.github.io/)**, a biosignal challenge accepted to the **NeurIPS 2025 Competition Track**. The competition aims to advance the field of EEG decoding by addressing two critical challenges:

1. **Cross-Task Transfer Learning**: Developing models that can effectively transfer knowledge from any cognitive EEG tasks to active tasks
2. **Subject Invariant Representation**: Creating robust representations that generalize across different subjects while predicting clinical factors

This submission addresses **Challenge 2: Subject Invariant Representation**, where participants predict continuous psychopathology scores (externalizing factor) from EEG recordings across multiple experimental paradigms, with the requirement that models must generalize to completely new subjects not seen during training.

**Competition Details:**
- **Dataset:** HBN-EEG dataset with over 3,000 participants across six cognitive tasks
- **Submissions:** 8,400+ submissions from teams worldwide
- **Organizers:** Meta, Child Mind Institute, UC San Diego, and leading neuroscience institutions
- **Website:** [https://eeg2025.github.io/](https://eeg2025.github.io/)

---

## 📋 Important Context

**Competition Submission Status:** Although we were not aware of the competition timeframe and did not submit our solution for official consideration, our independent evaluation demonstrates that our **harmonic frequency (HF) model** achieves a normalized error score of **0.70879—27.5% better than the winning benchmark** (0.97843). Based on this benchmark, we can confidently state that our solution works and meets the competition's rigorous standards. Therefore, we are publishing these verifiable testings and documents to demonstrate the scientific rigor and real-world usefulness of our HF model architecture, which was trained on EEG data for the following critical applications:

### Our Team's Long-Term Commitment

This breakthrough represents more than a competition achievement—it's the culmination of years of deep inquiry into human consciousness, coherence, and the relationship between our bodies and the universe. Our team at MirrorAI Neural Research (Univault Technologies) has literally **slept on these problems**, studying how human consciousness interacts with planetary rhythms during sleep, investigating correlations between free will and external influence when the mind is at rest, and exploring how the human body functions as a coherence system embedded within Earth–Moon resonance architecture.

Our work builds upon the [Coherence-Mediated Human Coupling Hypothesis (CMH)](https://github.com/paragon-dao/coherence-biological-physics/blob/main/cmh-compiled/cmh-full.md), which proposes that human beings are planetarily tuned coherence systems whose heart-centered oscillatory dynamics and structural geometry enable nonlocal coupling mediated by the Earth–Moon system. This framework has informed our understanding that human beings are active coherence nodes within a vast, layered resonant field—biological, planetary, and potentially cosmic.

**What drives us:** We have been deeply concerned—even alarmed—by the rising rate of suicides and suicidal thoughts, especially among youth worldwide. The paradox of economically and technologically advanced countries like Japan and South Korea having suicide rates way above the global baseline has puzzled us and motivated our research. We believe the answer may lie in understanding how human beings function as coherence systems—how our mental health depends on our connection to ourselves, to each other, and to the planetary rhythms that have shaped human biology for millions of years.

**Why this breakthrough matters:** This success validates that we're moving in the right direction. We can now predict individual mental health differences (not just averages), opening possibilities for early intervention and personalized treatment. For a team that has spent years studying how human bodies interact with each other and the universe, this breakthrough is more than encouraging—it's a sign that our long-term inquiry into human coherence, connection, and consciousness is bearing fruit in ways that could genuinely help address one of humanity's most pressing crises: the mental health epidemic affecting our youth.

### Use Cases for Our Harmonic Frequency (HF) Model

1. **Mental Health Screening**
   - Early detection of behavioral problems (externalizing factor)
   - Objective biomarker (EEG) vs. subjective questionnaires
   - Early intervention before symptoms manifest

2. **Suicide Prevention (988 Lifeline)**
   - Real-time mental health assessment during crisis calls
   - Identify high-risk individuals (externalizing behaviors linked to suicide risk)
   - Subject-invariance ensures models work on new callers

3. **Soundbite Testing (Content Validation)**
   - SoundbiteTesting.com: Validate content impact on human brains
   - Test AI-generated vs. human-created audio
   - Ensure models work across diverse populations

4. **Model Hallucination Prevention (Testing Framework)**
   - **Statistical rigor prevents false positives:** Our testing framework employs rigorous statistical methods (p-values < 0.05, effect sizes > 0.5, confidence intervals, multiple comparison correction via Benjamini-Hochberg FDR) to distinguish real model performance from spurious correlations and random chance. This prevents models from "hallucinating" patterns that don't actually exist in the data.
   - **Subject-level splits ensure no data leakage:** By evaluating on completely held-out subjects (not seen during training), we ensure models are tested on truly novel data, preventing overfitting and false confidence from data leakage—a critical requirement for detecting when models make predictions based on memorized patterns rather than learned generalizable features.
   - **Multi-metric validation:** Our framework tests multiple independent metrics (engagement, joy, coherence, stress) and requires consensus across metrics, ensuring that model predictions are validated through multiple lenses rather than relying on a single potentially misleading metric.
   - **Reproducible methodology:** All results are verifiable through open-source verification scripts, ensuring that model performance claims can be independently validated and preventing "hallucinated" results that cannot be reproduced.

5. **Clinical Assessment**
   - Pediatric primary care: Routine mental health screening
   - School mental health screening: Annual assessments
   - Early referral: Identify children needing specialist care

6. **Personalized Treatment**
   - Individual "profiles" enable personalized treatment plans
   - Monitor treatment response via EEG changes
   - Track developmental trajectories

---

## 📊 Results Summary

### **Competition Performance:**

| Metric | Our Score | Winning Benchmark | Improvement |
|--------|-----------|-----------------|-------------|
| **Normalized Error** | **0.70879** | 0.97843 (JLShen) | **27.5% better** |
| **Test Correlation** | **55.94%** | N/A | - |
| **Statistical Significance** | p < 0.001 | - | Highly significant |

### **Benchmark Comparison:**
- **Our Score:** 0.70879 (normalized error)
- **Winning Benchmark (JLShen):** 0.97843
- **2nd Place Benchmark (MBZUAI):** 0.98519
- **3rd Place Benchmark (MIN~C²):** 0.98817
- **Improvement:** Our score is 27.5% better than the winning benchmark

---

## 📁 Submission Contents

### **1. Verification Scripts** (`verification/`)
- `verify_competition_metric.py` - Verifies normalized error calculation
- `verify_data_compliance.py` - Verifies data format compliance (100 Hz, 2s windows, 4 channels)
- `verify_subject_splits.py` - Verifies subject-level splits (no data leakage)
- `verify_results.py` - Verifies our reported results

### **2. Results** (`results/`)
- `test_results.json` - Test set evaluation results
- `benchmark_comparison.json` - Comparison with competition benchmarks
- `performance_metrics.json` - Detailed performance metrics

### **3. Benchmarks** (`benchmarks/`)
- `competition_benchmarks.md` - Competition leaderboard benchmarks
- `comparison_analysis.md` - Detailed comparison analysis

### **4. Documentation** (`documentation/`)
- `PEER_REVIEW_REPORT.md` - Comprehensive peer review report
- `METHODOLOGY.md` - High-level methodology (without proprietary details)
- `RESULTS_ANALYSIS.md` - Detailed results analysis

---

## 🔍 Verification Instructions

### **Step 1: Verify Competition Metric**
```bash
cd verification
python verify_competition_metric.py
```

### **Step 2: Verify Data Compliance**
```bash
python verify_data_compliance.py
```

### **Step 3: Verify Subject Splits**
```bash
python verify_subject_splits.py
```

### **Step 4: Verify Results**
```bash
python verify_results.py
```

---

## 📊 Key Achievements

1. **27.5% Better** than winning benchmark
2. **55.94% Test Correlation** on held-out subjects
3. **Subject-Invariant Performance** (generalizes to new subjects)
4. **Statistically Significant** (p < 0.001)

---

## ⚠️ Important Notes

- **Model Architecture:** Proprietary (not included in submission)
- **Training Code:** Proprietary (not included in submission)
- **Checkpoints:** Proprietary (not included in submission)
- **Verification Code:** Public (included for reproducibility)
- **Results:** Public (included for verification)

---

## 📚 Citation

If you use our results or methodology, please cite:

```
[Your Citation Here]
```

---

**Last Updated:** December 20, 2025  
**Status:** ✅ Ready for Submission

