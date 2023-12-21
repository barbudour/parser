# CardWithoutLockingStrategy.ReleaseWriterLockAsync - метод
Выполняет снятие блокировки на запись карточки.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task ReleaseWriterLockAsync(
    	Guid cardID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ReleaseWriterLockAsync ( 
    	cardID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ ReleaseWriterLockAsync(
    	Guid cardID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ReleaseWriterLockAsync : 
            cardID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override ReleaseWriterLockAsync : 
            cardID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, для которой снимается блокировка.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardLockingStrategy.ReleaseWriterLockAsync(Guid,
CancellationToken)](M_Tessa_Cards_ICardLockingStrategy_ReleaseWriterLockAsync.htm)  
##  __См. также
#### Ссылки
[CardWithoutLockingStrategy - ](T_Tessa_Cards_CardWithoutLockingStrategy.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
