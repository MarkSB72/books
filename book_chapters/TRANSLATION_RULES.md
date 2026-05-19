# Translation Rules for AUTOSAR Book

## Core Rules
1. Translate ALL descriptive text to natural Simplified Chinese. NO summarization, NO skipping.
2. Keep ALL technical abbreviations UNCHANGED: AUTOSAR, ECU, RTE, BSW, MCAL, SWC, COM, OS, CAN, LIN, FlexRay, Ethernet, SPI, I2C, MCU, CPU, RAM, ROM, EEPROM, API, ID, IP, MAC, TLS, AES, HSM, Crypto, DEM, DET, NVM, BSWM, ECUM, WDG, GPT, ICU, PWM, ADC, DIO, PORT, SoC, OEM, VFB, ARXML, XML, UML, PDU, SDU, PCI, ISR, FIFO, OSEK, RTOS, CDD, BMS, ADAS, EV, ECU, CAN, LIN, FR, ETH, TCP, UDP, HTTP, MQTT, ASW, ASIL, ISO, POSIX, SOA, V2X, E2E, ACC, ABS, ECM, TCM, BCM, ESC, HMI, IVI, MCAL, ECUM, CRC
3. Keep ALL code, XML, config, shell commands, file paths, URLs EXACTLY as-is
4. Translate headings naturally: "Chapter X" → "第X章", "Part X" → "第X部分", "Figure X.Y" → "图 X.Y", "Table X.Y" → "表 X.Y"
5. Keep page markers: === Page N === 
6. Keep company/product names in English
7. "Summary" → "本章小结", "Questions" → "思考题", "Note" → "注意", "Case study" → "案例研究"

## HTML Output Rules
- Use the CSS from Chapter 1 HTML as template (read ch01 HTML for reference style)
- Page markers become: <div class="page-marker">第 N 页</div>
- Figures: <div class="figure"><img src="images/FILENAME" alt="..."><p>图 X.Y – ...</p></div>
- Notes/注意: <div class="note">...</div>
- Case studies: <div class="case-study"><h3>案例研究 – ...</h3>...</div>
- Summary: <div class="summary"><h3>本章小结</h3>...</div>
- Questions: <div class="questions"><h3>思考题</h3>...</div>
- Code blocks: <pre><code>...</code></pre>
- Lists: proper <ul>/<ol> with <li>
