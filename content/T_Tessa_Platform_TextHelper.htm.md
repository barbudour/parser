# TextHelper - класс
Вспомогательные методы для работы с текстом.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class TextHelper
VB __Копировать
     Public NotInheritable Class TextHelper
C++ __Копировать
     public ref class TextHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type TextHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TextHelper
##  __Методы
[DetectEncoding](M_Tessa_Platform_TextHelper_DetectEncoding.htm)|  Определяет
кодировку текста по заданному массиву байт textBytes. Если кодировка не может
быть определена, то возвращает
[Default](https://learn.microsoft.com/dotnet/api/system.text.encoding.default#system-
text-encoding-default), что соответствует текущей кодовой странице ANSI в
настройках учётной записи Windows. Возвращаемый объект не равен null.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
