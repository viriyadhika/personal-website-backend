# Wait for kafka to fully boot
sleep 20
echo 'Wakeyy'
alembic upgrade head
# Unbuffered so that the print output is not saved to buffer but displayed straight away
uvicorn app:app --host 0.0.0.0 --port 5000