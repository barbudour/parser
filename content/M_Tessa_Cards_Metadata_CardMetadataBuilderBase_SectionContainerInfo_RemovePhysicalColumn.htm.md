# CardMetadataBuilderBase.SectionContainerInfo.RemovePhysicalColumn - метод
Удаляет информацию о физической колонке с заданным идентификатором.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void RemovePhysicalColumn(
    	Guid columnID
    )
VB __Копировать
     Public Sub RemovePhysicalColumn ( 
    	columnID As Guid
    )
C++ __Копировать
     public:
    void RemovePhysicalColumn(
    	Guid columnID
    )
F# __Копировать
     member RemovePhysicalColumn : 
            columnID : Guid -> unit 
#### Параметры
columnID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор физической колонки, информацию о которой требуется удалить.
##  __Заметки
Если информация о колонке отсутствовала в объекте, то действий не
производится.
## __См. также
#### Ссылки
[CardMetadataBuilderBase.SectionContainerInfo -
](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_SectionContainerInfo.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
