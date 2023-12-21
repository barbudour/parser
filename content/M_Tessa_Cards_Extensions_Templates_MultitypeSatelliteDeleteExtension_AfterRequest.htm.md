# MultitypeSatelliteDeleteExtension.AfterRequest - метод
Действие, выполняемое после удаления карточки как при успешном, так и при
неудачном результате.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task AfterRequest(
    	ICardDeleteExtensionContext context
    )
VB __Копировать
     Public Overrides Function AfterRequest ( 
    	context As ICardDeleteExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequest(
    	ICardDeleteExtensionContext^ context
    ) override
F# __Копировать
     abstract AfterRequest : 
            context : ICardDeleteExtensionContext -> Task 
    override AfterRequest : 
            context : ICardDeleteExtensionContext -> Task 
#### Параметры
context
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
    Контекст процесса удаления карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardDeleteExtension.AfterRequest(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_ICardDeleteExtension_AfterRequest.htm)  
##  __См. также
#### Ссылки
[MultitypeSatelliteDeleteExtension -
](T_Tessa_Cards_Extensions_Templates_MultitypeSatelliteDeleteExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
