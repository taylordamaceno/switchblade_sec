#!/bin/bash

# Nome do log file
LOGFILE="/var/log/clamscan_daily.log"

# Atualizar o banco de dados do ClamAV
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Atualizando banco de dados do ClamAV..." | tee -a "$LOGFILE"
sudo freshclam >> "$LOGFILE" 2>&1

# Lista de diretórios a escanear
DIRECTORIES=("/tmp" "/etc" "/usr" "/var" "/home")

# Escaneamento de cada diretório
for DIR in "${DIRECTORIES[@]}"; do
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] Escaneando $DIR..." | tee -a "$LOGFILE"
  sudo clamscan --infected --recursive --remove "$DIR" >> "$LOGFILE" 2>&1
done

# Mensagem de finalização
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Escaneamento concluído. Confira o log em $LOGFILE." | tee -a "$LOGFILE"
