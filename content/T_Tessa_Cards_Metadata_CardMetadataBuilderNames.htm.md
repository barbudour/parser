# CardMetadataBuilderNames - класс
Имена, используемые для регистрации реализаций
[ICardMetadataBuilder](T_Tessa_Cards_Metadata_ICardMetadataBuilder.htm) в
Unity.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardMetadataBuilderNames
VB __Копировать
     Public NotInheritable Class CardMetadataBuilderNames
C++ __Копировать
     public ref class CardMetadataBuilderNames abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardMetadataBuilderNames = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardMetadataBuilderNames
##  __Поля
[AllTables](F_Tessa_Cards_Metadata_CardMetadataBuilderNames_AllTables.htm)|
Реализация, учитывающая построение метаинформации по всем таблицам, включая
те, которые не используются ни в одном типе карточек. Расширения не
используются.  
---|---  
[ByUsage](F_Tessa_Cards_Metadata_CardMetadataBuilderNames_ByUsage.htm)|
Реализация, учитывающая построение метаинформации по факту использования
таблиц и колонок в типах карточек. При построении используются расширения.  
[ByUsageWithoutExtensions](F_Tessa_Cards_Metadata_CardMetadataBuilderNames_ByUsageWithoutExtensions.htm)|
Реализация, учитывающая построение метаинформации по факту использования
таблиц и колонок в типах карточек и не использующая расширения.  
[Default](F_Tessa_Cards_Metadata_CardMetadataBuilderNames_Default.htm)|
Реализация по умолчанию. При построении используются расширения.  
[Dialog](F_Tessa_Cards_Metadata_CardMetadataBuilderNames_Dialog.htm)|
Реализация, учитывающая построение метаинформации по умолчанию для типов
карточек кроме [Dialog](T_Tessa_Cards_CardInstanceType.htm) и по виртуальной
схеме для типа [Dialog](T_Tessa_Cards_CardInstanceType.htm). Расширения не
используются.  
[WithoutExtensions](F_Tessa_Cards_Metadata_CardMetadataBuilderNames_WithoutExtensions.htm)|
Реализация по умолчанию, не использующая расширения.  
## __См. также
#### Ссылки
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
