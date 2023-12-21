# MultitypeSatelliteDeleteExtension.BeforeRequest - метод
Действие, выполняемое перед удалением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы удаление карточки стандартными
средствами не выполнялось.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task BeforeRequest(
    	ICardDeleteExtensionContext context
    )
VB __Копировать
     Public Overrides Function BeforeRequest ( 
    	context As ICardDeleteExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ BeforeRequest(
    	ICardDeleteExtensionContext^ context
    ) override
F# __Копировать
     abstract BeforeRequest : 
            context : ICardDeleteExtensionContext -> Task 
    override BeforeRequest : 
            context : ICardDeleteExtensionContext -> Task 
#### Параметры
context
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
    Контекст процесса удаления карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardDeleteExtension.BeforeRequest(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_ICardDeleteExtension_BeforeRequest.htm)  
##  __См. также
#### Ссылки
[MultitypeSatelliteDeleteExtension -
](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
