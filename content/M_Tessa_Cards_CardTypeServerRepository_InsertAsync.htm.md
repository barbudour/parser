# CardTypeServerRepository.InsertAsync - метод
Добавляет тип карточки.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task InsertAsync(
    	CardTypeRepositoryData cardType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function InsertAsync ( 
    	cardType As CardTypeRepositoryData,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ InsertAsync(
    	CardTypeRepositoryData^ cardType, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract InsertAsync : 
            cardType : CardTypeRepositoryData * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override InsertAsync : 
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
#### Реализации
[ICardTypeServerRepository.InsertAsync(CardTypeRepositoryData,
CancellationToken)](M_Tessa_Cards_ICardTypeServerRepository_InsertAsync.htm)  
##  __См. также
#### Ссылки
[CardTypeServerRepository - ](T_Tessa_Cards_CardTypeServerRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
