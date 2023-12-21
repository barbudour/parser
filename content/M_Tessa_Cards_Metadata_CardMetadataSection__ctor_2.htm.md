# CardMetadataSection(CardMetadataSection,
IReadOnlyCollection<CardMetadataColumn>) - конструктор
Создаёт экземпляр класса с указанием копируемого объекта и списка колонок.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataSection(
    	CardMetadataSection section,
    	IReadOnlyCollection<CardMetadataColumn> columns
    )
VB __Копировать
     Public Sub New ( 
    	section As CardMetadataSection,
    	columns As IReadOnlyCollection(Of CardMetadataColumn)
    )
C++ __Копировать
     public:
    CardMetadataSection(
    	CardMetadataSection^ section, 
    	IReadOnlyCollection<CardMetadataColumn^>^ columns
    )
F# __Копировать
     new : 
            section : CardMetadataSection * 
            columns : IReadOnlyCollection<CardMetadataColumn> -> CardMetadataSection
#### Параметры
section [CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
     Объект, для которого создаётся полная копия, за исключением списка колонок. 
columns
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)>
    Список колонок в секции.
##  __См. также
#### Ссылки
[CardMetadataSection - ](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
[CardMetadataSection -
перегрузка](Overload_Tessa_Cards_Metadata_CardMetadataSection__ctor.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
