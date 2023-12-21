# CardTypeServerRepository.UpdateAsync - метод
Обновляет имя и метаданные типа карточки с идентификатором
[Tessa.Cards.CardTypeRepositoryData.ID].
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task UpdateAsync(
    	CardTypeRepositoryData cardType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function UpdateAsync ( 
    	cardType As CardTypeRepositoryData,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ UpdateAsync(
    	CardTypeRepositoryData^ cardType, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract UpdateAsync : 
            cardType : CardTypeRepositoryData * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override UpdateAsync : 
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
[ICardTypeServerRepository.UpdateAsync(CardTypeRepositoryData,
CancellationToken)](M_Tessa_Cards_ICardTypeServerRepository_UpdateAsync.htm)  
##  __См. также
#### Ссылки
[CardTypeServerRepository - ](T_Tessa_Cards_CardTypeServerRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
