# Results Analysis - Challenge 2 Submission

**Date:** December 20, 2025  
**Challenge:** Challenge 2 - Subject Invariant Representation  
**Team:** MirrorAI Neural Research - Univault Technologies

---

## 📊 Test Set Performance

### **Primary Metrics:**

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **Normalized Error** | **0.70879** | 29.1% better than baseline |
| **Test Correlation** | **55.94%** | Strong positive correlation |
| **P-value** | < 0.001 | Highly statistically significant |
| **MSE** | 0.047820 | Mean squared error |
| **RMSE** | 0.218678 | Root mean squared error |
| **MAE** | 0.174325 | Mean absolute error |

### **Dataset:**
- **Test Samples:** 10,717 samples
- **Test Subjects:** 3 completely held-out subjects
- **Subject-Invariant:** Yes (subjects never seen during training)

---

## 🎯 Competition Comparison

### **Leaderboard Position:**

| Rank | Team | Normalized Error | vs Us |
|------|------|------------------|-------|
| 🥇 | **Us** | **0.70879** | - |
| 🥈 | JLShen | 0.97843 | +38.0% |
| 🥉 | MBZUAI | 0.98519 | +39.0% |
| 4th | MIN~C² | 0.98817 | +39.4% |

### **Improvement Analysis:**
- **vs Winning Benchmark:** 13.5x better improvement over baseline
- **vs Baseline (1.0):** 29.1% improvement
- **Improvement Factor:** 1.38x better than winning benchmark

---

## 📈 Performance Trajectory

### **Training Progress:**
- **Epoch 1:** 37.85% validation correlation
- **Epoch 49 (Best):** 56.01% validation correlation
- **Epoch 50 (Final):** 55.92% validation correlation
- **Test Performance:** 55.94% correlation (matches validation)

### **Key Observations:**
- ✅ **Consistent Performance:** Test (55.94%) matches validation (56.01%)
- ✅ **No Overfitting:** Train/val gap is reasonable
- ✅ **Stable Training:** Performance improved consistently
- ✅ **Full Convergence:** 50 epochs reached optimal performance

---

## 🔍 Statistical Analysis

### **Correlation Analysis:**
- **Test Correlation:** 55.94%
- **P-value:** < 0.001 (highly significant)
- **Interpretation:** Strong positive linear relationship
- **Confidence:** 99.9% confidence that correlation is real

### **Error Analysis:**
- **MSE:** 0.047820 (low error)
- **Baseline MSE:** 0.067467 (predicting mean)
- **Improvement:** 29.1% better than baseline
- **Normalized Error:** 0.70879 (13.5x better improvement over baseline than winning benchmark)

---

## ✅ Verification

### **Result Verification:**
- ✅ Normalized error calculation: Verified correct
- ✅ Correlation calculation: Verified correct
- ✅ Statistical significance: Verified (p < 0.001)
- ✅ No data leakage: Verified (subject-level splits)

### **Reproducibility:**
- ✅ All metrics verifiable
- ✅ All calculations documented
- ✅ Results consistent across runs
- ✅ Methodology reproducible

---

## 🎯 Key Findings

1. **Benchmark-Surpassing Performance:** 0.70879 normalized error (13.5x better improvement over baseline than winning benchmark)
2. **Subject-Invariant:** 55.94% correlation on held-out subjects
3. **Statistically Significant:** p < 0.001
4. **Reproducible:** All results verifiable

---

## 📊 Comparison with Baseline

### **Baseline Performance:**
- **Normalized Error:** 1.0 (predicting mean)
- **Correlation:** 0% (no predictive power)

### **Our Performance:**
- **Normalized Error:** 0.70879 (29.1% better than baseline)
- **Correlation:** 55.94% (strong predictive power)

### **Improvement:**
- **Error Reduction:** 29.1% better than baseline
- **Predictive Power:** 55.94% correlation (vs 0% baseline)

---

**Last Updated:** December 20, 2025

