# 🎯 Demo Guide - Medicine & Drug Interaction Advisor

## 🚀 Live Demo Examples

### 1. Mental Health Medication Queries

Try these queries in the General Query tab:

```
"What are the side effects of sertraline?"
"Side effects of alprazolam"
"What is fluoxetine used for?"
"Dosage for escitalopram"
"Mental health medications"
```

### 2. Indian Medicine Queries

```
"Side effects of Crocin"
"What is Pan 40 used for?"
"Combiflam side effects"
"Uses of Ecosprin"
```

### 3. Drug Interaction Checks

In the Drug Interaction tab, try these combinations:

**Dangerous Interactions:**
- Alprazolam + Alcohol
- Crocin + Combiflam (both contain paracetamol)
- Sertraline + Ibuprofen (bleeding risk)

**Safe Combinations:**
- Pan 40 + Ecosprin
- Metformin + Lisinopril
- Cetirizine + Montelukast

### 4. API Testing

```bash
# Get all mental health drugs
curl http://localhost:8000/mental-health-drugs

# Get specific drug details
curl http://localhost:8000/drug/sertraline

# Search by category
curl http://localhost:8000/search/antidepressant

# Check interaction
curl -X POST http://localhost:8000/check-interaction \
  -H "Content-Type: application/json" \
  -d '{"drug1": "alprazolam", "drug2": "lorazepam"}'
```

## 📊 Database Statistics

- **Total Drugs**: 45+
- **Mental Health Drugs**: 20+
- **Indian Brand Medicines**: 15+
- **Ayurvedic Medicines**: 3+
- **Drug Categories**: 15+

## 🎨 UI Features to Showcase

1. **Dark Theme** with animated background
2. **Voice Search** capability
3. **Pill Identifier** with visual selection
4. **My Medications List** with interaction checking
5. **Category-based browsing**
6. **A-Z Medicine Directory**

## 💡 Unique Selling Points

1. **Indian Medicine Focus**: Includes popular Indian brands
2. **Mental Health Emphasis**: Comprehensive psychotropic drug information
3. **Multi-Drug Interaction Checker**: Check all medications at once
4. **Price Information**: In Indian Rupees
5. **Prescription Status**: Know what needs a prescription
6. **Controlled Substance Warnings**: For regulated drugs

## 🔥 Quick Showcase Flow

1. **Start with Search**: Show voice search and instant results
2. **Demonstrate Drug Details**: Click on a drug to show comprehensive info
3. **Check Interactions**: Show both safe and dangerous combinations
4. **Browse by Condition**: Show mental health category
5. **Use Pill Identifier**: Demonstrate visual pill identification
6. **Show API**: Quick Postman/curl demo of endpoints