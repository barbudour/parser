# CardNewGetExtension.AfterRequest(ICardNewExtensionContext) - метод
Действие, выполняемое после создания структуры карточки как при успешном, так
и при неудачном результате.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task AfterRequest(
    	ICardNewExtensionContext context
    )
VB __Копировать
     Public Overridable Function AfterRequest ( 
    	context As ICardNewExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequest(
    	ICardNewExtensionContext^ context
    )
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
[CardNewGetExtension - ](T_Tessa_Cards_Extensions_CardNewGetExtension.htm)
[AfterRequest -
перегрузка](Overload_Tessa_Cards_Extensions_CardNewGetExtension_AfterRequest.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
