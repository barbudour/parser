# ICardContentStrategy.CleanFileAsync - метод
Очищает место, отведённое для контента файла. Метод вызывается перед удалением
файла.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task CleanFileAsync(
    	Guid cardID,
    	Guid fileID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function CleanFileAsync ( 
    	cardID As Guid,
    	fileID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ CleanFileAsync(
    	Guid cardID, 
    	Guid fileID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CleanFileAsync : 
            cardID : Guid * 
            fileID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, место для контента файла которой требуется очистить.
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла, место для контента которого требуется очистить.
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
