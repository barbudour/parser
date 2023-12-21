# ICardStoreTaskExtension.StoreTaskAfterBeginTransaction - метод
Действие, выполняемое после начала транзакции на сохранение задания, которое
включает в себя создание, изменение, завершение и удаление. Метод выполняется
всегда, если был выполнен метод
[Tessa.Cards.Extensions.ICardStoreTaskExtension.StoreTaskBeforeRequest].
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task StoreTaskAfterBeginTransaction(
    	ICardStoreTaskExtensionContext context
    )
VB __Копировать
     Function StoreTaskAfterBeginTransaction ( 
    	context As ICardStoreTaskExtensionContext
    ) As Task
C++ __Копировать
    Task^ StoreTaskAfterBeginTransaction(
    	ICardStoreTaskExtensionContext^ context
    )
F# __Копировать
     abstract StoreTaskAfterBeginTransaction : 
            context : ICardStoreTaskExtensionContext -> Task 
#### Параметры
context
[ICardStoreTaskExtensionContext](T_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext.htm)
    Контекст процесса сохранения задания.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardStoreTaskExtension -
](T_Tessa_Cards_Extensions_ICardStoreTaskExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
