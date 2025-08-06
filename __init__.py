# __init__.py — инициализация FDL-SKLONOS ядра

__version__ = "0.1.0"
__name__ = "fdl_sklonos_core"
__description__ = "Σ-FDL Склоняющий Логос: Ядро падежного смысла для семантической архитектуры ИИ и языка"

from .fdl_compiler import FDLCompiler
from .fdl_gateway import FDLGateway
from .fdl_translator import FDLTranslator
from .fdl_ontology_map import FDLOntologyMap
from .sklonos_logic import PadezhSklonLogic
from .sklon_graph import SklonGraphVisualizer
