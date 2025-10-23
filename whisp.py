#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
import tempfile
from pathlib import Path

VENV = os.path.expanduser("~/whisper-env")
CLI = os.path.join(VENV, "bin", "whisper")
DESKTOP = os.path.expanduser("~/Desktop")

def find_audio_file(filename):
    """Cerca il file nel percorso assoluto o sul Desktop."""
    if os.path.isfile(filename):
        return filename
    
    cand = os.path.join(DESKTOP, filename)
    if os.path.isfile(cand):
        return cand
    
    return None

def check_dependencies():
    """Verifica che siano installati whisper e ffmpeg."""
    if not os.path.isfile(CLI):
        print(f"❌ CLI non trovato: {CLI}\nAttiva venv e installa openai-whisper.")
        sys.exit(1)
    
    if not shutil.which("ffmpeg"):
        print("❌ ffmpeg non trovato. Installa con: brew install ffmpeg")
        sys.exit(1)

def transcribe_single(audio_path, temp_dir):
    """Trascrivi un singolo file e ritorna il testo."""
    defaults = [
        "--model", "base",
        "--language", "English",
        "--output_format", "txt",
        "--output_dir", temp_dir,
    ]
    
    cmd = [CLI, audio_path] + defaults
    
    try:
        print(f"🎙️  Trascrivo: {os.path.basename(audio_path)}...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"❌ Errore nella trascrizione di {audio_path}")
            print(result.stderr)
            return None
        
        # Whisper crea un file .txt con lo stesso nome (senza estensione originale)
        base_name = Path(audio_path).stem
        txt_file = os.path.join(temp_dir, f"{base_name}.txt")
        
        if os.path.isfile(txt_file):
            with open(txt_file, 'r', encoding='utf-8') as f:
                text = f.read()
            print(f"✅ Completato: {os.path.basename(audio_path)}")
            return text
        
        return None
    
    except Exception as e:
        print(f"❌ Errore: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Uso: whisp file1.m4a [file2.mp3 file3.mp4 ...]")
        sys.exit(1)
    
    audio_files = sys.argv[1:]
    check_dependencies()
    os.makedirs(DESKTOP, exist_ok=True)
    
    # Trova e valida tutti i file
    resolved_files = []
    for f in audio_files:
        path = find_audio_file(f)
        if path:
            resolved_files.append(path)
        else:
            print(f"⚠️  File non trovato: {f}")
    
    if not resolved_files:
        print("❌ Nessun file valido trovato.")
        sys.exit(1)
    
    # Usa una temp directory per i file temporanei
    with tempfile.TemporaryDirectory() as temp_dir:
        all_texts = []
        
        for audio_file in resolved_files:
            text = transcribe_single(audio_file, temp_dir)
            if text:
                all_texts.append(text)
        
        if not all_texts:
            print("❌ Nessuna trascrizione completata.")
            sys.exit(1)
        
        # Combina tutti i testi senza separazioni
        combined_text = "\n".join(all_texts)
        
        # Usa il nome del primo file come output
        first_file = Path(resolved_files[0]).stem
        output_name = f"{first_file}.txt"
        output_path = os.path.join(DESKTOP, output_name)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(combined_text)
        
        print(f"\n✨ Trascrizione completata!")
        print(f"📄 Salvato: {output_path}")
        print(f"📊 File processati: {len(resolved_files)}")
        print(f"📝 Caratteri: {len(combined_text)}")

if __name__ == "__main__":
    sys.exit(main())
