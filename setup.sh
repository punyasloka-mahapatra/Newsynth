#!/bin/bash

echo "🚀 Setting up Newsynth - AI Research Assistant"
echo "============================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama is not installed."
    echo "Please install Ollama from: https://ollama.ai"
    echo "Or run: curl -fsSL https://ollama.ai/install.sh | sh"
    exit 1
fi

echo "✅ Python 3 found"
echo "✅ Ollama found"

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

# Start Ollama (if not already running)
echo "🔄 Starting Ollama service..."
ollama serve &
sleep 3

# Pull Mistral model
echo "📥 Downloading Mistral model (this may take a few minutes)..."
ollama pull mistral

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To run Newsynth:"
echo "python3 newsynth.py"
echo ""
echo "Or make it executable and run directly:"
echo "chmod +x newsynth.py"
echo "./newsynth.py"
