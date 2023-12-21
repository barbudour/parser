# CardNewGetExtension.AfterRequest(ICardGetExtensionContext) - метод
Действие, выполняемое после получения карточки как при успешном, так и при
неудачном результате.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task AfterRequest(
    	ICardGetExtensionContext context
    )
VB __Копировать
     Public Overridable Function AfterRequest ( 
    	context As ICardGetExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequest(
    	ICardGetExtensionContext^ context
    )
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
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardNewGetExtension - ](T_Tessa_Cards_Extensions_CardNewGetExtension.htm)
[AfterRequest -
перегрузка](Overload_Tessa_Cards_Extensions_CardNewGetExtension_AfterRequest.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
