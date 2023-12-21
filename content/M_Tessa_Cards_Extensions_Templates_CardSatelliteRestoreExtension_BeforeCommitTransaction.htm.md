# CardSatelliteRestoreExtension.BeforeCommitTransaction - метод
##  __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task BeforeCommitTransaction(
    	ICardDeleteExtensionContext context
    )
VB __Копировать
     Public Overrides Function BeforeCommitTransaction ( 
    	context As ICardDeleteExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ BeforeCommitTransaction(
    	ICardDeleteExtensionContext^ context
    ) override
F# __Копировать
     abstract BeforeCommitTransaction : 
            context : ICardDeleteExtensionContext -> Task 
    override BeforeCommitTransaction : 
            context : ICardDeleteExtensionContext -> Task 
#### Параметры
context
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ICardDeleteExtension.BeforeCommitTransaction(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_ICardDeleteExtension_BeforeCommitTransaction.htm)  
##  __См. также
#### Ссылки
[CardSatelliteRestoreExtension -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteRestoreExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
