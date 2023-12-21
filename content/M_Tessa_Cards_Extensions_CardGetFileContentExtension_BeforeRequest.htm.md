# CardGetFileContentExtension.BeforeRequest - метод
Действие, выполняемое перед получением контента файла стандартными средствами.
Может установить ответ на запрос и функцию получения контента для того, чтобы
получение контента стандартными средствами не выполнялось.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task BeforeRequest(
    	ICardGetFileContentExtensionContext context
    )
VB __Копировать
     Public Overridable Function BeforeRequest ( 
    	context As ICardGetFileContentExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ BeforeRequest(
    	ICardGetFileContentExtensionContext^ context
    )
F# __Копировать
     abstract BeforeRequest : 
            context : ICardGetFileContentExtensionContext -> Task 
    override BeforeRequest : 
            context : ICardGetFileContentExtensionContext -> Task 
#### Параметры
context
[ICardGetFileContentExtensionContext](T_Tessa_Cards_Extensions_ICardGetFileContentExtensionContext.htm)
    Контекст процесса получения контента файла.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardGetFileContentExtension.BeforeRequest(ICardGetFileContentExtensionContext)](M_Tessa_Cards_Extensions_ICardGetFileContentExtension_BeforeRequest.htm)  
##  __См. также
#### Ссылки
[CardGetFileContentExtension -
](T_Tessa_Cards_Extensions_CardGetFileContentExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
