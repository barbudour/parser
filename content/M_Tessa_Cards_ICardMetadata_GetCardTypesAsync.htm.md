# ICardMetadata.GetCardTypesAsync - метод
Возвращает список типов карточек карточек.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<CardTypeCollection> GetCardTypesAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetCardTypesAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardTypeCollection)
C++ __Копировать
     ValueTask<CardTypeCollection^> GetCardTypesAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetCardTypesAsync : 
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
##  __См. также
#### Ссылки
[ICardMetadata - ](T_Tessa_Cards_ICardMetadata.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
