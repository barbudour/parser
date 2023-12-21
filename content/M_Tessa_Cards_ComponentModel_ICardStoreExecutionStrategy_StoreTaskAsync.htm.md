# ICardStoreExecutionStrategy.StoreTaskAsync - метод
Выполняет сохранение задания. Возвращает список идентификаторов ролей заданий,
которые необходимо удалить, или null, если список пуст.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Task<List<Guid>> StoreTaskAsync(
    	CardStoreContext context,
    	CardTask task,
    	List<Guid> taskRolesToDelete
    )
VB __Копировать
     Function StoreTaskAsync ( 
    	context As CardStoreContext,
    	task As CardTask,
    	taskRolesToDelete As List(Of Guid)
    ) As Task(Of List(Of Guid))
C++ __Копировать
    Task<List<Guid>^>^ StoreTaskAsync(
    	CardStoreContext^ context, 
    	CardTask^ task, 
    	List<Guid>^ taskRolesToDelete
    )
F# __Копировать
     abstract StoreTaskAsync : 
            context : CardStoreContext * 
            task : CardTask * 
            taskRolesToDelete : List<Guid> -> Task<List<Guid>> 
#### Параметры
context [CardStoreContext](T_Tessa_Cards_ComponentModel_CardStoreContext.htm)
    Контекст операции по сохранению карточки, для которой назначено задание.
task [CardTask](T_Tessa_Cards_CardTask.htm)
    Сохраняемое задание.
taskRolesToDelete
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Список идентификаторов временных ролей, которые необходимо удалить, или null,
если список пуст.
## __См. также
#### Ссылки
[ICardStoreExecutionStrategy -
](T_Tessa_Cards_ComponentModel_ICardStoreExecutionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
