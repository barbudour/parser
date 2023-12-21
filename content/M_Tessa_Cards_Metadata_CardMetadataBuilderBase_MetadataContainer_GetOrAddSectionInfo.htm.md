# CardMetadataBuilderBase.MetadataContainer.GetOrAddSectionInfo - метод
Возвращает собранную информацию по секции с заданным идентификатором, если
информация по секции с таким идентификатором не найдена, то создает ее.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataBuilderBase.SectionContainerInfo GetOrAddSectionInfo(
    	Guid sectionID
    )
VB __Копировать
     Public Function GetOrAddSectionInfo ( 
    	sectionID As Guid
    ) As CardMetadataBuilderBase.SectionContainerInfo
C++ __Копировать
     public:
    CardMetadataBuilderBase.SectionContainerInfo^ GetOrAddSectionInfo(
    	Guid sectionID
    )
F# __Копировать
     member GetOrAddSectionInfo : 
            sectionID : Guid -> CardMetadataBuilderBase.SectionContainerInfo 
#### Параметры
sectionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор секции.
#### Возвращаемое значение
[CardMetadataBuilderBase.SectionContainerInfo](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_SectionContainerInfo.htm)  
Собранная информация по секции.
##  __См. также
#### Ссылки
[CardMetadataBuilderBase.MetadataContainer -
](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
