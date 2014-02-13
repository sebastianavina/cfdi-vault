# encoding: utf-8

from xml.etree import ElementTree
import codecs


class Factura:
	""" 
	Clase para representar una factura
	"""
	
	def __init__(self, xml):
		self.xml = xml
		self.arbol = ElementTree.parse(self.xml)
		#codecs.open(self.xml, encoding="UTF-8"))
		self.raiz = self.arbol.getroot()
    
		return None
	
	def GetFecha(self):
		return self.raiz.attrib["fecha"]

	def GetConceptos(self):
		conceptos = self.raiz.iter("{http://www.sat.gob.mx/cfd/2}Concepto")
		return conceptos

	def GetRFC(self):
		Emisor = self.raiz.find("{http://www.sat.gob.mx/cfd/2}Emisor")
		return Emisor.attrib["rfc"]
	
	def GetFolio(self):
		serie = self.raiz.attrib["serie"] 
		folio = self.raiz.attrib["folio"]
		ret = "%s-%s" % (serie, folio)
		return ret

	def GetCFDi(self):
		cert = self.raiz.attrib["noCertificado"]
		return cert