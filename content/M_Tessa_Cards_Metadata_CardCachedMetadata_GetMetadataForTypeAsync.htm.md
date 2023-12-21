# CardCachedMetadata.GetMetadataForTypeAsync - метод
Возвращает выборку из метаинформации, которая относится только к заданному
типу карточек. В возвращённую выборку не передаются перечисления.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<ICardMetadata> GetMetadataForTypeAsync(
    	Guid cardTypeID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetMetadataForTypeAsync ( 
    	cardTypeID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ICardMetadata)
C++ __Копировать
     public:
    virtual ValueTask<ICardMetadata^> GetMetadataForTypeAsync(
    	Guid cardTypeID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetMetadataForTypeAsync : 
            cardTypeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICardMetadata> 
    override GetMetadataForTypeAsync : 
            cardTypeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICardMetadata> 
#### Параметры
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки, для которого строится выборка из метаинформации.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)>  
Выборка метаинформации, которая относится только к заданному типу карточки.
#### Реализации
[ICardMetadata.GetMetadataForTypeAsync(Guid,
CancellationToken)](M_Tessa_Cards_ICardMetadata_GetMetadataForTypeAsync.htm)  
##  __Заметки
Если текущий объект защищён от изменений методом
[Seal()](M_Tessa_Cards_Metadata_CardCachedMetadata_Seal.htm), то этот метод
использует кэш.
Метод является потокобезопасным.
##  __См. также
#### Ссылки
[CardCachedMetadata - ](T_Tessa_Cards_Metadata_CardCachedMetadata.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
