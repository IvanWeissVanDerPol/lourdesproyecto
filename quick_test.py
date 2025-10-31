#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quick Test - Verificación rápida del sistema

Este script verifica que todos los módulos principales funcionan correctamente.
"""

import sys
from pathlib import Path

# Fix encoding for Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout.reconfigure(encoding='utf-8')

def test_imports():
    """Test: Verificar que todos los módulos se importan correctamente"""
    print("="*60)
    print("TEST 1: Importación de Módulos")
    print("="*60)

    try:
        from src.core.styles.apa_styles import APA_HEADING_1
        print("✓ src.core.styles.apa_styles")

        from src.core.styles.style_factory import StyleFactory
        print("✓ src.core.styles.style_factory")

        from src.core.parsers.markdown_parser import MarkdownParser
        print("✓ src.core.parsers.markdown_parser")

        from src.core.parsers.inline_formatter import InlineFormatter
        print("✓ src.core.parsers.inline_formatter")

        from src.core.builders.document_builder import DocumentBuilder
        print("✓ src.core.builders.document_builder")

        from src.config.apa7_config import APAConfig
        print("✓ src.config.apa7_config")

        from src.core.converter import APAConverter
        print("✓ src.core.converter")

        from src.core.utils.exceptions import APAConverterError
        print("✓ src.core.utils.exceptions")

        from src.core.utils.text_cleaner import TextCleaner
        print("✓ src.core.utils.text_cleaner")

        from src.core.utils.logger import APAConverterLogger
        print("✓ src.core.utils.logger")

        print("\nOK Todos los modulos se importaron correctamente\n")
        return True

    except ImportError as e:
        print(f"\nX Error de importacion: {e}\n")
        return False


def test_style_definitions():
    """Test: Verificar definiciones de estilos"""
    print("="*60)
    print("TEST 2: Definiciones de Estilos APA")
    print("="*60)

    try:
        from src.core.styles.apa_styles import (
            APA_NORMAL, APA_HEADING_1, APA_HEADING_2,
            APA_HEADING_3, APA_HEADING_4, APA_HEADING_5,
            APA_REFERENCE, APA_QUOTE
        )

        assert APA_NORMAL.name == 'Normal'
        print("✓ APA_NORMAL definido correctamente")

        assert APA_HEADING_1.bold == True
        print("✓ APA_HEADING_1 es negrita")

        assert APA_REFERENCE.first_line_indent.inches == -0.5
        print("✓ APA_REFERENCE tiene sangría francesa")

        print("\nOK Todas las definiciones son correctas\n")
        return True

    except Exception as e:
        print(f"\nX Error: {e}\n")
        return False


def test_parser():
    """Test: Verificar parser de Markdown"""
    print("="*60)
    print("TEST 3: Parser de Markdown")
    print("="*60)

    try:
        from src.core.parsers.markdown_parser import MarkdownParser

        parser = MarkdownParser()

        # Test simple
        content = "# Título\n\nPárrafo de texto."
        elements = parser.parse_content(content)

        assert len(elements) == 2
        print(f"✓ Parser procesó {len(elements)} elementos")

        from src.core.parsers.markdown_parser import ElementType
        assert elements[0].type == ElementType.HEADING_1
        print("✓ Detectó heading correctamente")

        assert elements[1].type == ElementType.PARAGRAPH
        print("✓ Detectó párrafo correctamente")

        print("\nOK Parser funciona correctamente\n")
        return True

    except Exception as e:
        print(f"\nX Error: {e}\n")
        return False


def test_config():
    """Test: Verificar sistema de configuración"""
    print("="*60)
    print("TEST 4: Sistema de Configuración")
    print("="*60)

    try:
        from src.config.apa7_config import APAConfig

        # Test configuración por defecto
        config = APAConfig.default_student()
        assert config.document_type == 'student'
        print("✓ Configuración student cargada")

        config_prof = APAConfig.default_professional()
        assert config_prof.document_type == 'professional'
        print("✓ Configuración professional cargada")

        # Test YAML
        yaml_path = Path('config/apa7_student.yaml')
        if yaml_path.exists():
            config_yaml = APAConfig.from_yaml(yaml_path)
            print("✓ Configuración YAML cargada correctamente")

        print("\nOK Sistema de configuracion funciona\n")
        return True

    except Exception as e:
        print(f"\nX Error: {e}\n")
        return False


def test_converter():
    """Test: Verificar convertidor principal"""
    print("="*60)
    print("TEST 5: Convertidor Principal")
    print("="*60)

    try:
        from src.core.converter import APAConverter

        # Test inicialización
        converter = APAConverter.from_defaults('student')
        print("✓ Convertidor inicializado (student)")

        converter_prof = APAConverter.from_defaults('professional')
        print("✓ Convertidor inicializado (professional)")

        print("\nOK Convertidor funciona correctamente\n")
        return True

    except Exception as e:
        print(f"\nX Error: {e}\n")
        return False


def main():
    """Ejecutar todos los tests"""
    print("\n" + "="*60)
    print(" VERIFICACIÓN RÁPIDA DEL SISTEMA APA 7 CONVERTER v2.0.0")
    print("="*60 + "\n")

    results = []

    results.append(test_imports())
    results.append(test_style_definitions())
    results.append(test_parser())
    results.append(test_config())
    results.append(test_converter())

    # Resumen
    print("="*60)
    print(" RESUMEN DE TESTS")
    print("="*60)

    passed = sum(results)
    total = len(results)

    print(f"\nTests pasados: {passed}/{total}")

    if passed == total:
        print("\n** TODOS LOS TESTS PASARON! **")
        print("\nOK El sistema esta listo para usar")
        print("\nPróximos pasos:")
        print("  1. Ejecutar tests completos: pytest")
        print("  2. Probar CLI: python -m src.cli --help")
        print("  3. Ver ejemplos: python docs/examples/basic_usage.py")
        return 0
    else:
        print(f"\nWARNING: {total - passed} tests fallaron")
        print("\nRevisa los errores arriba y corrige los problemas.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
