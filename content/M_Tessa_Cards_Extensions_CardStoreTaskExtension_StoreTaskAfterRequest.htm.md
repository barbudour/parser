# CardStoreTaskExtension.StoreTaskAfterRequest - метод
Действие, выполняемое после сохранения задания, которое включает в себя
создание, изменение, завершение и удаление. Метод выполняется всегда, если был
выполнен метод
[Tessa.Cards.Extensions.ICardStoreTaskExtension.StoreTaskBeforeRequest].
Проверить, было ли сохранение задания успешным, можно, обратившись к свойству
[Tessa.Cards.Extensions.ICardExtensionContext.RequestIsSuccessful].
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task StoreTaskAfterRequest(
    	ICardStoreTaskExtensionContext context
    )
VB __Копировать
     Public Overridable Function StoreTaskAfterRequest ( 
    	context As ICardStoreTaskExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ StoreTaskAfterRequest(
    	ICardStoreTaskExtensionContext^ context
    )
F# __Копировать
     abstract StoreTaskAfterRequest : 
            context : ICardStoreTaskExtensionContext -> Task 
    override StoreTaskAfterRequest : 
            context : ICardStoreTaskExtensionContext -> Task 
#### Параметры
context
[ICardStoreTaskExtensionContext](T_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext.htm)
    Контекст процесса сохранения задания.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreTaskExtension.StoreTaskAfterRequest(ICardStoreTaskExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreTaskExtension_StoreTaskAfterRequest.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardStoreTaskExtension -
](T_Tessa_Cards_Extensions_CardStoreTaskExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
