# EntropyScan

**A Python-based forensic tool to detect obfuscated or packed executables using Shannon Entropy analysis.**

In cybersecurity, high entropy is a strong indicator of hidden payloads. Malware authors often use packers or encryption to hide their code from antivirus scanners. This tool calculates the randomness of a file's byte distribution to flag suspicious binaries.

## Usage

```bash
python3 scanner.py <filename>
```
# Interpretation
*0.0 - 6.5: Likely standard code, text, or non-compressed data.
*6.5 - 7.2: Suspicious, possibly compressed.
*7.2 - 8.0: High Risk. Likely encrypted, packed, or obfuscated malware payload.
