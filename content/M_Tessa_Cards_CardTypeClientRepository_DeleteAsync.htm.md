# CardTypeClientRepository.DeleteAsync - метод
Удаляет тип карточки с заданным идентификатором.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task DeleteAsync(
    	Guid cardTypeID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeleteAsync ( 
    	cardTypeID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ DeleteAsync(
    	Guid cardTypeID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DeleteAsync : 
            cardTypeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override DeleteAsync : 
            cardTypeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardTypeClientRepository.DeleteAsync(Guid,
CancellationToken)](M_Tessa_Cards_ICardTypeClientRepository_DeleteAsync.htm)  
##  __См. также
#### Ссылки
[CardTypeClientRepository - ](T_Tessa_Cards_CardTypeClientRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
