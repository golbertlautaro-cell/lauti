import pytest
from biblioteca import Biblioteca, Material, Libro, Ebook, Revista

def test_constructor_biblioteca():
    biblioteca = Biblioteca("material.csv")
    assert biblioteca is not None
    assert len(biblioteca.cantidad_materiales()) == 6

def test_constructor_archivo_inexistente():
    with pytest.raises(FileNotFoundError):
        Biblioteca("archivo_inexistente.csv")

def test_cantidad_por_tipo():
    biblioteca = Biblioteca("material.csv")
    cantidades = biblioteca.cantidad_por_tipo()
    assert cantidades == { "Libro": 2, "Ebook": 2, "Revista": 2 }

def test_libro_45_dias():
    libro = Libro("L001", "El Quijote", "Miguel de Cervantes", 200, 45)
    assert libro.calcular_costo_mantenimiento() == 200

def test_libro_15_dias():
    libro = Libro("L002", "Cien Años de Soledad", "Gabriel García Márquez", 250, 15)
    assert libro.calcular_costo_mantenimiento() == 100

def test_ebook_valor_400():
    ebook = Ebook("E101", "Introducción a Python", "Mark Lutz", 400, 400)
    assert ebook.calcular_costo_mantenimiento() == 20

def test_ebook_valor_350():
    ebook = Ebook("E102", "Machine Learning Basics", "Andrew Ng", 350, 350)
    assert ebook.calcular_costo_mantenimiento() == 17.5

def test_revista_importada():
    revista = Revista("R201", "Nature Science", "Autor Varios", 100, "importada")
    assert revista.calcular_costo_mantenimiento() == 60

def test_revista_nacional():
    revista = Revista("R202", "Revista Tecnología", "Autor Varios", 80, "nacional")
    assert revista.calcular_costo_mantenimiento() == 50

def test_calcular_promedio_precios_base():
    biblioteca = Biblioteca("material.csv")
    promedio = biblioteca.calcular_promedio_precios_base()
    assert promedio == 230

def test_material_mayor_costo_mantenimiento():
    biblioteca = Biblioteca("material.csv")
    material_caro = biblioteca.obtener_material_mayor_costo_mantenimiento()
    assert material_caro.codigo == "L001"
    assert material_caro.titulo == "El Quijote"
    assert material_caro.calcular_costo_mantenimiento() == 200

def test_suma_costo_mantenimiento():
    biblioteca = Biblioteca("material.csv")
    suma_mantenimiento = biblioteca.calcular_suma_costo_mantenimiento()
    assert suma_mantenimiento == 447.5

def test_contar_libros_mas_30_dias():
    biblioteca = Biblioteca("material.csv")
    libros_mas_30 = biblioteca.contar_libros_mas_30_dias()
    assert libros_mas_30 == 1

def test_contar_revistas_importadas():
    biblioteca = Biblioteca("material.csv")
    revistas_importadas = biblioteca.contar_revistas_importadas()
    assert revistas_importadas == 1

def test_herencia_materiales():
    assert issubclass(Libro, Material)
    assert issubclass(Ebook, Material)
    assert issubclass(Revista, Material)

def test_composicion_biblioteca_materiales():
    biblioteca = Biblioteca("material.csv")
    assert hasattr(biblioteca, 'materiales')
    for material in biblioteca.materiales:
        assert isinstance(material, Material)

def test_atributos_libro():
    libro = Libro("L001", "El Quijote", "Miguel de Cervantes", 200, 45)
    assert libro.tipo == 1
    assert libro.codigo == "L001"
    assert libro.titulo == "El Quijote"
    assert libro.autor == "Miguel de Cervantes"
    assert libro.precio_base == 200
    assert libro.dias_prestados == 45

def test_atributos_ebook():
    ebook = Ebook("E101", "Introducción a Python", "Mark Lutz", 400, 400)
    assert ebook.tipo == 2
    assert ebook.valor_venta == 400

def test_atributos_revista():
    revista = Revista("R201", "Nature Science", "Autor Varios", 100, "importada")
    assert revista.tipo == 3
    assert revista.origen == "importada"
    
