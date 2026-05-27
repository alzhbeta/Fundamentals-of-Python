from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from lab4.modules.analyze_gc import sort_by_gc

def test_gc_sorting():
    rec1 = SeqRecord(Seq("ATATATAT"), id="test1")
    rec2 = SeqRecord(Seq("GCGCGCGC"), id="test2")
    
    result = sort_by_gc([rec2, rec1])
    assert result[0][1].id == "test1"
    assert result[1][1].id == "test2"

