# CardTaskDialogActionStoreExtension.StoreTaskBeforeRequest - метод
Действие, выполняемое при сохранении задания, которое включает в себя
создание, изменение, завершение и удаление.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task StoreTaskBeforeRequest(
    	ICardStoreTaskExtensionContext context
    )
VB __Копировать
     Public Overrides Function StoreTaskBeforeRequest ( 
    	context As ICardStoreTaskExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ StoreTaskBeforeRequest(
    	ICardStoreTaskExtensionContext^ context
    ) override
F# __Копировать
     abstract StoreTaskBeforeRequest : 
            context : ICardStoreTaskExtensionContext -> Task 
    override StoreTaskBeforeRequest : 
            context : ICardStoreTaskExtensionContext -> Task 
#### Параметры
context
[ICardStoreTaskExtensionContext](T_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext.htm)
    Контекст процесса сохранения задания.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreTaskExtension.StoreTaskBeforeRequest(ICardStoreTaskExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreTaskExtension_StoreTaskBeforeRequest.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardTaskDialogActionStoreExtension -
](T_Tessa_Extensions_Platform_Server_Cards_CardTaskDialogActionStoreExtension.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
