# ============================
# Base image
# ============================
FROM python:3.11-slim

# ============================
# Environment
# ============================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ============================
# System dependencies
# ============================
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    ffmpeg \
    curl \
    && rm -rf /var/lib/apt/lists/*


# ============================
# Workdir
# ============================
WORKDIR /app

# ============================
# Install Python dependencies
# ============================
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ============================
# Copy project
# ============================
COPY . .

# ============================
# Entrypoint
# ============================
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# ============================
# Static files
# ============================
RUN mkdir -p /app/staticfiles

# ============================
# Expose port
# ============================
EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
