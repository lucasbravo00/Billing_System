# Restaurant Billing System

A comprehensive restaurant billing and management system developed in Python using Tkinter for the graphical user interface.

## Overview

This application provides a complete solution for restaurant order management and billing. It allows staff to select food items, drinks, and desserts; calculate costs (including configurable tax rates); and generate detailed receipts that can be saved for record-keeping.

## Features

- **Product Selection:** Checkboxes for choosing food items, drinks, and desserts
- **Quantity Management:** Input fields for specifying quantities
- **Automatic Calculations:** Real-time subtotal, tax, and total calculations
- **Receipt Generation:** Detailed receipt with order breakdown and timestamp
- **Receipt Storage:** Save receipts as plain-text files
- **Built-in Calculator:** Quick calculator for additional needs
- **Reset Function:** Clear all inputs with a single click
- **User-friendly Interface:** Clean, intuitive layout

## Technical Details

- **Language:** Python 3.x
- **GUI Framework:** Tkinter
- **Dependencies:**
  - `random` (receipt numbers)
  - `datetime` (timestamps)
- **Tax Rate:** Configurable (default 21%)
- **Product Database:** Easily customizable lists of items and prices

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lucasbravo00/Billing_system.git
   cd Billing_system
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   ```

## Running the Application

From the project's root directory, run:
```bash
python Billing_System.py
```
The graphical interface will launch immediately—no additional arguments required.

## How to Use

1. **Select Products:** Tick the boxes next to desired items
2. **Enter Quantities:** Specify quantity for each selection
3. **Calculate Total:** Click Total to compute costs
4. **Generate Receipt:** Click Receipt to view order summary
5. **Save Receipt:** Click Save to write receipt to a text file
6. **Reset:** Click Reset to clear all inputs

## System Requirements

- Python 3.6+
- Tkinter (bundled with Python)
- Minimal CPU/memory — runs on virtually any desktop or laptop

## Customization

- Modify product lists and prices in the source
- Adjust tax rate via the TAX_RATE constant
- Change receipt formatting in the receipt generation function
- Update UI labels, fonts, and colors in Tkinter widget definitions

## Future Enhancements

- Database integration for dynamic menu management
- User authentication with role-based access
- Sales reporting dashboard
- Inventory tracking
- Table and reservation management
- Payment gateway integration

## License

Feel free to use, modify, and distribute this code for personal or educational purposes.
