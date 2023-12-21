# CardMetadata.GetEnumerationsAsync - метод
Возвращает список перечислений.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<CardMetadataEnumerationCollection> GetEnumerationsAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetEnumerationsAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardMetadataEnumerationCollection)
C++ __Копировать
     public:
    virtual ValueTask<CardMetadataEnumerationCollection^> GetEnumerationsAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetEnumerationsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardMetadataEnumerationCollection> 
    override GetEnumerationsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardMetadataEnumerationCollection> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardMetadataEnumerationCollection](T_Tessa_Cards_Metadata_CardMetadataEnumerationCollection.htm)>  
Возвращаемое значение.
#### Реализации
[ICardMetadata.GetEnumerationsAsync(CancellationToken)](M_Tessa_Cards_ICardMetadata_GetEnumerationsAsync.htm)  
##  __См. также
#### Ссылки
[CardMetadata - ](T_Tessa_Cards_Metadata_CardMetadata.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
