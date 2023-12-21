# CardCachedMetadata.GetCachedMetadataAsync - метод
Возвращает исходный объект метаинформации, который кэшируется текущим
объектом.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<ICardMetadata> GetCachedMetadataAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetCachedMetadataAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ICardMetadata)
C++ __Копировать
     public:
    virtual ValueTask<ICardMetadata^> GetCachedMetadataAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetCachedMetadataAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICardMetadata> 
    override GetCachedMetadataAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICardMetadata> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)>  
Исходный объект метаинформации, который кэшируется текущим объектом.
#### Реализации
[ICardCachedMetadata.GetCachedMetadataAsync(CancellationToken)](M_Tessa_Cards_ICardCachedMetadata_GetCachedMetadataAsync.htm)  
##  __См. также
#### Ссылки
[CardCachedMetadata - ](T_Tessa_Cards_Metadata_CardCachedMetadata.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
