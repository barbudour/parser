# ICardContentStrategy.CleanCardAsync - метод
Очищает место, отведённое для контента файлов, принадлежащих карточке. Метод
вызывается перед удалением карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task CleanCardAsync(
    	Guid cardID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function CleanCardAsync ( 
    	cardID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ CleanCardAsync(
    	Guid cardID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CleanCardAsync : 
            cardID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, место для контента файлов которой требуется очистить.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardContentStrategy -
](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
