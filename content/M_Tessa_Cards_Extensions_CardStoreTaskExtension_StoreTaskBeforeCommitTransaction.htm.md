# CardStoreTaskExtension.StoreTaskBeforeCommitTransaction - метод
Действие, выполняемое перед завершением транзакции на сохранение задания,
которое включает в себя создание, изменение, завершение и удаление. Метод
выполняется всегда, если был выполнен метод
[Tessa.Cards.Extensions.ICardStoreTaskExtension.StoreTaskBeforeRequest].
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task StoreTaskBeforeCommitTransaction(
    	ICardStoreTaskExtensionContext context
    )
VB __Копировать
     Public Overridable Function StoreTaskBeforeCommitTransaction ( 
    	context As ICardStoreTaskExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ StoreTaskBeforeCommitTransaction(
    	ICardStoreTaskExtensionContext^ context
    )
F# __Копировать
     abstract StoreTaskBeforeCommitTransaction : 
            context : ICardStoreTaskExtensionContext -> Task 
    override StoreTaskBeforeCommitTransaction : 
            context : ICardStoreTaskExtensionContext -> Task 
#### Параметры
context
[ICardStoreTaskExtensionContext](T_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext.htm)
    Контекст процесса сохранения задания.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreTaskExtension.StoreTaskBeforeCommitTransaction(ICardStoreTaskExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreTaskExtension_StoreTaskBeforeCommitTransaction.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardStoreTaskExtension -
](T_Tessa_Cards_Extensions_CardStoreTaskExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
