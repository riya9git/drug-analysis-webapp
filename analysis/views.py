from django.shortcuts import render

import pandas as pd
import os
from django.shortcuts import render
from django.conf import settings

def drug_summary(request):
    # Path to the dataset
    file_path = os.path.join(settings.BASE_DIR, 'analysis', 'data', 'prescription_drugs_introduced_to_market.csv')
    
    # Load and analyze data
    df = pd.read_csv(file_path)
    
    if 'Approval Date' in df.columns:
        df['Approval Date'] = pd.to_datetime(df['Approval Date'], errors='coerce')
        df['Approval Year'] = df['Approval Date'].dt.year
    
    year_counts = df['Approval Year'].value_counts().sort_index()
    top_sponsors = df['Sponsor'].value_counts().head(5) if 'Sponsor' in df.columns else None
    top_classes = df['Therapeutic Class'].value_counts().head(5) if 'Therapeutic Class' in df.columns else None

    context = {
        'total': len(df),
        'year_data': year_counts.to_dict(),
        'top_sponsors': top_sponsors.to_dict() if top_sponsors is not None else None,
        'top_classes': top_classes.to_dict() if top_classes is not None else None
    }
    
    return render(request, 'analysis/summary.html', context)
