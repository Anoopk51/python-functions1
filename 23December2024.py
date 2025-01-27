from fpdf import FPDF

# Create a PDF instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", style="B", size=14)
pdf.cell(0, 10, "Safety Conditions at Daims", ln=True, align="C")
pdf.ln(10)

# Content
pdf.set_font("Arial", size=12)
content = """
1. Workplace Safety
   - Personal Protective Equipment (PPE): Employees must wear appropriate PPE like helmets, gloves, safety shoes, and eye protection in production areas.
   - Safe Machinery Operation: Ensure all machinery is regularly inspected, maintained, and operated by trained personnel.
   - Emergency Stops: All equipment should have easily accessible emergency stop mechanisms.
   - Proper Training: Employees should be well-trained in handling equipment, identifying hazards, and following safety protocols.

2. Fire and Emergency Preparedness
   - Fire Alarms and Extinguishers: Regularly test fire alarms and ensure fire extinguishers are available and accessible.
   - Emergency Exits: Mark and keep exits unobstructed at all times.
   - Evacuation Plans: Post clear evacuation maps and conduct regular drills.
   - Fire Suppression Systems: Install automatic systems in high-risk areas.

3. Chemical and Environmental Safety
   - Chemical Handling: Store and use chemicals according to safety data sheets (SDS). Provide spill kits and ensure proper ventilation.
   - Waste Disposal: Follow environmental regulations for disposing of hazardous and non-hazardous waste.
   - Air Quality Control: Monitor and control emissions to maintain air quality in compliance with safety standards.

4. Health and Ergonomics
   - Ergonomic Workstations: Design workstations to reduce strain and prevent repetitive motion injuries.
   - Regular Health Checks: Offer periodic health screenings for employees.
   - Hygiene Standards: Ensure availability of clean drinking water and sanitation facilities.

5. Digital and Cyber Safety
   - Data Protection: Implement robust cybersecurity measures to protect sensitive information.
   - System Backups: Regularly back up important data to avoid loss due to system failures.

6. Transport and Logistics
   - Vehicle Maintenance: Regularly inspect and maintain company vehicles.
   - Driver Safety Training: Train drivers on road safety and compliance with traffic laws.
   - Safe Loading Practices: Follow guidelines for securing loads during transport.

7. Continuous Monitoring and Reporting
   - Incident Reporting: Establish a clear protocol for reporting and analyzing workplace incidents.
   - Audits and Inspections: Conduct routine safety audits and inspections to identify and mitigate risks.
   - Feedback Mechanisms: Encourage employees to report unsafe conditions or suggest safety improvements.
"""

pdf.multi_cell(0, 10, content)

# Save the PDF
file_path = "/mnt/data/Safety_Conditions_at_Daims.pdf"
pdf.output(file_path)

file_path
