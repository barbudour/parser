# TaskSatelliteRestoreExtension.AfterBeginTransaction - метод
Действие, выполняемое перед коммитом транзакции.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task AfterBeginTransaction(
    	ICardDeleteExtensionContext context
    )
VB __Копировать
     Public Overrides Function AfterBeginTransaction ( 
    	context As ICardDeleteExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterBeginTransaction(
    	ICardDeleteExtensionContext^ context
    ) override
F# __Копировать
     abstract AfterBeginTransaction : 
            context : ICardDeleteExtensionContext -> Task 
    override AfterBeginTransaction : 
            context : ICardDeleteExtensionContext -> Task 
#### Параметры
context
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
    Контекст процесса удаления карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardDeleteExtension.AfterBeginTransaction(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_ICardDeleteExtension_AfterBeginTransaction.htm)  
##  __См. также
#### Ссылки
[TaskSatelliteRestoreExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteRestoreExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
