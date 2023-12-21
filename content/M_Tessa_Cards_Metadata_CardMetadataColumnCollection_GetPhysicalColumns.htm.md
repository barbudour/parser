# CardMetadataColumnCollection.GetPhysicalColumns - метод
Возвращает список физических колонок, которые включены в заданную комплексную
колонку.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IEnumerable<CardMetadataColumn> GetPhysicalColumns(
    	CardMetadataColumn complexColumn
    )
VB __Копировать
     Public Function GetPhysicalColumns ( 
    	complexColumn As CardMetadataColumn
    ) As IEnumerable(Of CardMetadataColumn)
C++ __Копировать
     public:
    IEnumerable<CardMetadataColumn^>^ GetPhysicalColumns(
    	CardMetadataColumn^ complexColumn
    )
F# __Копировать
     member GetPhysicalColumns : 
            complexColumn : CardMetadataColumn -> IEnumerable<CardMetadataColumn> 
#### Параметры
complexColumn
[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
    Комплексная колонка.
#### Возвращаемое значение
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)>  
Список физических колонок, которые включены в заданную комплексную колонку.
##  __См. также
#### Ссылки
[CardMetadataColumnCollection -
](T_Tessa_Cards_Metadata_CardMetadataColumnCollection.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
