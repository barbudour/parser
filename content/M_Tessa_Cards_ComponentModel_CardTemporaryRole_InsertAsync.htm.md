# CardTemporaryRole.InsertAsync - метод
Создаёт временную роль.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task InsertAsync(
    	IDbScope dbScope,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function InsertAsync ( 
    	dbScope As IDbScope,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ InsertAsync(
    	IDbScope^ dbScope, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract InsertAsync : 
            dbScope : IDbScope * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override InsertAsync : 
            dbScope : IDbScope * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
     Объект, выполняющий SQL-команды. Не может быть равен null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardTemporaryRole.InsertAsync(IDbScope,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardTemporaryRole_InsertAsync.htm)  
##  __См. также
#### Ссылки
[CardTemporaryRole - ](T_Tessa_Cards_ComponentModel_CardTemporaryRole.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
