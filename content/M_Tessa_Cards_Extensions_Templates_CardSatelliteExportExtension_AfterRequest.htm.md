# CardSatelliteExportExtension.AfterRequest - метод
Действие, выполняемое после получения карточки как при успешном, так и при
неудачном результате.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task AfterRequest(
    	ICardGetExtensionContext context
    )
VB __Копировать
     Public Overrides Function AfterRequest ( 
    	context As ICardGetExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequest(
    	ICardGetExtensionContext^ context
    ) override
F# __Копировать
     abstract AfterRequest : 
            context : ICardGetExtensionContext -> Task 
    override AfterRequest : 
            context : ICardGetExtensionContext -> Task 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст процесса получения карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardGetExtension.AfterRequest(ICardGetExtensionContext)](M_Tessa_Cards_Extensions_ICardGetExtension_AfterRequest.htm)  
##  __См. также
#### Ссылки
[CardSatelliteExportExtension -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteExportExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
