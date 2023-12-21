# ICardStoreStrategy.UpdateOriginalTaskInfoAsync - метод
Заполняет в заданиях информацию по текущим ролям, на которые были назначены
задания, из базы данных, если это актуально для текущего сохранения (например,
если роль изменяется в процессе сохранения).
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task UpdateOriginalTaskInfoAsync(
    	IEnumerable<CardTask> tasks,
    	DbManager db,
    	IQueryBuilderFactory builderFactory,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function UpdateOriginalTaskInfoAsync ( 
    	tasks As IEnumerable(Of CardTask),
    	db As DbManager,
    	builderFactory As IQueryBuilderFactory,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ UpdateOriginalTaskInfoAsync(
    	IEnumerable<CardTask^>^ tasks, 
    	DbManager^ db, 
    	IQueryBuilderFactory^ builderFactory, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract UpdateOriginalTaskInfoAsync : 
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
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardStoreStrategy - ](T_Tessa_Cards_ComponentModel_ICardStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
