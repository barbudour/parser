# CardSatelliteRepairExtension.AfterRequest - метод
Действие, выполняемое после исправления структуры карточки как при успешном,
так и при неудачном результате.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task AfterRequest(
    	ICardRepairExtensionContext context
    )
VB __Копировать
     Public Overrides Function AfterRequest ( 
    	context As ICardRepairExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequest(
    	ICardRepairExtensionContext^ context
    ) override
F# __Копировать
     abstract AfterRequest : 
            context : ICardRepairExtensionContext -> Task 
    override AfterRequest : 
            context : ICardRepairExtensionContext -> Task 
#### Параметры
context
[ICardRepairExtensionContext](T_Tessa_Cards_Extensions_ICardRepairExtensionContext.htm)
    Контекст процесса исправления структуры карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardRepairExtension.AfterRequest(ICardRepairExtensionContext)](M_Tessa_Cards_Extensions_ICardRepairExtension_AfterRequest.htm)  
##  __См. также
#### Ссылки
[CardSatelliteRepairExtension -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteRepairExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
