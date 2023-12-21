# CardStoreDeletionStrategy.DeleteAllSectionsAsync - метод
Удаляет данные из всех секций заданной карточки.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task DeleteAllSectionsAsync(
    	Guid cardID,
    	ICardMetadata typeMetadata,
    	IQueryExecutor executor,
    	IQueryBuilderFactory builderFactory,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeleteAllSectionsAsync ( 
    	cardID As Guid,
    	typeMetadata As ICardMetadata,
    	executor As IQueryExecutor,
    	builderFactory As IQueryBuilderFactory,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ DeleteAllSectionsAsync(
    	Guid cardID, 
    	ICardMetadata^ typeMetadata, 
    	IQueryExecutor^ executor, 
    	IQueryBuilderFactory^ builderFactory, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DeleteAllSectionsAsync : 
            cardID : Guid * 
            typeMetadata : ICardMetadata * 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override DeleteAllSectionsAsync : 
            cardID : Guid * 
            typeMetadata : ICardMetadata * 
            executor : IQueryExecutor * 
            builderFactory : IQueryBuilderFactory * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, для которой производится удаление данных из всех её секций.
typeMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация типа удаляемой карточки.
executor [IQueryExecutor](T_Tessa_Platform_Data_IQueryExecutor.htm)
    Объект, выполняющий SQL-команды по удалению секций.
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
[ICardStoreDeletionStrategy.DeleteAllSectionsAsync(Guid, ICardMetadata,
IQueryExecutor, IQueryBuilderFactory,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardStoreDeletionStrategy_DeleteAllSectionsAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreDeletionStrategy -
](T_Tessa_Cards_ComponentModel_CardStoreDeletionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
