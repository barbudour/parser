# ICardTypeServerRepository.CardTypeExistsAsync - метод
Возвращает признак того, что тип карточки с заданным идентификатором
существует.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<bool> CardTypeExistsAsync(
    	Guid cardTypeID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function CardTypeExistsAsync ( 
    	cardTypeID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
    Task<bool>^ CardTypeExistsAsync(
    	Guid cardTypeID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CardTypeExistsAsync : 
            cardTypeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки, существование которого требуется проверить.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если тип карточки существует; false в противном случае.
## __См. также
#### Ссылки
[ICardTypeServerRepository - ](T_Tessa_Cards_ICardTypeServerRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
