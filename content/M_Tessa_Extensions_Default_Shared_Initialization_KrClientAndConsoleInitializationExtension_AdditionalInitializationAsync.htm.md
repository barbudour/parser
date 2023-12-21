# KrClientAndConsoleInitializationExtension.AdditionalInitializationAsync -
метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Initialization](N_Tessa_Extensions_Default_Shared_Initialization.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task AdditionalInitializationAsync(
    	Guid[] unavailableTypes,
    	ListStorage<KrDocType> docTypes,
    	CancellationToken cancellationToken
    )
VB __Копировать
     Protected Overridable Function AdditionalInitializationAsync ( 
    	unavailableTypes As Guid(),
    	docTypes As ListStorage(Of KrDocType),
    	cancellationToken As CancellationToken
    ) As Task
C++ __Копировать
     protected:
    virtual Task^ AdditionalInitializationAsync(
    	array<Guid>^ unavailableTypes, 
    	ListStorage<KrDocType^>^ docTypes, 
    	CancellationToken cancellationToken
    )
F# __Копировать
     abstract AdditionalInitializationAsync : 
            unavailableTypes : Guid[] * 
            docTypes : ListStorage<KrDocType> * 
            cancellationToken : CancellationToken -> Task 
    override AdditionalInitializationAsync : 
            unavailableTypes : Guid[] * 
            docTypes : ListStorage<KrDocType> * 
            cancellationToken : CancellationToken -> Task 
#### Параметры
unavailableTypes [Guid](https://learn.microsoft.com/dotnet/api/system.guid)[]
docTypes
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[KrDocType](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrDocType.htm)>
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[KrClientAndConsoleInitializationExtension -
](T_Tessa_Extensions_Default_Shared_Initialization_KrClientAndConsoleInitializationExtension.htm)
[Tessa.Extensions.Default.Shared.Initialization - пространство
имён](N_Tessa_Extensions_Default_Shared_Initialization.htm)
