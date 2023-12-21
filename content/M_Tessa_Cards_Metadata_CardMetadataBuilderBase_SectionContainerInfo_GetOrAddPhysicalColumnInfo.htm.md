# CardMetadataBuilderBase.SectionContainerInfo.GetOrAddPhysicalColumnInfo -
метод
Возвращает информацию о физической колонке с заданным идентификатором, если
такая колонка не существует, добавляет ее.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataBuilderBase.ColumnContainerInfo GetOrAddPhysicalColumnInfo(
    	Guid columnID
    )
VB __Копировать
     Public Function GetOrAddPhysicalColumnInfo ( 
    	columnID As Guid
    ) As CardMetadataBuilderBase.ColumnContainerInfo
C++ __Копировать
     public:
    CardMetadataBuilderBase.ColumnContainerInfo^ GetOrAddPhysicalColumnInfo(
    	Guid columnID
    )
F# __Копировать
     member GetOrAddPhysicalColumnInfo : 
            columnID : Guid -> CardMetadataBuilderBase.ColumnContainerInfo 
#### Параметры
columnID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор физической колонки, информацию о которой требуется вернуть.
#### Возвращаемое значение
[CardMetadataBuilderBase.ColumnContainerInfo](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_ColumnContainerInfo.htm)  
Информация о физической колонке.
##  __См. также
#### Ссылки
[CardMetadataBuilderBase.SectionContainerInfo -
](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_SectionContainerInfo.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
