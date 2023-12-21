# TemplateRecordNewExtension.AfterRequest - метод
Действие, выполняемое после создания структуры карточки как при успешном, так
и при неудачном результате.
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task AfterRequest(
    	ICardNewExtensionContext context
    )
VB __Копировать
     Public Overrides Function AfterRequest ( 
    	context As ICardNewExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequest(
    	ICardNewExtensionContext^ context
    ) override
F# __Копировать
     abstract AfterRequest : 
            context : ICardNewExtensionContext -> Task 
    override AfterRequest : 
            context : ICardNewExtensionContext -> Task 
#### Параметры
context
[ICardNewExtensionContext](T_Tessa_Cards_Extensions_ICardNewExtensionContext.htm)
    Контекст процесса создания структуры карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardNewExtension.AfterRequest(ICardNewExtensionContext)](M_Tessa_Cards_Extensions_ICardNewExtension_AfterRequest.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[TemplateRecordNewExtension -
](T_Tessa_Extensions_Platform_Client_Cards_TemplateRecordNewExtension.htm)
[Tessa.Extensions.Platform.Client.Cards - пространство
имён](N_Tessa_Extensions_Platform_Client_Cards.htm)
