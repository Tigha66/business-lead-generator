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
    
    # Count batch files
    batch_count=$(ls -1 batches/proposals-*.csv 2>/dev/null | wc -l)
    if [ $batch_count -gt 0 ]; then
        echo ""
        echo "Available Batches:"
        ls -1 batches/proposals-*.csv 2>/dev/null | while read f; do
            name=$(basename "$f")
            count=$(tail -n +2 "$f" | wc -l)
            echo "  • $name ($count leads)"
        done
    fi
    
    echo ""
    echo "📋 ACTIONS"
    echo "----------"
    echo "1. Send NYC emails (20 today)"
    echo "2. Send NYC emails (50 today)"
    echo "3. Send follow-up #1 (3 days)"
    echo "4. Send follow-up #2 (10 days)"
    echo "5. Launch new batch (LA Restaurants)"
    echo "6. Launch new batch (Chicago Restaurants)"
    echo "7. Launch new batch (Miami Restaurants)"
    echo "8. Setup automated follow-ups (cron)"
    echo "9. View campaign stats"
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
        echo "NYC Campaign:"
        total=$(tail -n +2 proposals-100.csv | wc -l)
        sent=$(grep -c ",sent," proposals-100.csv 2>/dev/null || echo 0)
        reply_rate="~5-10%"
        conv_rate="~1-3%"
        
        echo "  Emails sent: $sent / $total"
        echo "  Expected replies: $((sent * 5 / 100)) - $((sent * 10 / 100))"
        echo "  Expected conversions: $((sent * 1 / 100)) - $((sent * 3 / 100))"
        echo "  Potential revenue: £$((sent * 1 / 100 * 397)) - £$((sent * 3 / 100 * 397))"
    fi
    
    echo ""
    echo "Batch Inventory:"
    ls -1 batches/proposals-*.csv 2>/dev/null | while read f; do
        name=$(basename "$f")
        count=$(tail -n +2 "$f" | wc -l)
        potential=$((count * 2 / 100 * 397))
        echo "  • $name: $count leads (~£$potential potential)"
    done
    
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
        5) launch_batch "proposals-LA-Restaurants-20260315.csv" ;;
        6) launch_batch "proposals-Chicago-Restaurants-20260315.csv" ;;
        7) launch_batch "proposals-Miami-Restaurants-20260315.csv" ;;
        8) setup_automation ;;
        9) show_stats ;;
        0) echo "👋 Goodbye!"; exit 0 ;;
        *) echo "❌ Invalid choice" ;;
    esac
done
