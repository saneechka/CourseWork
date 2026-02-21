# Преобразование Фурье | Fourier Transform
## Курсовая работа | Course Work




### Русская версия

#### Описание
Курсовая работа посвящена изучению и практическому применению преобразования Фурье в различных областях науки и техники.

#### Основные разделы
1. **Теоретическая часть**
   - Базовые понятия
   - Свойства и теоремы
   - Методы вычисления
   - Связь с другими преобразованиями

2. **Практическая часть**
   - Разложение в ряд Фурье
   - Косинус преобразование
   - Преобразование Лапласа
   - Обработка сигналов
   - Сжатие изображений

---

### English version

#### Description
This coursework is dedicated to studying and practical application of Fourier transform in various fields of science and technology.

#### Main Sections
1. **Theoretical Part**
   - Basic concepts
   - Properties and theorems
   - Calculation methods
   - Relations with other transforms

2. **Practical Part**
   - Fourier series expansion
   - Cosine transform
   - Laplace transform
   - Signal processing
   - Image compression

### Technologies | Технологии
- Maple
- Python + NumPy
- LaTeX

### Project Structure | Структура проекта
```
CourseWork/
├── Task.tex              # Tasks and solutions | Задачи и решения
├── main.tex             # Main document | Основной документ
├── list.tex            # References | Список литературы
├── Conclusion.tex      # Conclusion | Заключение
├── Application.tex     # Code appendix | Приложение с кодом
└── images/            # Images | Изображения
```

### Build Instructions | Инструкция по сборке
```bash
# Install dependencies | Установка зависимостей
pip install numpy pillow

# Build LaTeX | Сборка LaTeX
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```



