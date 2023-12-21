# DebugHelper - класс
Вспомогательные методы для удобства отладки.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class DebugHelper
VB __Копировать
     Public NotInheritable Class DebugHelper
C++ __Копировать
     public ref class DebugHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type DebugHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DebugHelper
##  __Методы
[FormatNullable(String)](M_Tessa_Platform_DebugHelper_FormatNullable.htm)|
Форматирует строку, заключая её в кавычки или выполняя вывод строки
[NullText](F_Tessa_Platform_DebugHelper_NullText.htm), если строка равна null.  
---|---  
[FormatNullable<T>(Nullable<T>)](M_Tessa_Platform_DebugHelper_FormatNullable__1.htm)|
Форматирует значение в неизменном виде, если оно задано, или выполняя вывод
строки [NullText](F_Tessa_Platform_DebugHelper_NullText.htm), если значение
равно null.  
[GetTypeDisplayName](M_Tessa_Platform_DebugHelper_GetTypeDisplayName.htm)|
Возвращает имя типа, отформатированное для вывода в окне отладчика.  
[GetTypeName](M_Tessa_Platform_DebugHelper_GetTypeName.htm)|  Возвращает имя
типа, отформатированное для вывода в окне отладчика.  
## __Поля
[NullText](F_Tessa_Platform_DebugHelper_NullText.htm)|  Строка, отображаемая
вместо значения null в методах FormatNullable.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
