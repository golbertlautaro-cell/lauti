import csv
from abc import ABC, abstractmethod
from math import ceil
from typing import List, Dict, Optional


class Material(ABC):
	def __init__(self, tipo: int, codigo: str, titulo: str, autor: str, precio_base: float):
		self.tipo = tipo
		self.codigo = codigo
		self.titulo = titulo
		self.autor = autor
		self.precio_base = precio_base

	@abstractmethod
	def calcular_costo_mantenimiento(self) -> float:
		pass


class Libro(Material):            
	def __init__(self, codigo: str, titulo: str, autor: str, precio_base: float, dias_prestados: int):
		super().__init__(tipo=1, codigo=codigo, titulo=titulo, autor=autor, precio_base=precio_base)
		self.dias_prestados = dias_prestados

	def calcular_costo_mantenimiento(self) -> float:
		tramos = ceil(self.dias_prestados / 30) if self.dias_prestados > 0 else 1
		return tramos * 100


class Ebook(Material):
	def __init__(self, codigo: str, titulo: str, autor: str, precio_base: float, valor_venta: float):
		super().__init__(tipo=2, codigo=codigo, titulo=titulo, autor=autor, precio_base=precio_base)
		self.valor_venta = valor_venta

	def calcular_costo_mantenimiento(self) -> float:
		return self.valor_venta * 0.05


class Revista(Material):
	def __init__(self, codigo: str, titulo: str, autor: str, precio_base: float, origen: str):
		super().__init__(tipo=3, codigo=codigo, titulo=titulo, autor=autor, precio_base=precio_base)
		self.origen = origen

	def calcular_costo_mantenimiento(self) -> float:
		base = 50
		if str(self.origen).strip().lower() == "importada":
			return base * 1.2
		return base


class Biblioteca:
	def __init__(self, archivo_csv: str):
		self.materiales: List[Material] = []
		self.cargar_materiales_desde_csv(archivo_csv)

	def cargar_materiales_desde_csv(self, archivo_csv: str) -> None:
		with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
			lector = csv.reader(csvfile)
			for fila in lector:
				if not fila or len(fila) < 6:
					continue
				tipo = int(str(fila[0]).strip())
				codigo = fila[1].strip()
				titulo = fila[2].strip()
				autor = fila[3].strip()
				precio_base = float(fila[4])
				extra = fila[5].strip()

				if tipo == 1:
					material = Libro(codigo, titulo, autor, precio_base, int(extra))
				elif tipo == 2:
					material = Ebook(codigo, titulo, autor, precio_base, float(extra))
				elif tipo == 3:
					material = Revista(codigo, titulo, autor, precio_base, extra)
				else:
					continue
				self.materiales.append(material)

	def cantidad_materiales(self) -> List[Material]:
		return self.materiales

	def cantidad_por_tipo(self) -> Dict[str, int]:
		conteo = {"Libro": 0, "Ebook": 0, "Revista": 0}
		for m in self.materiales:
			if isinstance(m, Libro):
				conteo["Libro"] += 1
			elif isinstance(m, Ebook):
				conteo["Ebook"] += 1
			elif isinstance(m, Revista):
				conteo["Revista"] += 1
		return conteo

	def calcular_promedio_precios_base(self) -> int:
		if not self.materiales:
			return 0
		total = sum(m.precio_base for m in self.materiales)
		return int(total / len(self.materiales))

	def obtener_material_mayor_costo_mantenimiento(self) -> Optional[Material]:
		if not self.materiales:
			return None
		return max(self.materiales, key=lambda m: m.calcular_costo_mantenimiento())

	def calcular_suma_costo_mantenimiento(self) -> float:
		return sum(m.calcular_costo_mantenimiento() for m in self.materiales)

	def contar_libros_mas_30_dias(self) -> int:
		return sum(1 for m in self.materiales if isinstance(m, Libro) and m.dias_prestados > 30)

	def contar_revistas_importadas(self) -> int:
		return sum(
			1
			for m in self.materiales
			if isinstance(m, Revista) and str(m.origen).strip().lower() == "importada"
		)

