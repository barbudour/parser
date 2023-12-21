# AutoStartTaskRollbackStoreExtension.AfterRequestFinally - метод
Действие, выполняемое при возникновении исключения или после сохранения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task AfterRequestFinally(
    	ICardStoreExtensionContext context
    )
VB __Копировать
     Public Overrides Function AfterRequestFinally ( 
    	context As ICardStoreExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequestFinally(
    	ICardStoreExtensionContext^ context
    ) override
F# __Копировать
     abstract AfterRequestFinally : 
            context : ICardStoreExtensionContext -> Task 
    override AfterRequestFinally : 
            context : ICardStoreExtensionContext -> Task 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
    Контекст процесса сохранения карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreExtension.AfterRequestFinally(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_AfterRequestFinally.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[AutoStartTaskRollbackStoreExtension -
](T_Tessa_Extensions_Platform_Server_Cards_AutoStartTaskRollbackStoreExtension.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
