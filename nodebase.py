from abc import abstractmethod
from typing import Dict, List, Optional, Dict, Union

from tqdm.auto import tqdm

from scheme import Document

class BaseComponent(ABC):

    outgoing_edges: int
    
    def __init__(self):
        pass
    