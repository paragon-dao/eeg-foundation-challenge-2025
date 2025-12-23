#!/usr/bin/env python3
"""
Verify Reported Results

This script verifies all reported results are consistent and correct.
"""

import json
from pathlib import Path
import numpy as np

def verify_results():
    """Verify all reported results"""
    print("="*70)
    print("RESULTS VERIFICATION")
    print("="*70)
    print()
    
    results_file = Path(__file__).parent.parent / "results" / "test_results.json"
    benchmark_file = Path(__file__).parent.parent / "results" / "benchmark_comparison.json"
    
    if not results_file.exists():
        print("❌ Results file not found!")
        return
    
    with open(results_file, 'r') as f:
        results = json.load(f)
    
    print("📊 Reported Results:")
    print(f"   Test Correlation: {results.get('correlation', 0)*100:.2f}%")
    print(f"   P-value: {results.get('p_value', 0):.2e}")
    print(f"   MSE: {results.get('mse', 0):.6f}")
    print(f"   RMSE: {results.get('rmse', 0):.6f}")
    print(f"   MAE: {results.get('mae', 0):.6f}")
    print(f"   Baseline MSE: {results.get('baseline_mse', 0):.6f}")
    print(f"   Normalized Error: {results.get('normalized_error', 0):.5f}")
    print()
    
    # Verify normalized error calculation
    mse = results.get('mse', 0)
    baseline_mse = results.get('baseline_mse', 0)
    reported_error = results.get('normalized_error', 0)
    calculated_error = mse / baseline_mse if baseline_mse > 0 else float('inf')
    
    print("🔍 Verification Checks:")
    print()
    
    # Check 1: Normalized error calculation
    if abs(calculated_error - reported_error) < 1e-5:
        print("   ✅ Normalized error calculation: Correct")
    else:
        print(f"   ❌ Normalized error calculation: Mismatch!")
        print(f"      Reported: {reported_error:.5f}")
        print(f"      Calculated: {calculated_error:.5f}")
    
    # Check 2: RMSE calculation
    rmse_reported = results.get('rmse', 0)
    rmse_calculated = np.sqrt(mse)
    if abs(rmse_calculated - rmse_reported) < 1e-5:
        print("   ✅ RMSE calculation: Correct")
    else:
        print(f"   ❌ RMSE calculation: Mismatch!")
    
    # Check 3: Statistical significance
    p_value = results.get('p_value', 1.0)
    if p_value < 0.001:
        print("   ✅ Statistical significance: Highly significant (p < 0.001)")
    elif p_value < 0.05:
        print("   ✅ Statistical significance: Significant (p < 0.05)")
    else:
        print(f"   ⚠️  Statistical significance: Not significant (p = {p_value:.4f})")
    
    # Check 4: Competition comparison
    if benchmark_file.exists():
        with open(benchmark_file, 'r') as f:
            benchmarks = json.load(f)
        
        our_score = results.get('normalized_error', 1.0)
        winner_score = benchmarks.get('winner_score', 1.0)
        
        print()
        print("📊 Competition Comparison:")
        print(f"   Our Score: {our_score:.5f}")
        print(f"   Previous Winner: {winner_score:.5f}")
        
        if our_score < winner_score:
            improvement = (winner_score - our_score) / winner_score * 100
            print(f"   ✅ We beat the winner by {improvement:.2f}%")
        else:
            gap = our_score - winner_score
            print(f"   ⚠️  Gap from winner: {gap:.5f}")
    
    print()
    print("="*70)
    print("✅ VERIFICATION COMPLETE")

if __name__ == '__main__':
    verify_results()

