"""
config.py
Configurações centrais do Livro Digital Indicador Real.
Todos os caminhos são relativos à raiz do projeto.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "indicador_real.db"

BACKUP_DIR = BASE_DIR / "backups"
AUTOMATIC_BACKUP_DIR = BACKUP_DIR / "automatic"
MANUAL_BACKUP_DIR = BACKUP_DIR / "manual"

REPORTS_DIR = BASE_DIR / "reports"
REPORTS_GENERATED_DIR = REPORTS_DIR / "generated"

LOG_DIR = BASE_DIR / "logs"
SYSTEM_LOG = LOG_DIR / "system.log"
ACCESS_LOG = LOG_DIR / "access.log"
AUDIT_LOG = LOG_DIR / "audit.log"

APP_NAME = "Livro Digital - Indicador Real"
APP_VERSION = "1.0.0"

AUTO_BACKUP_ON_START = False

def preparar_diretorios() -> None:
    for path in (
        DATABASE_DIR, AUTOMATIC_BACKUP_DIR, MANUAL_BACKUP_DIR,
        REPORTS_GENERATED_DIR, LOG_DIR
    ):
        path.mkdir(parents=True, exist_ok=True)
    for path in (SYSTEM_LOG, ACCESS_LOG, AUDIT_LOG):
        path.touch(exist_ok=True)
