#!/bin/bash
# 🦞 Business Lead Gen - Campaign Manager
# Master script for managing email campaigns

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

show_menu() {
    echo ""
    echo "🦞 Business Lead Gen - Campaign Manager"
    echo "========================================"
    echo ""
    echo "📊 CURRENT STATUS"
    echo "----------------"
    
    # Count emails by status
    if [ -f "proposals-100.csv" ]; then
        total=$(tail -n +2 proposals-100.csv | wc -l)
        sent=$(grep -c ",sent," proposals-100.csv 2>/dev/null || echo 0)
        draft=$(grep -c ",draft," proposals-100.csv 2>/dev/null || echo 0)
        echo "NYC Campaign (proposals-100.csv):"
        echo "  Total: $total | Sent: $sent | Draft: $draft"
    fi
    
    # Count US batch files
    us_batch_count=$(ls -1 scripts/batches/proposals-*.csv 2>/dev/null | wc -l)
    if [ $us_batch_count -gt 0 ]; then
        echo ""
        echo "🇺🇸 US Batches:"
        ls -1 scripts/batches/proposals-*.csv 2>/dev/null | head -6 | while read f; do
            name=$(basename "$f")
            count=$(tail -n +2 "$f" | wc -l)
            echo "  • $name ($count leads)"
        done
        if [ $us_batch_count -gt 6 ]; then
            echo "  ... and $((us_batch_count - 6)) more"
        fi
    fi
    
    # Count UK batch files
    uk_batch_count=$(ls -1 scripts/batches-uk/proposals-*.csv 2>/dev/null | wc -l)
    if [ $uk_batch_count -gt 0 ]; then
        echo ""
        echo "🇬🇧 UK Batches:"
        ls -1 scripts/batches-uk/proposals-*.csv 2>/dev/null | head -6 | while read f; do
            name=$(basename "$f")
            count=$(tail -n +2 "$f" | wc -l)
            echo "  • $name ($count leads)"
        done
        if [ $uk_batch_count -gt 6 ]; then
            echo "  ... and $((uk_batch_count - 6)) more"
        fi
    fi
    
    echo ""
    echo "📋 ACTIONS"
    echo "----------"
    echo "1. Send NYC emails (20 today)"
    echo "2. Send NYC emails (50 today)"
    echo "3. Send follow-up #1 (3 days)"
    echo "4. Send follow-up #2 (10 days)"
    echo "5. Launch US batch (LA Restaurants)"
    echo "6. Launch US batch (Chicago Restaurants)"
    echo "7. Launch US batch (Miami Restaurants)"
    echo "8. Setup automated follow-ups (cron)"
    echo "9. View campaign stats"
    echo "U. Launch UK batch (London Restaurants)"
    echo "K. Launch UK batch (Manchester Restaurants)"
    echo "L. Launch UK batch (Birmingham Restaurants)"
    echo "0. Exit"
    echo ""
}

send_nyc() {
    limit=$1
    echo "📧 Sending $limit NYC emails..."
    python3 scripts/send_emails.py --input proposals-100.csv --start-index 0 --delay 60 2>&1 | head -50
}

send_followup() {
    num=$1
    echo "🔔 Sending follow-up #$num..."
    python3 scripts/send_follow_ups.py --input proposals-100.csv --follow-up $num --dry-run
    echo ""
    read -p "Send for real? (y/n): " confirm
    if [ "$confirm" = "y" ]; then
        python3 scripts/send_follow_ups.py --input proposals-100.csv --follow-up $num
    fi
}

launch_batch() {
    batch=$1
    file="batches/$batch"
    if [ -f "$file" ]; then
        echo "📧 Launching batch: $batch"
        python3 scripts/send_emails.py --input "$file" --limit 20 --delay 60 2>&1 | head -50
    else
        echo "❌ Batch not found: $file"
    fi
}

setup_automation() {
    echo "🔧 Setting up automation..."
    bash scripts/setup-followups.sh
}

show_stats() {
    echo ""
    echo "📊 Campaign Statistics"
    echo "======================"
    echo ""
    
    if [ -f "proposals-100.csv" ]; then
        echo "🇺🇸 NYC Campaign:"
        total=$(tail -n +2 proposals-100.csv | wc -l)
        sent=$(grep -c ",sent," proposals-100.csv 2>/dev/null || echo 0)
        
        echo "  Emails sent: $sent / $total"
        echo "  Expected replies: $((sent * 5 / 100)) - $((sent * 10 / 100))"
        echo "  Expected conversions: $((sent * 1 / 100)) - $((sent * 3 / 100))"
        echo "  Potential revenue: £$((sent * 1 / 100 * 397)) - £$((sent * 3 / 100 * 397))"
    fi
    
    echo ""
    echo "📦 Lead Inventory:"
    us_count=$(ls -1 scripts/batches/proposals-*.csv 2>/dev/null | wc -l)
    uk_count=$(ls -1 scripts/batches-uk/proposals-*.csv 2>/dev/null | wc -l)
    us_leads=$((us_count * 50))
    uk_leads=$((uk_count * 50))
    total_leads=$((us_leads + uk_leads + 100))
    
    echo "  🇺🇸 US Batches: $us_count ($us_leads leads)"
    echo "  🇬🇧 UK Batches: $uk_count ($uk_leads leads)"
    echo "  🗽 NYC Original: 100 leads"
    echo "  ━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  TOTAL: $total_leads leads"
    
    echo ""
    echo "💰 Total Revenue Potential:"
    total_potential_conservative=$((total_leads * 1 / 100 * 397))
    total_potential_optimistic=$((total_leads * 3 / 100 * 397))
    echo "  Conservative (1%): £$total_potential_conservative"
    echo "  Optimistic (3%): £$total_potential_optimistic"
    
    echo ""
}

# Main loop
while true; do
    show_menu
    read -p "Choose action: " choice
    
    case $choice in
        1) send_nyc 20 ;;
        2) send_nyc 50 ;;
        3) send_followup 1 ;;
        4) send_followup 2 ;;
        5) launch_batch "scripts/batches/proposals-LA-Restaurants-20260315.csv" ;;
        6) launch_batch "scripts/batches/proposals-Chicago-Restaurants-20260315.csv" ;;
        7) launch_batch "scripts/batches/proposals-Miami-Restaurants-20260315.csv" ;;
        8) setup_automation ;;
        9) show_stats ;;
        U|u) launch_batch "scripts/batches-uk/proposals-London-Restaurants-UK-20260315.csv" ;;
        K|k) launch_batch "scripts/batches-uk/proposals-Manchester-Restaurants-UK-20260315.csv" ;;
        L|l) launch_batch "scripts/batches-uk/proposals-Birmingham-Restaurants-UK-20260315.csv" ;;
        0) echo "👋 Goodbye!"; exit 0 ;;
        *) echo "❌ Invalid choice" ;;
    esac
done
