# CardStoreStrategy.UpdateTimeZoneTaskInfoAsync - метод
Заполняет в заданиях информацию по временныс зонам.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task UpdateTimeZoneTaskInfoAsync(
    	IEnumerable<CardTask> tasks,
    	DbManager db,
    	IQueryBuilderFactory builderFactory,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function UpdateTimeZoneTaskInfoAsync ( 
    	tasks As IEnumerable(Of CardTask),
    	db As DbManager,
    	builderFactory As IQueryBuilderFactory,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ UpdateTimeZoneTaskInfoAsync(
    	IEnumerable<CardTask^>^ tasks, 
    	DbManager^ db, 
    	IQueryBuilderFactory^ builderFactory, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract UpdateTimeZoneTaskInfoAsync : 
            tasks : IEnumerable<CardTask> * 
            db : DbManager * 
            builderFactory : IQueryBuilderFactory * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override UpdateTimeZoneTaskInfoAsync : 
            tasks : IEnumerable<CardTask> * 
            db : DbManager * 
            builderFactory : IQueryBuilderFactory * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
tasks
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardTask](T_Tessa_Cards_CardTask.htm)>
    Сохраняемые задания.
db [DbManager](T_Tessa_Platform_Data_DbManager.htm)
    Объект, посредством которого осуществляется взаимодействие с базой данных.
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
    Объект для генерации текста запросов.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreStrategy.UpdateTimeZoneTaskInfoAsync(IEnumerable<CardTask>,
DbManager, IQueryBuilderFactory,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_UpdateTimeZoneTaskInfoAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreStrategy - ](T_Tessa_Cards_ComponentModel_CardStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
