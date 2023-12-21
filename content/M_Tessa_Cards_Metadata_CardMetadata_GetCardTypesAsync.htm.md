# CardMetadata.GetCardTypesAsync - метод
Возвращает список типов карточек карточек.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<CardTypeCollection> GetCardTypesAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetCardTypesAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardTypeCollection)
C++ __Копировать
     public:
    virtual ValueTask<CardTypeCollection^> GetCardTypesAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetCardTypesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardTypeCollection> 
    override GetCardTypesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardTypeCollection> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardTypeCollection](T_Tessa_Cards_CardTypeCollection.htm)>  
Возвращаемое значение.
#### Реализации
[ICardMetadata.GetCardTypesAsync(CancellationToken)](M_Tessa_Cards_ICardMetadata_GetCardTypesAsync.htm)  
##  __См. также
#### Ссылки
[CardMetadata - ](T_Tessa_Cards_Metadata_CardMetadata.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
