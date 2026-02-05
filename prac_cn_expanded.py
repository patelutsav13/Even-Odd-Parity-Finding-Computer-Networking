# ============================================================
# CN PROJECT: Parity Finding Using Python
# Concept: Error Detection using Even and Odd Parity
# ============================================================

import matplotlib.pyplot as plt
from typing import Tuple

# ============================================================
# INPUT VALIDATION
# ============================================================

def validate_binary_input(data: str) -> Tuple[bool, str]:
    """Validates binary input."""
    if not data or data.strip() == "":
        return False, "Error: Input cannot be empty!"
    data = data.strip()
    for char in data:
        if char not in ('0', '1'):
            return False, f"Error: Invalid character '{char}'! Only 0 and 1 allowed."
    if len(data) < 4:
        return False, "Error: Binary data must be at least 4 bits long!"
    if len(data) > 32:
        return False, "Error: Binary data cannot exceed 32 bits!"
    return True, "Valid"

def get_binary_input() -> str:
    """Gets validated binary input from user."""
    while True:
        data = input("\n📥 Enter Binary Data (4-32 bits): ").strip()
        is_valid, message = validate_binary_input(data)
        if is_valid:
            return data
        else:
            print(f"❌ {message}\n")

def validate_integer_input(prompt: str, min_val: int, max_val: int) -> int:
    """Validates integer input with range checking."""
    while True:
        try:
            user_input = input(prompt)
            if not user_input or user_input.strip() == "":
                print(f"❌ Error: Input cannot be empty! Enter number between {min_val} and {max_val}.")
                continue
            value = int(user_input.strip())
            if value < min_val or value > max_val:
                print(f"❌ Error: Enter a number between {min_val} and {max_val}.")
                continue
            return value
        except ValueError:
            print(f"❌ Error: Invalid input! Enter an integer only.")

# ============================================================
# 1. EVEN PARITY
# ============================================================

def generate_even_parity(data: str) -> Tuple[int, dict]:
    """Generates even parity bit."""
    ones_count = data.count('1')
    zeros_count = len(data) - ones_count
    parity_bit = 0 if ones_count % 2 == 0 else 1
    
    details = {
        'data': data,
        'ones_count': ones_count,
        'zeros_count': zeros_count,
        'parity_bit': parity_bit,
        'explanation': f"Count of 1's = {ones_count} ({'EVEN' if ones_count % 2 == 0 else 'ODD'}) → Parity bit = {parity_bit} (to keep total even)"
    }
    return parity_bit, details

def display_even_parity(details: dict):
    """Displays even parity calculation."""
    print("\n" + "="*60)
    print("  1. EVEN PARITY CALCULATION")
    print("="*60)
    print(f"\n📊 Original Data: {details['data']}")
    print(f"   Length: {len(details['data'])} bits")
    print(f"   Count of 0's: {details['zeros_count']}")
    print(f"   Count of 1's: {details['ones_count']}")
    print(f"\n✅ {details['explanation']}")
    print(f"🎯 Generated Parity Bit: {details['parity_bit']}")
    print(f"📡 Transmitted Data: {details['data']}{details['parity_bit']}")

# ============================================================
# 2. ODD PARITY
# ============================================================

def generate_odd_parity(data: str) -> Tuple[int, dict]:
    """Generates odd parity bit."""
    ones_count = data.count('1')
    zeros_count = len(data) - ones_count
    parity_bit = 1 if ones_count % 2 == 0 else 0
    
    details = {
        'data': data,
        'ones_count': ones_count,
        'zeros_count': zeros_count,
        'parity_bit': parity_bit,
        'explanation': f"Count of 1's = {ones_count} ({'EVEN' if ones_count % 2 == 0 else 'ODD'}) → Parity bit = {parity_bit} (to make total odd)"
    }
    return parity_bit, details

def display_odd_parity(details: dict):
    """Displays odd parity calculation."""
    print("\n" + "="*60)
    print("  2. ODD PARITY CALCULATION")
    print("="*60)
    print(f"\n📊 Original Data: {details['data']}")
    print(f"   Length: {len(details['data'])} bits")
    print(f"   Count of 0's: {details['zeros_count']}")
    print(f"   Count of 1's: {details['ones_count']}")
    print(f"\n✅ {details['explanation']}")
    print(f"🎯 Generated Parity Bit: {details['parity_bit']}")
    print(f"📡 Transmitted Data: {details['data']}{details['parity_bit']}")

# ============================================================
# 3. EVEN PARITY GRAPH
# ============================================================

