#!/bin/bash
# Automated Follow-Up Cron Jobs
# Run this to set up automated follow-ups

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "🔔 Setting Up Automated Follow-Ups"
echo "=================================="
echo ""

# Create cron entries
CRON_FILE="$SCRIPT_DIR/followup-crontab.txt"

cat > "$CRON_FILE" << 'EOF'
# Business Lead Gen - Automated Follow-Ups
# Run daily at 10 AM to check and send follow-ups

# Follow-up #1: 3 days after initial email
0 10 * * * cd /home/admin/.openclaw/workspace/skills/business-lead-gen && python3 scripts/send_follow_ups.py --input proposals-100.csv --follow-up 1 >> logs/followup.log 2>&1

# Follow-up #2: 10 days after initial email  
0 10 * * * cd /home/admin/.openclaw/workspace/skills/business-lead-gen && python3 scripts/send_follow_ups.py --input proposals-100.csv --follow-up 2 >> logs/followup.log 2>&1
EOF

echo "✅ Created cron file: $CRON_FILE"
echo ""
echo "📋 Cron entries:"
cat "$CRON_FILE"
echo ""

# Install crontab
echo "📥 Installing crontab..."
(crontab -l 2>/dev/null | grep -v "followup-crontab"; cat "$CRON_FILE") | crontab -

if [ $? -eq 0 ]; then
    echo "✅ Crontab installed successfully!"
else
    echo "⚠️  Could not install crontab automatically"
    echo "   Run: crontab $CRON_FILE"
fi

echo ""
echo "📊 Current crontab:"
crontab -l | grep -A10 "Follow-Up" || echo "   (no follow-up entries found)"

echo ""
echo "=================================="
echo "✅ Setup Complete!"
echo ""
echo "📝 Follow-up schedule:"
echo "   • Follow-up #1: 3 days after initial email"
echo "   • Follow-up #2: 10 days after initial email"
echo "   • Checks run daily at 10 AM"
echo ""
echo "📄 Logs: $SCRIPT_DIR/logs/followup.log"
echo ""
