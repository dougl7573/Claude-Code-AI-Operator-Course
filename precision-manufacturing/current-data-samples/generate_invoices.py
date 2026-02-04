#!/usr/bin/env python3
"""
Generate realistic invoice PDFs for the course
Uses reportlab to create professional-looking invoices
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.enums import TA_RIGHT, TA_CENTER, TA_LEFT
from datetime import datetime
import os

# Base path for saving invoices
INVOICE_DIR = "/Users/tomcrawshaw/AI OPERATOR OS/Claude-Code-AI-Operator-Course/precision-manufacturing/current-data-samples/invoices/"

def create_invoice_1():
    """Invoice 1: Acme Corp - Clean, modern digital invoice"""
    filename = os.path.join(INVOICE_DIR, "invoice-001-acme-corp.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2C3E50'),
        spaceAfter=30,
    )

    header_style = ParagraphStyle(
        'HeaderRight',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_RIGHT,
    )

    # Company header
    story.append(Paragraph("<b>ACME CORP</b>", title_style))
    story.append(Paragraph("1234 Industrial Parkway<br/>Steel City, SC 29406<br/>Phone: (555) 123-4567<br/>Email: billing@acmecorp.com", header_style))
    story.append(Spacer(1, 0.3*inch))

    # Invoice title
    invoice_title = ParagraphStyle(
        'InvoiceTitle',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.HexColor('#E74C3C'),
    )
    story.append(Paragraph("<b>INVOICE</b>", invoice_title))
    story.append(Spacer(1, 0.2*inch))

    # Invoice details
    invoice_data = [
        ['Invoice Number:', 'INV-2024-0342', 'Invoice Date:', '01/15/2024'],
        ['Customer ID:', 'CUST-9876', 'Due Date:', '02/14/2024'],
        ['Payment Terms:', 'Net 30', '', ''],
    ]

    invoice_table = Table(invoice_data, colWidths=[1.5*inch, 2*inch, 1.5*inch, 1.5*inch])
    invoice_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#34495E')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(invoice_table)
    story.append(Spacer(1, 0.3*inch))

    # Bill To section
    story.append(Paragraph("<b>BILL TO:</b>", styles['Heading3']))
    story.append(Paragraph("Precision Manufacturing Ltd.<br/>5678 Factory Road<br/>Industrial Park, IP 12345", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))

    # Line items table
    line_items_data = [
        ['Description', 'Qty', 'Unit Price', 'Total'],
        ['Steel rods - Grade 304', '50', '$18.00', '$900.00'],
        ['Shipping & Handling', '1', '$250.00', '$250.00'],
    ]

    line_items_table = Table(line_items_data, colWidths=[3.5*inch, 0.8*inch, 1.2*inch, 1.2*inch])
    line_items_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495E')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ECF0F1')]),
    ]))
    story.append(line_items_table)
    story.append(Spacer(1, 0.3*inch))

    # Totals table
    totals_data = [
        ['', 'Subtotal:', '$1,150.00'],
        ['', 'Tax (8%):', '$92.00'],
        ['', 'TOTAL DUE:', '$1,242.00'],
    ]

    totals_table = Table(totals_data, colWidths=[4.3*inch, 1.2*inch, 1.2*inch])
    totals_table.setStyle(TableStyle([
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LINEABOVE', (1, 2), (-1, 2), 2, colors.black),
        ('FONTSIZE', (1, 2), (-1, 2), 12),
        ('TEXTCOLOR', (1, 2), (-1, 2), colors.HexColor('#E74C3C')),
    ]))
    story.append(totals_table)
    story.append(Spacer(1, 0.3*inch))

    # Notes
    story.append(Paragraph("<b>Notes:</b>", styles['Heading4']))
    story.append(Paragraph("Payment terms: Net 30<br/>Please reference invoice number on payment.<br/>Thank you for your business!", styles['Normal']))

    # Build PDF
    doc.build(story)
    print(f"Created: {filename}")

def create_invoice_2():
    """Invoice 2: Widget Supplies Inc - Standard business format"""
    filename = os.path.join(INVOICE_DIR, "invoice-002-widget-supplies.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Header with company name
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=22,
        textColor=colors.HexColor('#1F618D'),
        alignment=TA_CENTER,
        spaceAfter=10,
    )

    story.append(Paragraph("<b>Widget Supplies Inc.</b>", title_style))
    story.append(Paragraph("7890 Commerce Boulevard | Widget City, WC 54321<br/>Tel: (555) 789-0123 | Fax: (555) 789-0124<br/>www.widgetsupplies.com",
                          ParagraphStyle('Center', parent=styles['Normal'], alignment=TA_CENTER, fontSize=9)))
    story.append(Spacer(1, 0.2*inch))

    # Horizontal line
    from reportlab.platypus import HRFlowable
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1F618D')))
    story.append(Spacer(1, 0.2*inch))

    # Invoice header
    story.append(Paragraph("<b>INVOICE</b>", ParagraphStyle('InvTitle', parent=styles['Heading2'], fontSize=16, textColor=colors.HexColor('#1F618D'))))
    story.append(Spacer(1, 0.2*inch))

    # Two column layout for invoice details and bill to
    details_data = [
        ['<b>Invoice #:</b>', 'WS-789456', '<b>BILL TO:</b>'],
        ['<b>Date:</b>', '01/18/2024', 'Precision Manufacturing Ltd.'],
        ['<b>Due Date:</b>', '02/17/2024', '5678 Factory Road'],
        ['<b>Terms:</b>', 'Net 30', 'Industrial Park, IP 12345'],
    ]

    details_table = Table(details_data, colWidths=[1.2*inch, 1.8*inch, 3.5*inch])
    details_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('SPAN', (2, 0), (2, 0)),
        ('FONTNAME', (2, 0), (2, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (2, 0), (2, 0), 10),
    ]))
    story.append(details_table)
    story.append(Spacer(1, 0.3*inch))

    # Line items
    items_data = [
        ['Item', 'Description', 'Qty', 'Unit Price', 'Total'],
        ['1', 'Precision bearings (SKU: BR-2040)', '100', '$12.50', '$1,250.00'],
        ['2', 'Industrial fasteners - Set A', '25', '$79.62', '$1,990.50'],
    ]

    items_table = Table(items_data, colWidths=[0.5*inch, 3.3*inch, 0.7*inch, 1.1*inch, 1.1*inch])
    items_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F618D')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (2, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ALIGN', (0, 1), (0, -1), 'CENTER'),
    ]))
    story.append(items_table)
    story.append(Spacer(1, 0.2*inch))

    # Summary box
    summary_data = [
        ['Subtotal:', '$3,240.50'],
        ['Tax (8%):', '$259.24'],
        ['<b>AMOUNT DUE:</b>', '<b>$3,499.74</b>'],
    ]

    summary_table = Table(summary_data, colWidths=[5.4*inch, 1.3*inch])
    summary_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LINEABOVE', (0, 2), (-1, 2), 1.5, colors.black),
        ('FONTSIZE', (0, 2), (-1, 2), 11),
        ('TEXTCOLOR', (0, 2), (-1, 2), colors.HexColor('#1F618D')),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 0.3*inch))

    # Footer notes
    story.append(Paragraph("<b>Special Notes:</b>", styles['Heading4']))
    story.append(Paragraph("Bulk discount applied - 10%", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Make checks payable to: Widget Supplies Inc.<br/>Payment is due within 30 days. Past due accounts are subject to a 1.5% monthly finance charge.",
                          ParagraphStyle('Small', parent=styles['Normal'], fontSize=8, textColor=colors.grey)))

    doc.build(story)
    print(f"Created: {filename}")

def create_invoice_3():
    """Invoice 3: Tech Parts Direct - Different template style"""
    filename = os.path.join(INVOICE_DIR, "invoice-003-tech-parts-inc.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Side-by-side header
    header_data = [
        ['<b><font size=20 color="#C0392B">TECH PARTS DIRECT</font></b>', '<b><font size=16>INVOICE</font></b>'],
        ['<font size=8>2468 Technology Drive<br/>Circuit City, CC 13579<br/>Phone: (555) 246-8000<br/>support@techpartsdirect.com</font>',
         '<font size=9><b>Invoice #:</b> TP-2024-0891<br/><b>Date:</b> 01/20/2024<br/><b>Due:</b> 02/04/2024</font>'],
    ]

    header_table = Table(header_data, colWidths=[3.5*inch, 3.2*inch])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 0.3*inch))

    # Colored bar
    from reportlab.platypus import HRFlowable
    story.append(HRFlowable(width="100%", thickness=3, color=colors.HexColor('#C0392B')))
    story.append(Spacer(1, 0.2*inch))

    # Customer info box
    customer_data = [
        ['<b>CUSTOMER INFORMATION</b>'],
        ['<b>Bill To:</b><br/>Precision Manufacturing Ltd.<br/>5678 Factory Road<br/>Industrial Park, IP 12345'],
    ]

    customer_table = Table(customer_data, colWidths=[6.7*inch])
    customer_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#ECF0F1')),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.HexColor('#C0392B')),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, 0), 10),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#BDC3C7')),
    ]))
    story.append(customer_table)
    story.append(Spacer(1, 0.3*inch))

    # Order details
    story.append(Paragraph("<b>ORDER DETAILS</b>",
                          ParagraphStyle('SectionHeader', parent=styles['Heading3'],
                                       textColor=colors.HexColor('#C0392B'), fontSize=12)))
    story.append(Spacer(1, 0.1*inch))

    # Items table
    items_data = [
        ['Item #', 'Description', 'Quantity', 'Unit Price', 'Line Total'],
        ['1', 'Circuit boards - Custom order #45', '15', '$58.33', '$875.00'],
    ]

    items_table = Table(items_data, colWidths=[0.6*inch, 3.5*inch, 0.9*inch, 1*inch, 1*inch])
    items_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495E')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (2, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white]),
        ('PADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(items_table)
    story.append(Spacer(1, 0.3*inch))

    # Total section
    totals_data = [
        ['', '', 'Subtotal:', '$875.00'],
        ['', '', 'Sales Tax (8%):', '$70.00'],
        ['', '', '<b>TOTAL:</b>', '<b>$945.00</b>'],
    ]

    totals_table = Table(totals_data, colWidths=[0.6*inch, 3.5*inch, 1.5*inch, 1.1*inch])
    totals_table.setStyle(TableStyle([
        ('ALIGN', (2, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 1), 9),
        ('FONTSIZE', (0, 2), (-1, 2), 11),
        ('LINEABOVE', (2, 2), (-1, 2), 2, colors.HexColor('#C0392B')),
        ('TEXTCOLOR', (2, 2), (-1, 2), colors.HexColor('#C0392B')),
    ]))
    story.append(totals_table)
    story.append(Spacer(1, 0.3*inch))

    # Important notice box
    notice_data = [
        ['<b>IMPORTANT NOTICE</b>'],
        ['Express shipping - Due date is strict<br/>Payment must be received by due date to avoid project delays.'],
    ]

    notice_table = Table(notice_data, colWidths=[6.7*inch])
    notice_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#E74C3C')),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.white),
        ('BACKGROUND', (0, 1), (0, 1), colors.HexColor('#FADBD8')),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, 0), 10),
        ('FONTSIZE', (0, 1), (0, 1), 9),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#C0392B')),
    ]))
    story.append(notice_table)

    doc.build(story)
    print(f"Created: {filename}")

def create_invoice_4():
    """Invoice 4: Global Shipping - Simpler format"""
    filename = os.path.join(INVOICE_DIR, "invoice-004-global-shipping.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Simple header
    story.append(Paragraph("<b><font size=18>Global Shipping Solutions</font></b>",
                          ParagraphStyle('Title', parent=styles['Normal'], alignment=TA_CENTER)))
    story.append(Paragraph("<font size=9>9999 Port Avenue, Harbor City, HC 98765<br/>Tel: (555) 999-0000</font>",
                          ParagraphStyle('Center', parent=styles['Normal'], alignment=TA_CENTER, fontSize=9)))
    story.append(Spacer(1, 0.3*inch))

    story.append(Paragraph("<b>INVOICE</b>", ParagraphStyle('InvTitle', parent=styles['Heading2'], fontSize=14)))
    story.append(Spacer(1, 0.2*inch))

    # Basic details
    details = [
        ['Invoice Number:', 'GS-2024-1556'],
        ['Invoice Date:', '01/22/2024'],
        ['Due Date:', '02/21/2024'],
        ['', ''],
        ['<b>Bill To:</b>', ''],
        ['Precision Manufacturing Ltd.', ''],
        ['5678 Factory Road', ''],
        ['Industrial Park, IP 12345', ''],
    ]

    details_table = Table(details, colWidths=[2*inch, 4.5*inch])
    details_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 3), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(details_table)
    story.append(Spacer(1, 0.3*inch))

    # Simple items table
    items = [
        ['Description', 'Amount'],
        ['International freight - Container #45782', '$2,150.00'],
        ['Customs clearance fees', '$340.00'],
        ['Documentation processing', '$125.00'],
    ]

    items_table = Table(items, colWidths=[4.7*inch, 2*inch])
    items_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]))
    story.append(items_table)
    story.append(Spacer(1, 0.2*inch))

    # Totals
    totals = [
        ['Subtotal:', '$2,615.00'],
        ['Tax (8%):', '$209.20'],
        ['<b>Total Due:</b>', '<b>$2,824.20</b>'],
    ]

    totals_table = Table(totals, colWidths=[4.7*inch, 2*inch])
    totals_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LINEABOVE', (0, 2), (-1, 2), 1, colors.black),
    ]))
    story.append(totals_table)
    story.append(Spacer(1, 0.3*inch))

    story.append(Paragraph("Payment terms: Net 30 days", styles['Normal']))
    story.append(Paragraph("Please remit payment to address above or via wire transfer (details upon request).", styles['Normal']))

    doc.build(story)
    print(f"Created: {filename}")

def create_invoice_5():
    """Invoice 5: Office Depot - Multi-page with many line items"""
    filename = os.path.join(INVOICE_DIR, "invoice-005-office-depot.pdf")
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Header
    header_style = ParagraphStyle(
        'Header',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor('#D35400'),
        alignment=TA_CENTER,
    )

    story.append(Paragraph("<b>OFFICE DEPOT INDUSTRIAL SUPPLIES</b>", header_style))
    story.append(Paragraph("<font size=9>3333 Supply Chain Boulevard | Supplies City, SC 24680<br/>Phone: (555) 333-4444 | Fax: (555) 333-4445<br/>orders@officedepotind.com</font>",
                          ParagraphStyle('Center', parent=styles['Normal'], alignment=TA_CENTER, fontSize=9)))
    story.append(Spacer(1, 0.2*inch))

    from reportlab.platypus import HRFlowable
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#D35400')))
    story.append(Spacer(1, 0.2*inch))

    # Invoice info
    story.append(Paragraph("<b>INVOICE</b>", ParagraphStyle('InvTitle', parent=styles['Heading2'], fontSize=16, textColor=colors.HexColor('#D35400'))))
    story.append(Spacer(1, 0.15*inch))

    # Two-column details
    details_data = [
        ['<b>Invoice #:</b>', 'OD-2024-8823', '<b>Customer #:</b>', 'PM-54321'],
        ['<b>Invoice Date:</b>', '01/25/2024', '<b>P.O. Number:</b>', 'PO-2024-0156'],
        ['<b>Due Date:</b>', '02/24/2024', '<b>Sales Rep:</b>', 'Johnson, M.'],
        ['<b>Terms:</b>', 'Net 30', '<b>Ship Via:</b>', 'UPS Ground'],
    ]

    details_table = Table(details_data, colWidths=[1.3*inch, 1.9*inch, 1.3*inch, 1.9*inch])
    details_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(details_table)
    story.append(Spacer(1, 0.2*inch))

    # Bill To / Ship To
    address_data = [
        ['<b>BILL TO:</b>', '<b>SHIP TO:</b>'],
        ['Precision Manufacturing Ltd.', 'Precision Manufacturing Ltd.'],
        ['Accounts Payable Dept.', 'Receiving Dock B'],
        ['5678 Factory Road', '5678 Factory Road'],
        ['Industrial Park, IP 12345', 'Industrial Park, IP 12345'],
    ]

    address_table = Table(address_data, colWidths=[3.35*inch, 3.35*inch])
    address_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(address_table)
    story.append(Spacer(1, 0.3*inch))

    # Line items header
    items_data = [
        ['Item', 'SKU', 'Description', 'Qty', 'Unit Price', 'Total'],
    ]

    # Many line items
    line_items = [
        ['1', 'OFF-2045', 'Heavy-duty staplers', '24', '$12.99', '$311.76'],
        ['2', 'OFF-8821', 'Paper reams (20 lb, white)', '50', '$4.50', '$225.00'],
        ['3', 'OFF-3309', 'Ballpoint pens - Black (box of 12)', '30', '$8.75', '$262.50'],
        ['4', 'OFF-4456', 'File folders - Letter size', '100', '$0.45', '$45.00'],
        ['5', 'OFF-7782', 'Sticky notes - Yellow 3x3', '60', '$1.20', '$72.00'],
        ['6', 'OFF-5534', 'Binder clips - Assorted sizes', '40', '$3.50', '$140.00'],
        ['7', 'OFF-9921', 'Desk organizers - Metal mesh', '12', '$18.99', '$227.88'],
        ['8', 'OFF-1147', 'Paper clips - Standard (box)', '80', '$1.15', '$92.00'],
        ['9', 'OFF-6683', 'Highlighters - 4 color set', '35', '$5.99', '$209.65'],
        ['10', 'OFF-2290', 'Markers - Permanent black', '45', '$2.75', '$123.75'],
        ['11', 'OFF-8856', 'Rubber bands - Assorted', '25', '$2.25', '$56.25'],
        ['12', 'OFF-4423', 'Tape dispensers - Desktop', '18', '$7.50', '$135.00'],
        ['13', 'OFF-7709', 'Scissors - 8 inch', '22', '$6.25', '$137.50'],
        ['14', 'OFF-3381', 'Correction fluid - White', '40', '$2.99', '$119.60'],
        ['15', 'OFF-9934', 'Labels - Address (sheets)', '75', '$3.80', '$285.00'],
        ['16', 'OFF-5567', 'Envelopes - #10 Business', '120', '$0.85', '$102.00'],
        ['17', 'OFF-1198', 'Notebooks - College ruled', '55', '$4.25', '$233.75'],
        ['18', 'OFF-6625', 'Index cards - 3x5 (pack)', '48', '$2.15', '$103.20'],
        ['19', 'OFF-8837', 'Desk calendars - 2024', '15', '$9.99', '$149.85'],
        ['20', 'OFF-2214', 'Push pins - Assorted colors', '38', '$1.89', '$71.82'],
    ]

    items_data.extend(line_items)

    items_table = Table(items_data, colWidths=[0.35*inch, 0.9*inch, 2.7*inch, 0.5*inch, 1*inch, 1*inch])
    items_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#D35400')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (3, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#FEF5E7')]),
        ('PADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(items_table)
    story.append(Spacer(1, 0.2*inch))

    # Totals
    totals_data = [
        ['', '', '', '', 'Subtotal:', '$3,503.51'],
        ['', '', '', '', 'Shipping:', '$125.00'],
        ['', '', '', '', 'Tax (8%):', '$290.28'],
        ['', '', '', '', '<b>TOTAL DUE:</b>', '<b>$3,918.79</b>'],
    ]

    totals_table = Table(totals_data, colWidths=[0.35*inch, 0.9*inch, 2.7*inch, 0.5*inch, 1.1*inch, 1*inch])
    totals_table.setStyle(TableStyle([
        ('ALIGN', (4, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (4, 0), (4, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 2), 9),
        ('FONTSIZE', (0, 3), (-1, 3), 11),
        ('LINEABOVE', (4, 3), (-1, 3), 2, colors.HexColor('#D35400')),
        ('TEXTCOLOR', (4, 3), (-1, 3), colors.HexColor('#D35400')),
    ]))
    story.append(totals_table)
    story.append(Spacer(1, 0.3*inch))

    # Footer
    story.append(Paragraph("<b>Payment Instructions:</b>", styles['Heading4']))
    story.append(Paragraph("• Make checks payable to: Office Depot Industrial Supplies<br/>• Include invoice number on payment<br/>• Net 30 terms - late payments subject to 1.5% monthly finance charge<br/>• Questions? Contact billing@officedepotind.com or call (555) 333-4444",
                          ParagraphStyle('Small', parent=styles['Normal'], fontSize=8)))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<i>Thank you for your business!</i>",
                          ParagraphStyle('Italic', parent=styles['Normal'], fontSize=9, textColor=colors.grey, alignment=TA_CENTER)))

    doc.build(story)
    print(f"Created: {filename}")

def main():
    """Generate all invoices"""
    print("Generating realistic invoice PDFs...")
    print("=" * 60)

    create_invoice_1()
    create_invoice_2()
    create_invoice_3()
    create_invoice_4()
    create_invoice_5()

    print("=" * 60)
    print("All invoices generated successfully!")
    print(f"Location: {INVOICE_DIR}")

if __name__ == "__main__":
    main()
