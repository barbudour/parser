# ConversionHelper - класс
Вспомогательные методы для преобразования типов.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ConversionHelper
VB __Копировать
     Public NotInheritable Class ConversionHelper
C++ __Копировать
     public ref class ConversionHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ConversionHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConversionHelper
##  __Методы
[ParseEnum<T>](M_Tessa_Platform_ConversionHelper_ParseEnum__1.htm)|
Возвращает преобразованное значение параметра value из строки, числа или
значения перечисления в перечисление типа T.  
---|---  
[ToGuidArray](M_Tessa_Platform_ConversionHelper_ToGuidArray.htm)|  Преобразует
строку, полученную вызовом метода
[ToString(IList<Guid>)](M_Tessa_Platform_ConversionHelper_ToString.htm), в
массив [Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
[ToString](M_Tessa_Platform_ConversionHelper_ToString.htm)|  Преобразует
список [Guid](https://learn.microsoft.com/dotnet/api/system.guid) в строку
текста.  
[TryConvert](M_Tessa_Platform_ConversionHelper_TryConvert.htm)|  Метод
пытается преобразовать объект convertibleObject в объект типа conversionType.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