def create_even_parity_graph(data: str, parity_bit: int, details: dict):
    """Creates single visualization for even parity."""
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.suptitle('EVEN PARITY VISUALIZATION', fontsize=14, fontweight='bold')
    
    # Single Graph: Data with Parity Bit
    data_with_parity = data + str(parity_bit)
    data_parity_array = [int(bit) for bit in data_with_parity]
    positions_parity = list(range(len(data_with_parity)))
    colors_parity = ['#FF6B6B' if bit == 0 else '#4ECDC4' for bit in data_parity_array]
    colors_parity[-1] = '#FFD93D'  # Highlight parity bit in yellow
    
    bars = ax.bar(positions_parity, data_parity_array, color=colors_parity, 
                  edgecolor='black', linewidth=2)
    ax.set_xlabel('Bit Position', fontsize=12, fontweight='bold')
    ax.set_ylabel('Bit Value', fontsize=12, fontweight='bold')
    ax.set_title(f'Data: {data} | Parity Bit: {parity_bit} | Transmitted: {data_with_parity}', 
                fontsize=11, fontweight='bold')
    ax.set_yticks([0, 1])
    ax.grid(axis='y', alpha=0.3)
    
    # Add text annotation
    ax.text(0.5, -0.3, f"0's: {details['zeros_count']} | 1's: {details['ones_count']} | Parity: {parity_bit} (Yellow)", 
           transform=ax.transAxes, ha='center', fontsize=11, 
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.show()

# ============================================================
# 4. ODD PARITY GRAPH
# ============================================================

def create_odd_parity_graph(data: str, parity_bit: int, details: dict):
    """Creates single visualization for odd parity."""
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.suptitle('ODD PARITY VISUALIZATION', fontsize=14, fontweight='bold')
    
    # Single Graph: Data with Parity Bit
    data_with_parity = data + str(parity_bit)
    data_parity_array = [int(bit) for bit in data_with_parity]
    positions_parity = list(range(len(data_with_parity)))
    colors_parity = ['#FF6B6B' if bit == 0 else '#4ECDC4' for bit in data_parity_array]
    colors_parity[-1] = '#FFD93D'  # Highlight parity bit in yellow
    
    bars = ax.bar(positions_parity, data_parity_array, color=colors_parity, 
                  edgecolor='black', linewidth=2)
    ax.set_xlabel('Bit Position', fontsize=12, fontweight='bold')
    ax.set_ylabel('Bit Value', fontsize=12, fontweight='bold')
    ax.set_title(f'Data: {data} | Parity Bit: {parity_bit} | Transmitted: {data_with_parity}', 
                fontsize=11, fontweight='bold')
    ax.set_yticks([0, 1])
    ax.grid(axis='y', alpha=0.3)
    
    # Add text annotation
    ax.text(0.5, -0.3, f"0's: {details['zeros_count']} | 1's: {details['ones_count']} | Parity: {parity_bit} (Yellow)", 
           transform=ax.transAxes, ha='center', fontsize=11, 
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.show()

# ============================================================
# MENU SYSTEM
# ============================================================

def display_menu():
    """Displays menu options."""
    print("\n" + "="*60)
    print("  MENU OPTIONS")
    print("="*60)
    print("   1. EVEN PARITY")
    print("   2. ODD PARITY")
    print("   3. EVEN PARITY GRAPH")
    print("   4. ODD PARITY GRAPH")
    print("   5. EXIT")
    print("="*60)

# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    """Main program entry point."""
    print("\n" + "="*60)
    print("  CN PROJECT: PARITY FINDING SYSTEM")
    print("="*60)
    
    # Get binary data once
    data = get_binary_input()
    
    # Pre-calculate both parities
    even_parity_bit, even_details = generate_even_parity(data)
    odd_parity_bit, odd_details = generate_odd_parity(data)
    
    # Menu loop
    while True:
        display_menu()
        choice = validate_integer_input("\n👉 Enter your choice (1-5): ", 1, 5)
        
        if choice == 1:
            # 1. EVEN PARITY
            display_even_parity(even_details)
        
        elif choice == 2:
            # 2. ODD PARITY
            display_odd_parity(odd_details)
        
        elif choice == 3:
            # 3. EVEN PARITY GRAPH
            print("\n📈 Generating Even Parity Graph...")
            create_even_parity_graph(data, even_parity_bit, even_details)
        
        elif choice == 4:
            # 4. ODD PARITY GRAPH
            print("\n📈 Generating Odd Parity Graph...")
            create_odd_parity_graph(data, odd_parity_bit, odd_details)
        
        elif choice == 5:
            # 5. EXIT
            print("\n" + "="*60)
            print("  ✅ THANK YOU! PROGRAM EXITED SUCCESSFULLY!")
            print("="*60 + "\n")
            break

# ============================================================
# PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":
    main()
