# CardTypeService.GetAllCardTypesAsync - метод
Возвращает объекты, описывающие типы всех карточек, со всей необходимой
информацией.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<List<CardType>> GetAllCardTypesAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetAllCardTypesAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of List(Of CardType))
C++ __Копировать
     public:
    virtual Task<List<CardType^>^>^ GetAllCardTypesAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetAllCardTypesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<List<CardType>> 
    override GetAllCardTypesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<List<CardType>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[CardType](T_Tessa_Cards_CardType.htm)>>  
Список объектов, описывающих типы карточек.
#### Реализации
[ICardTypeService.GetAllCardTypesAsync(CancellationToken)](M_Tessa_Cards_ICardTypeService_GetAllCardTypesAsync.htm)  
##  __См. также
#### Ссылки
[CardTypeService - ](T_Tessa_Cards_CardTypeService.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
