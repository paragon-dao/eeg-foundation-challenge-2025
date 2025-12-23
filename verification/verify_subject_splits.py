#!/usr/bin/env python3
"""
Verify Subject-Level Splits (No Data Leakage)

This script verifies that our dataset uses proper subject-level splits
with no data leakage (subjects don't appear in multiple splits).

Competition Requirement: Subject-invariant evaluation
- Train subjects: Never appear in test
- Val subjects: Never appear in train or test
- Test subjects: Completely held-out
"""

import json
from pathlib import Path

def verify_subject_splits():
    """Verify subject-level splits"""
    print("="*70)
    print("SUBJECT-LEVEL SPLITS VERIFICATION")
    print("="*70)
    print()
    
    results_file = Path(__file__).parent.parent / "results" / "test_results.json"
    if results_file.exists():
        with open(results_file, 'r') as f:
            results = json.load(f)
        
        splits = results.get('splits', {})
        
        train_subjects = set(splits.get('train_subjects', []))
        val_subjects = set(splits.get('val_subjects', []))
        test_subjects = set(splits.get('test_subjects', []))
        
        print("📊 Dataset Splits:")
        print(f"   Train: {len(train_subjects)} subjects, {splits.get('train_samples', 0)} samples")
        print(f"   Val:   {len(val_subjects)} subjects, {splits.get('val_samples', 0)} samples")
        print(f"   Test:  {len(test_subjects)} subjects, {splits.get('test_samples', 0)} samples")
        print()
        
        # Check for overlap
        train_val_overlap = train_subjects & val_subjects
        train_test_overlap = train_subjects & test_subjects
        val_test_overlap = val_subjects & test_subjects
        
        print("🔍 Checking for Data Leakage:")
        print()
        
        if not train_val_overlap:
            print("   ✅ Train-Val overlap: None (no leakage)")
        else:
            print(f"   ❌ Train-Val overlap: {train_val_overlap} (DATA LEAKAGE!)")
        
        if not train_test_overlap:
            print("   ✅ Train-Test overlap: None (no leakage)")
        else:
            print(f"   ❌ Train-Test overlap: {train_test_overlap} (DATA LEAKAGE!)")
        
        if not val_test_overlap:
            print("   ✅ Val-Test overlap: None (no leakage)")
        else:
            print(f"   ❌ Val-Test overlap: {val_test_overlap} (DATA LEAKAGE!)")
        
        print()
        
        if not train_val_overlap and not train_test_overlap and not val_test_overlap:
            print("✅ VERIFIED: No data leakage detected")
            print("   ✅ Proper subject-level splits confirmed")
            print("   ✅ Test subjects are completely held-out")
        else:
            print("❌ ERROR: Data leakage detected!")
            print("   ⚠️  Subjects appear in multiple splits")
    else:
        print("⚠️  Results file not found. Cannot verify subject splits.")
        print()
        print("Expected split structure:")
        print("   - Train subjects: Never appear in test")
        print("   - Val subjects: Never appear in train or test")
        print("   - Test subjects: Completely held-out")
    
    print()
    print("="*70)

if __name__ == '__main__':
    verify_subject_splits()

