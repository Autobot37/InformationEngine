import numpy as np
import pandas as pd
from dataclasses import dataclass,field
from typing import Literal,Optional,Dict,List,Union,Any
ContentTypes =  Literal["text","table","image","audio"]

@dataclass
class Document:
    id:str
    content:Union[str, pd.dataframe]
    content_type:ContentTypes=field(default="text")
    score = Optional[float]=None
    embedding:Optional[np.ndarray] = None


    def __init__(self,
                content,
                content_type,
                id,
                score,
                embedding):

                if content is None:
                    raise ValueError("doc is empty")
                
                self.content  = content
                self.content_type = content_type
                self.score = score
                self.meta = meta or {}

                if embedding is not None:
                    embedding = np.asarray(embedding)
                self.embedding = embedding

                if id is not None:
                    self.id:str = str(id)
                else:
                    self.id = "default_id"
    
    def to_dict(self,field_map:Optional[Dict[str,Any]]=None) -> Dict:
        if not field_map:
            field_map = {}
        
        inv_field_map = {v:k for k, v in field.map.items()}
        _doc = Dict[str, str] = {}
        for k, v in self.__dict__.items():
            if k.startswith("-"):
                continue
            if k == "content":
                if self.content_type == "table" and isinstance(self.content, pd.DataFrame):
                    v = [self.content.columns.tolist()] + self.content.values.tolist()
            k = k if k not in inv_field_map else inv_field_map[k]
            _doc[k] = v
        return _doc
    
    def __eq__(self,other):
        content = getattr(other, "content", None)
        is_content_equal = content == self.content
        return(
            isinstance(other, self.__class__)
            and is_content_equal
            and getattr(other, "content_type") == self.content_type
            and getattr(other, "id") == self.id 
            and getattr(other, "score") == self.score
            and np.array.equal(getattr(other, "embeddig") , self.embedding)
        )
    
    
        




