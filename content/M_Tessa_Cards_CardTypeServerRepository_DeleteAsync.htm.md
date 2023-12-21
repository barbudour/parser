# CardTypeServerRepository.DeleteAsync(IReadOnlyCollection<Guid>,
CancellationToken) - метод
Удаляет типы карточек с заданными идентификаторами.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task DeleteAsync(
    	IReadOnlyCollection<Guid> cardTypeIDList,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeleteAsync ( 
    	cardTypeIDList As IReadOnlyCollection(Of Guid),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ DeleteAsync(
    	IReadOnlyCollection<Guid>^ cardTypeIDList, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DeleteAsync : 
            cardTypeIDList : IReadOnlyCollection<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override DeleteAsync : 
            cardTypeIDList : IReadOnlyCollection<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cardTypeIDList
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификаторы типов карточек.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardTypeServerRepository.DeleteAsync(IReadOnlyCollection<Guid>,
CancellationToken)](M_Tessa_Cards_ICardTypeServerRepository_DeleteAsync.htm)  
##  __См. также
#### Ссылки
[CardTypeServerRepository - ](T_Tessa_Cards_CardTypeServerRepository.htm)
[DeleteAsync -
перегрузка](Overload_Tessa_Cards_CardTypeServerRepository_DeleteAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
