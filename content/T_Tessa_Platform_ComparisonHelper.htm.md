# ComparisonHelper - класс
Хэлперы для сравнения значений и генерации хеш-кодов.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ComparisonHelper
VB __Копировать
     Public NotInheritable Class ComparisonHelper
C++ __Копировать
     public ref class ComparisonHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ComparisonHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ComparisonHelper
##  __Методы
[FuzzyEquals(DateTime, DateTime,
Nullable<TimeSpan>)](M_Tessa_Platform_ComparisonHelper_FuzzyEquals.htm)|
Возвращает признак равенства двух объектов
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime) с заданным
интервалом погрешности errorInterval. Часовой пояс указанных дат не
учитывается, т.е.
[Kind](https://learn.microsoft.com/dotnet/api/system.datetime.kind#system-
datetime-kind) игнорируется.  
---|---  
[FuzzyEquals(Nullable<DateTime>, Nullable<DateTime>,
Nullable<TimeSpan>)](M_Tessa_Platform_ComparisonHelper_FuzzyEquals_1.htm)|
Возвращает признак равенства двух объектов
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime) с заданным
интервалом погрешности errorInterval.  
[TruncateDateTime](M_Tessa_Platform_ComparisonHelper_TruncateDateTime.htm)|
Округляет DateTime до указанной точности  
[TryCompareForEqualityWithConversion](M_Tessa_Platform_ComparisonHelper_TryCompareForEqualityWithConversion.htm)|
Сравнивает объекты на равенство с учётом возможных преобразований типов.
Порядок переданных аргументов определяет порядок возможных преобразований
типов.  
[TryCompareWithConversion](M_Tessa_Platform_ComparisonHelper_TryCompareWithConversion.htm)|
Сравнивает объекты с учётом возможных преобразований типов. Для сравнения
используется интерфейс
[IComparable](https://learn.microsoft.com/dotnet/api/system.icomparable),
который должен быть реализован хотя бы одним из заданных объектов.
Порядок переданных аргументов определяет порядок возможных преобразований
типов.  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
