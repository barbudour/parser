# CardFileSourceMapping.CreateContentSource - метод
Создаёт источник контента файла, который можно использовать в отображении без
потерь в производительности.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardFileContentSource CreateContentSource(
    	Guid cardID,
    	Guid cardTypeID,
    	Guid fileID,
    	Guid versionRowID,
    	CardFileSourceType storeSource,
    	Guid? originalVersionRowID = null
    )
VB __Копировать
     Public Function CreateContentSource ( 
    	cardID As Guid,
    	cardTypeID As Guid,
    	fileID As Guid,
    	versionRowID As Guid,
    	storeSource As CardFileSourceType,
    	Optional originalVersionRowID As Guid? = Nothing
    ) As ICardFileContentSource
C++ __Копировать
     public:
    virtual ICardFileContentSource^ CreateContentSource(
    	Guid cardID, 
    	Guid cardTypeID, 
    	Guid fileID, 
    	Guid versionRowID, 
    	CardFileSourceType storeSource, 
    	Nullable<Guid> originalVersionRowID = nullptr
    ) sealed
F# __Копировать
     abstract CreateContentSource : 
            cardID : Guid * 
            cardTypeID : Guid * 
            fileID : Guid * 
            versionRowID : Guid * 
            storeSource : CardFileSourceType * 
            ?originalVersionRowID : Nullable<Guid> 
    (* Defaults:
            let _originalVersionRowID = defaultArg originalVersionRowID null
    *)
    -> ICardFileContentSource 
    override CreateContentSource : 
            cardID : Guid * 
            cardTypeID : Guid * 
            fileID : Guid * 
            versionRowID : Guid * 
            storeSource : CardFileSourceType * 
            ?originalVersionRowID : Nullable<Guid> 
    (* Defaults:
            let _originalVersionRowID = defaultArg originalVersionRowID null
    *)
    -> ICardFileContentSource 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки.
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки.
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла.
versionRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор версии файла.
storeSource [CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm)
    Местоположение контента файла.
originalVersionRowID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Идентификатор исходной версии файла, к которой относится источник контента, или null, если источник относится к любой из версий. 
#### Возвращаемое значение
[ICardFileContentSource](T_Tessa_Cards_ICardFileContentSource.htm)  
Созданный источник контента файла, который можно использовать в отображении
без потерь в производительности.
#### Реализации
[ICardFileSourceMapping.CreateContentSource(Guid, Guid, Guid, Guid,
CardFileSourceType,
Nullable<Guid>)](M_Tessa_Cards_ICardFileSourceMapping_CreateContentSource.htm)  
##  __См. также
#### Ссылки
[CardFileSourceMapping - ](T_Tessa_Cards_CardFileSourceMapping.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
