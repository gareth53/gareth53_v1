try:
    from xml.etree import cElementTree as ET
except ImportError:
    import cElementTree as ET
        
__all__ = ['ET']