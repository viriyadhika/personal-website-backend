# Wait for kafka to fully boot
sleep 15
echo 'Wakeyy'
alembic upgrade head
python3 -u -m app setup
# Unbuffered so that the print output is not saved to buffer but displayed straight away
python3 -u -m app consumer