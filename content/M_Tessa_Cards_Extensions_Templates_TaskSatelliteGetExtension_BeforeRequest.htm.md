# TaskSatelliteGetExtension.BeforeRequest - метод
Действие, выполняемое перед получением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы получение карточки стандартными
средствами не выполнялось.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task BeforeRequest(
    	ICardGetExtensionContext context
    )
VB __Копировать
     Public Overrides Function BeforeRequest ( 
    	context As ICardGetExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ BeforeRequest(
    	ICardGetExtensionContext^ context
    ) override
F# __Копировать
     abstract BeforeRequest : 
            context : ICardGetExtensionContext -> Task 
    override BeforeRequest : 
            context : ICardGetExtensionContext -> Task 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст процесса получения карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardGetExtension.BeforeRequest(ICardGetExtensionContext)](M_Tessa_Cards_Extensions_ICardGetExtension_BeforeRequest.htm)  
##  __См. также
#### Ссылки
[TaskSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
