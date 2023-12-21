# ICardStoreTaskExtension.StoreTaskBeforeRequest - метод
Действие, выполняемое при сохранении задания, которое включает в себя
создание, изменение, завершение и удаление.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task StoreTaskBeforeRequest(
    	ICardStoreTaskExtensionContext context
    )
VB __Копировать
     Function StoreTaskBeforeRequest ( 
    	context As ICardStoreTaskExtensionContext
    ) As Task
C++ __Копировать
    Task^ StoreTaskBeforeRequest(
    	ICardStoreTaskExtensionContext^ context
    )
F# __Копировать
     abstract StoreTaskBeforeRequest : 
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
