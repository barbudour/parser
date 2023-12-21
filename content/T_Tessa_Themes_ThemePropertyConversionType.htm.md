# ThemePropertyConversionType - перечисление
Способ преобразования значения, получаемого для заданного свойства.
Используется в расширении разметки XAML {ThemeResource ...}.
## __Definition
 **Пространство имён:** [Tessa.Themes](N_Tessa_Themes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum ThemePropertyConversionType
VB __Копировать
     Public Enumeration ThemePropertyConversionType
C++ __Копировать
     public enum class ThemePropertyConversionType
F# __Копировать
     type ThemePropertyConversionType
##  __Члены
None| 0|  Значение свойства возвращается как есть, без преобразований.  
---|---|---  
Wpf| 1|  Если значению соответствует объект WPF, то он возвращается в
преобразованном виде. В текущей версии затрагивает цвет типа StorageColor и
StorageLinearGradientBrush.  
Brush| 2|  Значение свойства преобразуется в кисть SolidColorBrush с заливкой
сплошным цветом или в кисть LinearGradientBrush с заливкой линейным
градиентом.  
## __См. также
#### Ссылки
[Tessa.Themes - пространство имён](N_Tessa_Themes.htm)
