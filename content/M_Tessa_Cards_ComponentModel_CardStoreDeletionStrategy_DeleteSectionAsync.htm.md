# CardStoreDeletionStrategy.DeleteSectionAsync - метод
Удаляет данные из указанной секции заданной карточки.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task DeleteSectionAsync(
    	Guid cardID,
    	string sectionName,
    	IQueryExecutor executor,
    	IQueryBuilderFactory builderFactory,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeleteSectionAsync ( 
    	cardID As Guid,
    	sectionName As String,
    	executor As IQueryExecutor,
    	builderFactory As IQueryBuilderFactory,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ DeleteSectionAsync(
    	Guid cardID, 
    	String^ sectionName, 
    	IQueryExecutor^ executor, 
    	IQueryBuilderFactory^ builderFactory, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DeleteSectionAsync : 
            cardID : Guid * 
            sectionName : string * 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override DeleteSectionAsync : 
            cardID : Guid * 
            sectionName : string * 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, для которой производится удаление данных из заданной секции.
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции, из которой производится удаление.
executor [IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm)
    Объект, выполняющий SQL-команды по удалению секции.
builderFactory
[IQueryBuilderFactory](T_Tessa_Platform_Data_IQueryBuilderFactory.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreDeletionStrategy.DeleteSectionAsync(Guid, String, IQueryExecutor,
IQueryBuilderFactory,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStoreDeletionStrategy_DeleteSectionAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreDeletionStrategy -
](T_Tessa_Cards_ComponentModel_CardStoreDeletionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
