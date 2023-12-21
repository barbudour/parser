# CardMetadataBuilderBase.SectionContainerInfo.TryGetPhysicalColumnInfo -
метод
Возвращает информацию о физической колонке с заданным идентификатором или
false, если информация отсутствует.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool TryGetPhysicalColumnInfo(
    	Guid columnID,
    	out CardMetadataBuilderBase.ColumnContainerInfo info
    )
VB __Копировать
     Public Function TryGetPhysicalColumnInfo ( 
    	columnID As Guid,
    	<OutAttribute> ByRef info As CardMetadataBuilderBase.ColumnContainerInfo
    ) As Boolean
C++ __Копировать
     public:
    bool TryGetPhysicalColumnInfo(
    	Guid columnID, 
    	[OutAttribute] CardMetadataBuilderBase.ColumnContainerInfo^% info
    )
F# __Копировать
     member TryGetPhysicalColumnInfo : 
            columnID : Guid * 
            info : CardMetadataBuilderBase.ColumnContainerInfo byref -> bool 
#### Параметры
columnID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор физической колонки, информацию о котором требуется вернуть.
info
[CardMetadataBuilderBase.ColumnContainerInfo](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_ColumnContainerInfo.htm)
    Информация о физической колонке, доступная в случае, если метод вернул true.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если информация о физической колонке присутствует в объекте и была
возвращена в параметре info; false в противном случае.
## __См. также
#### Ссылки
[CardMetadataBuilderBase.SectionContainerInfo -
](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_SectionContainerInfo.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
