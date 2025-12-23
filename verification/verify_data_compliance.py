#!/usr/bin/env python3
"""
Verify Data Compliance with Competition Requirements

This script verifies that our data processing meets competition requirements:
- Sampling rate: 100 Hz
- Window size: 2 seconds (200 timepoints at 100 Hz)
- Channels: 4 channels (Muse device standard)
"""

import torch
import json
from pathlib import Path

def verify_data_compliance():
    """Verify data format compliance"""
    print("="*70)
    print("DATA COMPLIANCE VERIFICATION")
    print("="*70)
    print()
    
    requirements = {
        'sampling_rate': 100.0,  # Hz
        'window_size_sec': 2.0,  # seconds
        'timepoints': 200,  # 2 seconds × 100 Hz
        'channels': 4  # Muse device
    }
    
    print("📊 Competition Requirements:")
    for key, value in requirements.items():
        print(f"   {key}: {value}")
    print()
    
    # Check if we can verify from results
    results_file = Path(__file__).parent.parent / "results" / "test_results.json"
    if results_file.exists():
        with open(results_file, 'r') as f:
            results = json.load(f)
        
        metadata = results.get('metadata', {})
        
        print("📊 Our Data Format:")
        print(f"   Sampling Rate: {metadata.get('sampling_rate', 'N/A')} Hz")
        print(f"   Window Size: {metadata.get('window_size_sec', 'N/A')} seconds")
        print(f"   Timepoints: {metadata.get('n_times', 'N/A')}")
        print(f"   Channels: {metadata.get('n_channels', 'N/A')}")
        print()
        
        # Verify compliance
        checks = {
            'Sampling Rate (100 Hz)': metadata.get('sampling_rate', 0) == 100.0,
            'Window Size (2 seconds)': metadata.get('window_size_sec', 0) == 2.0,
            'Timepoints (200)': metadata.get('n_times', 0) == 200,
            'Channels (4)': metadata.get('n_channels', 0) == 4
        }
        
        print("✅ Compliance Checks:")
        all_passed = True
        for check_name, passed in checks.items():
            status = "✅" if passed else "❌"
            print(f"   {status} {check_name}")
            if not passed:
                all_passed = False
        
        if all_passed:
            print()
            print("✅ ALL CHECKS PASSED: Data format meets competition requirements")
        else:
            print()
            print("❌ SOME CHECKS FAILED: Please verify data processing")
    else:
        print("⚠️  Results file not found. Cannot verify data format.")
        print("   Expected format:")
        print(f"   - Sampling Rate: {requirements['sampling_rate']} Hz")
        print(f"   - Window Size: {requirements['window_size_sec']} seconds")
        print(f"   - Timepoints: {requirements['timepoints']}")
        print(f"   - Channels: {requirements['channels']}")
    
    print()
    print("="*70)

if __name__ == '__main__':
    verify_data_compliance()

