# CardGetFileVersionsExtension.AfterRequest - метод
Действие, выполняемое после получения версий файла как при успешном, так и при
неудачном результате.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task AfterRequest(
    	ICardGetFileVersionsExtensionContext context
    )
VB __Копировать
     Public Overridable Function AfterRequest ( 
    	context As ICardGetFileVersionsExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequest(
    	ICardGetFileVersionsExtensionContext^ context
    )
F# __Копировать
     abstract AfterRequest : 
            context : ICardGetFileVersionsExtensionContext -> Task 
    override AfterRequest : 
            context : ICardGetFileVersionsExtensionContext -> Task 
#### Параметры
context
[ICardGetFileVersionsExtensionContext](T_Tessa_Cards_Extensions_ICardGetFileVersionsExtensionContext.htm)
    Контекст процесса получения версий файла.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardGetFileVersionsExtension.AfterRequest(ICardGetFileVersionsExtensionContext)](M_Tessa_Cards_Extensions_ICardGetFileVersionsExtension_AfterRequest.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardGetFileVersionsExtension -
](T_Tessa_Cards_Extensions_CardGetFileVersionsExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
