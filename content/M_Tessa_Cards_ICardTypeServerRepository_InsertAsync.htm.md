# ICardTypeServerRepository.InsertAsync - метод
Добавляет тип карточки.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task InsertAsync(
    	CardTypeRepositoryData cardType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function InsertAsync ( 
    	cardType As CardTypeRepositoryData,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ InsertAsync(
    	CardTypeRepositoryData^ cardType, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract InsertAsync : 
            cardType : CardTypeRepositoryData * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cardType [CardTypeRepositoryData](T_Tessa_Cards_CardTypeRepositoryData.htm)
    Объект, описывающий тип карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardTypeServerRepository - ](T_Tessa_Cards_ICardTypeServerRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
