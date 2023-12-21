# CardLockingStrategy.ReleaseReaderLockCoreAsync - метод
Выполняет снятие блокировки на чтение карточки.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task ReleaseReaderLockCoreAsync(
    	Guid cardID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function ReleaseReaderLockCoreAsync ( 
    	cardID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     protected:
    virtual Task^ ReleaseReaderLockCoreAsync(
    	Guid cardID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ReleaseReaderLockCoreAsync : 
            cardID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override ReleaseReaderLockCoreAsync : 
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
##  __См. также
#### Ссылки
[CardLockingStrategy - ](T_Tessa_Cards_CardLockingStrategy.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
