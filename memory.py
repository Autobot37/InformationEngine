from typing import Any, Dict, List, Optional, Union, Generator, Literal
import numpy as np
import torch
from tqdm.auto import tqdm
import pandas as pd
from scheme import Document
from base import KeywordDocumentSearch

class MemoryDocumentStore(KeywordDocumentSearch):
    def __init__(self,
                index,
                label_index,
                embedding_field:Optional[str]="embedding",
                embedding_dim:int=768,
                retrun_embedding:bool = False,
                similarity:str="dot_product",
                ):

                self.index:str = index
                self.label_index:str = label_index
                self.embedding_field = embedding_field
                self.embedding_dim = embedding_dim
                self.return_embedding = return_embedding
                self.similarity = similarity

    def write_document(
                    self,
                    documents:Union[List[dict],List[Document]],
                    index:Optional[str]=None,
                    batch_size:int=10_000,
                    header:Optional[Dict[str,str]] = None,
                    ):
                    pass
    



