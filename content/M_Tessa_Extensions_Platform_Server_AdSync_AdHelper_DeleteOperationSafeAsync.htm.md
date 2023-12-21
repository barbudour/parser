# AdHelper.DeleteOperationSafeAsync - метод
Безопасное удаление операции
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task DeleteOperationSafeAsync(
    	this IOperationRepository operationRepository,
    	Guid operationID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function DeleteOperationSafeAsync ( 
    	operationRepository As IOperationRepository,
    	operationID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task^ DeleteOperationSafeAsync(
    	IOperationRepository^ operationRepository, 
    	Guid operationID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member DeleteOperationSafeAsync : 
            operationRepository : IOperationRepository * 
            operationID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
operationRepository
[IOperationRepository](T_Tessa_Platform_Operations_IOperationRepository.htm)
    репозиторий операций
operationID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    ID операции
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IOperationRepository](T_Tessa_Platform_Operations_IOperationRepository.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[AdHelper - ](T_Tessa_Extensions_Platform_Server_AdSync_AdHelper.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
