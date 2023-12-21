# ICardTypeServerRepository.GetAllCardTypesAsync - метод
Возвращает объекты, описывающие типы всех карточек, со всей необходимой
информацией.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Task<List<CardTypeRepositoryData>> GetAllCardTypesAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetAllCardTypesAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of List(Of CardTypeRepositoryData))
C++ __Копировать
    Task<List<CardTypeRepositoryData^>^>^ GetAllCardTypesAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetAllCardTypesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<List<CardTypeRepositoryData>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[CardTypeRepositoryData](T_Tessa_Cards_CardTypeRepositoryData.htm)>>  
Список объектов, описывающих типы карточек.
##  __См. также
#### Ссылки
[ICardTypeServerRepository - ](T_Tessa_Cards_ICardTypeServerRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
