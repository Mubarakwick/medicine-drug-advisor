# Comprehensive Drug Database with Mental Health Medications

COMPREHENSIVE_DRUG_DATABASE = {
    # PSYCHOTROPIC/MENTAL HEALTH DRUGS
    "alprazolam": {
        "brand_names": ["Xanax", "Alprax", "Restyl", "Trika"],
        "generic_name": "Alprazolam",
        "category": "Benzodiazepine (Anti-anxiety)",
        "uses": "Anxiety disorders, panic disorders, anxiety associated with depression",
        "side_effects": "Drowsiness, dizziness, increased saliva production, change in sex drive/ability, memory problems, dependence risk",
        "dosage": "0.25-0.5mg 2-3 times daily for anxiety. Maximum 4mg/day",
        "warnings": "Highly addictive, can cause dependence. Do not stop suddenly. Avoid alcohol. Risk of withdrawal symptoms",
        "interactions": ["Opioids", "Other benzodiazepines", "Alcohol", "CNS depressants"],
        "price_range": "₹20-50 per strip",
        "prescription_required": True,
        "controlled_substance": True
    },
    
    "sertraline": {
        "brand_names": ["Zoloft", "Serta", "Serlift", "Serenata"],
        "generic_name": "Sertraline",
        "category": "SSRI Antidepressant",
        "uses": "Depression, OCD, panic disorder, PTSD, social anxiety disorder, premenstrual dysphoric disorder",
        "side_effects": "Nausea, dizziness, dry mouth, loss of appetite, increased sweating, diarrhea, sexual dysfunction",
        "dosage": "Starting: 50mg once daily. May increase to 50-200mg/day",
        "warnings": "May increase suicidal thoughts in young adults. Takes 4-6 weeks for full effect. Do not stop suddenly",
        "interactions": ["MAOIs", "Blood thinners", "NSAIDs", "Other SSRIs"],
        "price_range": "₹50-150 per strip",
        "prescription_required": True
    },
    
    "fluoxetine": {
        "brand_names": ["Prozac", "Fludac", "Flunil", "Flutine"],
        "generic_name": "Fluoxetine",
        "category": "SSRI Antidepressant",
        "uses": "Major depressive disorder, OCD, bulimia nervosa, panic disorder",
        "side_effects": "Nausea, headache, insomnia, anxiety, drowsiness, loss of appetite, sexual dysfunction",
        "dosage": "20mg once daily in morning. May increase to 20-80mg/day",
        "warnings": "Black box warning for suicidal thoughts. Long half-life. May cause activation/agitation initially",
        "interactions": ["MAOIs", "Thioridazine", "Pimozide", "Blood thinners"],
        "price_range": "₹30-100 per strip",
        "prescription_required": True
    },
    
    "escitalopram": {
        "brand_names": ["Lexapro", "Cipralex", "Nexito", "Stalopam"],
        "generic_name": "Escitalopram",
        "category": "SSRI Antidepressant",
        "uses": "Depression, generalized anxiety disorder",
        "side_effects": "Nausea, insomnia, ejaculation disorder, fatigue, decreased libido, anorgasmia",
        "dosage": "10mg once daily. May increase to 20mg/day",
        "warnings": "Risk of QT prolongation at higher doses. Gradual discontinuation required",
        "interactions": ["MAOIs", "Pimozide", "NSAIDs", "Antiplatelet drugs"],
        "price_range": "₹60-200 per strip",
        "prescription_required": True
    },
    
    "clonazepam": {
        "brand_names": ["Klonopin", "Rivotril", "Clonotril", "Zapiz"],
        "generic_name": "Clonazepam",
        "category": "Benzodiazepine (Anticonvulsant/Anti-anxiety)",
        "uses": "Seizure disorders, panic disorder, anxiety",
        "side_effects": "Drowsiness, dizziness, fatigue, memory impairment, depression, coordination problems",
        "dosage": "0.5mg twice daily. Maximum 20mg/day for seizures, 4mg/day for panic",
        "warnings": "Risk of dependence. Can cause respiratory depression. Avoid sudden discontinuation",
        "interactions": ["Opioids", "Alcohol", "Other CNS depressants", "Phenytoin"],
        "price_range": "₹30-80 per strip",
        "prescription_required": True,
        "controlled_substance": True
    },
    
    "lorazepam": {
        "brand_names": ["Ativan", "Larpose", "Trapex", "Calmese"],
        "generic_name": "Lorazepam",
        "category": "Benzodiazepine (Anti-anxiety)",
        "uses": "Anxiety disorders, insomnia due to anxiety, pre-surgery sedation",
        "side_effects": "Sedation, dizziness, weakness, unsteadiness, cognitive impairment",
        "dosage": "2-3mg/day in divided doses for anxiety. 2-4mg at bedtime for insomnia",
        "warnings": "High potential for abuse and dependence. Use lowest effective dose for shortest duration",
        "interactions": ["Opioids", "Alcohol", "Barbiturates", "Antipsychotics"],
        "price_range": "₹40-100 per strip",
        "prescription_required": True,
        "controlled_substance": True
    },
    
    "quetiapine": {
        "brand_names": ["Seroquel", "Qutipin", "Qutan", "Quetirol"],
        "generic_name": "Quetiapine",
        "category": "Atypical Antipsychotic",
        "uses": "Schizophrenia, bipolar disorder, major depressive disorder (adjunct)",
        "side_effects": "Drowsiness, dizziness, dry mouth, constipation, weight gain, increased cholesterol",
        "dosage": "Schizophrenia: 300-800mg/day. Bipolar: 400-800mg/day. Depression: 150-300mg/day",
        "warnings": "Risk of metabolic syndrome, tardive dyskinesia. Monitor blood sugar and lipids",
        "interactions": ["CYP3A4 inhibitors", "Antihypertensives", "CNS depressants"],
        "price_range": "₹50-300 per strip",
        "prescription_required": True
    },
    
    "olanzapine": {
        "brand_names": ["Zyprexa", "Oliza", "Olanex", "Oleanz"],
        "generic_name": "Olanzapine",
        "category": "Atypical Antipsychotic",
        "uses": "Schizophrenia, bipolar disorder, treatment-resistant depression",
        "side_effects": "Weight gain, drowsiness, dizziness, restlessness, constipation, dry mouth",
        "dosage": "5-20mg once daily. Start with 5-10mg",
        "warnings": "High risk of weight gain and metabolic effects. Monitor glucose and lipids regularly",
        "interactions": ["Fluvoxamine", "Carbamazepine", "Alcohol", "Antihypertensives"],
        "price_range": "₹80-400 per strip",
        "prescription_required": True
    },
    
    "risperidone": {
        "brand_names": ["Risperdal", "Sizodon", "Respidon", "Risdone"],
        "generic_name": "Risperidone",
        "category": "Atypical Antipsychotic",
        "uses": "Schizophrenia, bipolar mania, irritability in autism",
        "side_effects": "Weight gain, drowsiness, dizziness, nausea, vomiting, extrapyramidal symptoms",
        "dosage": "2-6mg/day for schizophrenia. Start with 2mg/day",
        "warnings": "Risk of stroke in elderly with dementia. May cause hyperprolactinemia",
        "interactions": ["Carbamazepine", "Fluoxetine", "Paroxetine", "Antihypertensives"],
        "price_range": "₹30-200 per strip",
        "prescription_required": True
    },
    
    "aripiprazole": {
        "brand_names": ["Abilify", "Arip", "Asprito", "Aripra"],
        "generic_name": "Aripiprazole",
        "category": "Atypical Antipsychotic",
        "uses": "Schizophrenia, bipolar disorder, major depression (adjunct), irritability in autism",
        "side_effects": "Headache, anxiety, insomnia, nausea, vomiting, restlessness",
        "dosage": "10-15mg once daily. Maximum 30mg/day",
        "warnings": "May cause compulsive behaviors (gambling, shopping). Monitor for suicidal thoughts",
        "interactions": ["CYP3A4 inhibitors", "CYP2D6 inhibitors", "Antihypertensives"],
        "price_range": "₹100-500 per strip",
        "prescription_required": True
    },
    
    "lithium": {
        "brand_names": ["Lithosun", "Licab", "Lithium Carbonate"],
        "generic_name": "Lithium Carbonate",
        "category": "Mood Stabilizer",
        "uses": "Bipolar disorder (manic episodes), maintenance therapy for bipolar",
        "side_effects": "Tremor, increased thirst/urination, weight gain, cognitive dulling, hypothyroidism",
        "dosage": "300mg 2-3 times daily. Adjust based on blood levels (0.6-1.2 mEq/L)",
        "warnings": "Narrow therapeutic index. Regular blood level monitoring required. Risk of toxicity",
        "interactions": ["NSAIDs", "ACE inhibitors", "Diuretics", "Antipsychotics"],
        "price_range": "₹50-150 per strip",
        "prescription_required": True
    },
    
    "valproate": {
        "brand_names": ["Depakote", "Valprol", "Encorate", "Valparin"],
        "generic_name": "Sodium Valproate/Valproic Acid",
        "category": "Mood Stabilizer/Anticonvulsant",
        "uses": "Epilepsy, bipolar disorder (manic episodes), migraine prevention",
        "side_effects": "Nausea, vomiting, hair loss, weight gain, tremor, liver dysfunction",
        "dosage": "Starting: 250mg twice daily. Maintenance: 1000-2000mg/day",
        "warnings": "Risk of hepatotoxicity, pancreatitis. Highly teratogenic - avoid in pregnancy",
        "interactions": ["Lamotrigine", "Carbamazepine", "Aspirin", "Carbapenem antibiotics"],
        "price_range": "₹40-200 per strip",
        "prescription_required": True
    },
    
    "carbamazepine": {
        "brand_names": ["Tegretol", "Mazetol", "Tegrital", "Zen"],
        "generic_name": "Carbamazepine",
        "category": "Anticonvulsant/Mood Stabilizer",
        "uses": "Epilepsy, trigeminal neuralgia, bipolar disorder",
        "side_effects": "Dizziness, drowsiness, nausea, vomiting, ataxia, blood disorders",
        "dosage": "Starting: 200mg twice daily. Maintenance: 800-1200mg/day",
        "warnings": "Risk of Stevens-Johnson syndrome. Regular blood monitoring required",
        "interactions": ["Many drug interactions - induces liver enzymes", "Oral contraceptives", "Warfarin"],
        "price_range": "₹30-150 per strip",
        "prescription_required": True
    },
    
    "bupropion": {
        "brand_names": ["Wellbutrin", "Bupron", "Nicotex"],
        "generic_name": "Bupropion",
        "category": "Atypical Antidepressant",
        "uses": "Depression, seasonal affective disorder, smoking cessation",
        "side_effects": "Dry mouth, nausea, dizziness, excessive sweating, tremor, insomnia",
        "dosage": "Starting: 150mg once daily. May increase to 300-450mg/day",
        "warnings": "Lowers seizure threshold. Avoid in eating disorders. May increase blood pressure",
        "interactions": ["MAOIs", "Drugs that lower seizure threshold", "CYP2B6 inhibitors"],
        "price_range": "₹80-300 per strip",
        "prescription_required": True
    },
    
    "mirtazapine": {
        "brand_names": ["Remeron", "Mirnite", "Mirtaz"],
        "generic_name": "Mirtazapine",
        "category": "Atypical Antidepressant",
        "uses": "Major depressive disorder",
        "side_effects": "Increased appetite, weight gain, drowsiness, dizziness, dry mouth",
        "dosage": "Starting: 15mg at bedtime. May increase to 15-45mg/day",
        "warnings": "May cause significant weight gain. Risk of agranulocytosis",
        "interactions": ["MAOIs", "CNS depressants", "CYP3A4 inhibitors"],
        "price_range": "₹60-250 per strip",
        "prescription_required": True
    },
    
    "venlafaxine": {
        "brand_names": ["Effexor", "Veniz", "Venlor", "Venfax"],
        "generic_name": "Venlafaxine",
        "category": "SNRI Antidepressant",
        "uses": "Depression, generalized anxiety disorder, panic disorder, social anxiety disorder",
        "side_effects": "Nausea, dizziness, insomnia, nervousness, sexual dysfunction, increased blood pressure",
        "dosage": "Starting: 75mg/day. May increase to 75-375mg/day",
        "warnings": "May increase blood pressure. Risk of withdrawal symptoms. Monitor suicidal thoughts",
        "interactions": ["MAOIs", "SSRIs", "Triptans", "NSAIDs"],
        "price_range": "₹50-300 per strip",
        "prescription_required": True
    },
    
    "duloxetine": {
        "brand_names": ["Cymbalta", "Duvanta", "Duzela"],
        "generic_name": "Duloxetine",
        "category": "SNRI Antidepressant",
        "uses": "Depression, generalized anxiety disorder, diabetic neuropathy, fibromyalgia",
        "side_effects": "Nausea, dry mouth, constipation, decreased appetite, fatigue, drowsiness",
        "dosage": "Starting: 30-60mg once daily. Maximum 120mg/day",
        "warnings": "Risk of liver damage. Monitor blood pressure. Gradual discontinuation required",
        "interactions": ["MAOIs", "Thioridazine", "CYP1A2 inhibitors", "CYP2D6 inhibitors"],
        "price_range": "₹80-400 per strip",
        "prescription_required": True
    },
    
    "modafinil": {
        "brand_names": ["Provigil", "Modalert", "Modvigil", "Vilafinil"],
        "generic_name": "Modafinil",
        "category": "Wakefulness Promoting Agent",
        "uses": "Narcolepsy, shift work sleep disorder, excessive daytime sleepiness",
        "side_effects": "Headache, nausea, nervousness, dizziness, difficulty sleeping",
        "dosage": "200mg once daily in morning. Maximum 400mg/day",
        "warnings": "Risk of severe skin reactions. May be habit-forming. Can reduce effectiveness of birth control",
        "interactions": ["CYP3A4 inducers/inhibitors", "Oral contraceptives", "Cyclosporine"],
        "price_range": "₹100-500 per strip",
        "prescription_required": True,
        "controlled_substance": True
    },
    
    "methylphenidate": {
        "brand_names": ["Ritalin", "Concerta", "Inspiral", "Addwize"],
        "generic_name": "Methylphenidate",
        "category": "CNS Stimulant",
        "uses": "ADHD (Attention Deficit Hyperactivity Disorder), Narcolepsy",
        "side_effects": "Decreased appetite, insomnia, nervousness, increased heart rate, headache",
        "dosage": "Children: 5mg twice daily. Adults: 10-60mg/day in divided doses",
        "warnings": "High abuse potential. Can cause dependence. Monitor growth in children",
        "interactions": ["MAOIs", "Antihypertensives", "Anticoagulants", "Antidepressants"],
        "price_range": "₹50-300 per strip",
        "prescription_required": True,
        "controlled_substance": True
    },
    
    "atomoxetine": {
        "brand_names": ["Strattera", "Atonext", "Attera"],
        "generic_name": "Atomoxetine",
        "category": "ADHD Medication (Non-stimulant)",
        "uses": "Attention Deficit Hyperactivity Disorder (ADHD)",
        "side_effects": "Nausea, vomiting, fatigue, decreased appetite, dizziness, mood swings",
        "dosage": "Starting: 40mg/day. Target: 80mg/day. Maximum: 100mg/day",
        "warnings": "Risk of suicidal thoughts. May increase blood pressure and heart rate",
        "interactions": ["MAOIs", "CYP2D6 inhibitors", "Albuterol", "Antidepressants"],
        "price_range": "₹200-800 per strip",
        "prescription_required": True
    },
    
    # GENERAL MEDICINES (keeping existing ones)
    "paracetamol": {
        "brand_names": ["Crocin", "Dolo 650", "Calpol", "Tylenol"],
        "generic_name": "Paracetamol/Acetaminophen",
        "category": "Analgesic/Antipyretic",
        "uses": "Fever, mild to moderate pain, headache, toothache, cold and flu symptoms",
        "side_effects": "Generally well-tolerated. Rare: allergic reactions, skin rash. Overdose can cause liver damage",
        "dosage": "Adults: 500-1000mg every 4-6 hours. Maximum 4g/day. Children: 10-15mg/kg",
        "warnings": "Avoid overdose. Do not exceed 4g per day. Caution in liver disease. Avoid alcohol",
        "interactions": ["Warfarin", "Alcohol", "Other paracetamol-containing drugs"],
        "price_range": "₹10-30 per strip",
        "prescription_required": False
    },
    
    "ibuprofen": {
        "brand_names": ["Brufen", "Combiflam (with paracetamol)", "Ibugesic"],
        "generic_name": "Ibuprofen",
        "category": "NSAID (Non-steroidal anti-inflammatory)",
        "uses": "Pain relief, fever, inflammation, arthritis, menstrual cramps, headache",
        "side_effects": "Stomach upset, heartburn, nausea, dizziness. Serious: stomach bleeding, kidney problems",
        "dosage": "Adults: 200-400mg every 4-6 hours. Maximum 1200mg/day without medical supervision",
        "warnings": "Take with food. Avoid in stomach ulcers, kidney disease. Increases heart attack risk with long use",
        "interactions": ["Aspirin", "Blood thinners", "ACE inhibitors", "Lithium"],
        "price_range": "₹15-50 per strip",
        "prescription_required": False
    },
    
    "amoxicillin": {
        "brand_names": ["Mox", "Novamox", "Amoxil"],
        "generic_name": "Amoxicillin",
        "category": "Antibiotic (Penicillin)",
        "uses": "Bacterial infections: respiratory tract, ear, throat, urinary tract, skin infections",
        "side_effects": "Diarrhea, nausea, skin rash. Rare: severe allergic reactions",
        "dosage": "250-500mg three times daily or 875mg twice daily for 7-10 days",
        "warnings": "Complete full course. Allergic reactions possible. May reduce birth control effectiveness",
        "interactions": ["Methotrexate", "Warfarin", "Oral contraceptives"],
        "price_range": "₹50-150 per strip",
        "prescription_required": True
    },
    
    "azithromycin": {
        "brand_names": ["Azithral", "Zithromax", "Azee"],
        "generic_name": "Azithromycin",
        "category": "Antibiotic (Macrolide)",
        "uses": "Respiratory infections, skin infections, ear infections, sexually transmitted diseases",
        "side_effects": "Diarrhea, nausea, abdominal pain, vomiting. Rare: irregular heartbeat",
        "dosage": "500mg on day 1, then 250mg once daily for 4 days. Or 500mg once daily for 3 days",
        "warnings": "Can cause heart rhythm problems. Complete full course. Take 1 hour before or 2 hours after meals",
        "interactions": ["Antacids", "Warfarin", "Digoxin", "Ergot derivatives"],
        "price_range": "₹50-200 per strip",
        "prescription_required": True
    },
    
    "metformin": {
        "brand_names": ["Glycomet", "Glucophage", "Glyciphage"],
        "generic_name": "Metformin",
        "category": "Antidiabetic (Biguanide)",
        "uses": "Type 2 diabetes mellitus, PCOS (polycystic ovary syndrome)",
        "side_effects": "Nausea, vomiting, diarrhea, metallic taste. Rare: lactic acidosis",
        "dosage": "Starting: 500mg once or twice daily. Maximum: 2000-2500mg/day",
        "warnings": "Stop before surgery or contrast procedures. Monitor kidney function. Risk of B12 deficiency",
        "interactions": ["Alcohol", "Contrast dyes", "Carbonic anhydrase inhibitors"],
        "price_range": "₹20-100 per strip",
        "prescription_required": True
    },
    
    "amlodipine": {
        "brand_names": ["Amlip", "Norvasc", "Amlong"],
        "generic_name": "Amlodipine",
        "category": "Calcium Channel Blocker",
        "uses": "High blood pressure, angina (chest pain), coronary artery disease",
        "side_effects": "Swelling of ankles/feet, dizziness, flushing, palpitations, fatigue",
        "dosage": "5-10mg once daily. Start with 5mg in elderly",
        "warnings": "May cause low blood pressure. Monitor blood pressure regularly",
        "interactions": ["Simvastatin (dose limit)", "CYP3A4 inhibitors", "Grapefruit juice"],
        "price_range": "₹30-150 per strip",
        "prescription_required": True
    },
    
    "atorvastatin": {
        "brand_names": ["Atorva", "Lipitor", "Storvas"],
        "generic_name": "Atorvastatin",
        "category": "Statin (Cholesterol lowering)",
        "uses": "High cholesterol, prevention of heart disease and stroke",
        "side_effects": "Muscle pain, joint pain, diarrhea, upset stomach. Rare: liver problems, rhabdomyolysis",
        "dosage": "10-80mg once daily. Usually start with 10-20mg",
        "warnings": "Monitor liver function. Report muscle pain immediately. Avoid in pregnancy",
        "interactions": ["Fibrates", "Niacin", "Cyclosporine", "Certain antibiotics"],
        "price_range": "₹50-300 per strip",
        "prescription_required": True
    },
    
    "omeprazole": {
        "brand_names": ["Omez", "Prilosec", "Ocid"],
        "generic_name": "Omeprazole",
        "category": "Proton Pump Inhibitor",
        "uses": "Acid reflux, GERD, peptic ulcers, Zollinger-Ellison syndrome",
        "side_effects": "Headache, nausea, diarrhea, stomach pain, gas. Long-term: B12 deficiency, bone fractures",
        "dosage": "20-40mg once daily before meals. Take 30-60 minutes before food",
        "warnings": "Long-term use may cause nutrient deficiencies. Increased infection risk",
        "interactions": ["Clopidogrel", "Methotrexate", "Certain antifungals"],
        "price_range": "₹50-200 per strip",
        "prescription_required": True
    },
    
    "cetirizine": {
        "brand_names": ["Cetzine", "Zyrtec", "Alerid"],
        "generic_name": "Cetirizine",
        "category": "Antihistamine",
        "uses": "Allergic rhinitis, chronic urticaria, allergic conjunctivitis",
        "side_effects": "Drowsiness (less than older antihistamines), dry mouth, fatigue, dizziness",
        "dosage": "10mg once daily. 5mg for children 6-12 years",
        "warnings": "May cause drowsiness. Caution while driving. Reduce dose in kidney disease",
        "interactions": ["Alcohol", "CNS depressants", "Theophylline"],
        "price_range": "₹20-80 per strip",
        "prescription_required": False
    },
    
    "montelukast": {
        "brand_names": ["Montair", "Singulair", "Montek"],
        "generic_name": "Montelukast",
        "category": "Leukotriene Receptor Antagonist",
        "uses": "Asthma prevention, allergic rhinitis, exercise-induced bronchoconstriction",
        "side_effects": "Headache, abdominal pain, cough, dizziness. Rare: mood changes, depression",
        "dosage": "Adults: 10mg once daily in evening. Children 6-14 years: 5mg once daily",
        "warnings": "Monitor for behavior and mood changes. Not for acute asthma attacks",
        "interactions": ["Phenobarbital", "Phenytoin", "Rifampin"],
        "price_range": "₹80-300 per strip",
        "prescription_required": True
    },
    
    "prednisolone": {
        "brand_names": ["Omnacortil", "Wysolone", "Predone"],
        "generic_name": "Prednisolone",
        "category": "Corticosteroid",
        "uses": "Inflammatory conditions, allergies, asthma, autoimmune disorders",
        "side_effects": "Weight gain, mood changes, increased appetite, insomnia, high blood sugar",
        "dosage": "5-60mg/day depending on condition. Taper gradually when stopping",
        "warnings": "Suppresses immune system. Monitor blood sugar. Can cause osteoporosis with long use",
        "interactions": ["NSAIDs", "Vaccines", "Antidiabetic drugs", "Anticoagulants"],
        "price_range": "₹30-150 per strip",
        "prescription_required": True
    },
    
    "vitamin_d3": {
        "brand_names": ["Shelcal", "Uprise D3", "Calcirol"],
        "generic_name": "Cholecalciferol",
        "category": "Vitamin Supplement",
        "uses": "Vitamin D deficiency, osteoporosis prevention, bone health",
        "side_effects": "Generally safe. Excess: nausea, vomiting, weakness, kidney problems",
        "dosage": "1000-2000 IU daily for maintenance. 60,000 IU weekly for deficiency",
        "warnings": "Monitor calcium levels with high doses. Caution in kidney disease",
        "interactions": ["Digoxin", "Thiazide diuretics", "Calcium supplements"],
        "price_range": "₹100-300 per pack",
        "prescription_required": False
    },
    
    # AYURVEDIC MEDICINES
    "ashwagandha": {
        "brand_names": ["Himalaya Ashwagandha", "Dabur Ashwagandha", "Patanjali Ashwagandha"],
        "generic_name": "Withania somnifera",
        "category": "Ayurvedic Adaptogen",
        "uses": "Stress, anxiety, general weakness, immunity, male fertility",
        "side_effects": "Generally safe. May cause drowsiness, stomach upset, diarrhea in some",
        "dosage": "300-500mg standardized extract twice daily or as directed",
        "warnings": "May lower blood sugar and blood pressure. Avoid in pregnancy. May interact with thyroid meds",
        "interactions": ["Sedatives", "Thyroid medications", "Immunosuppressants", "Antidiabetic drugs"],
        "price_range": "₹100-500 per bottle",
        "prescription_required": False
    },
    
    "triphala": {
        "brand_names": ["Dabur Triphala", "Himalaya Triphala", "Zandu Triphala"],
        "generic_name": "Three fruits (Amalaki, Bibhitaki, Haritaki)",
        "category": "Ayurvedic Digestive",
        "uses": "Constipation, digestive health, detoxification, immunity",
        "side_effects": "May cause diarrhea in high doses, abdominal cramps",
        "dosage": "1-2 teaspoons powder with warm water at bedtime or 1-2 tablets twice daily",
        "warnings": "Start with lower dose. May interfere with nutrient absorption if overused",
        "interactions": ["Blood thinners", "Antidiabetic drugs"],
        "price_range": "₹50-300 per pack",
        "prescription_required": False
    }
}