# CardGetFileVersionsExtension.BeforeRequest - метод
Действие, выполняемое перед получением версий файла стандартными средствами.
Может установить ответ на запрос для того, чтобы получение версий файла
стандартными средствами не выполнялось.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task BeforeRequest(
    	ICardGetFileVersionsExtensionContext context
    )
VB __Копировать
     Public Overridable Function BeforeRequest ( 
    	context As ICardGetFileVersionsExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ BeforeRequest(
    	ICardGetFileVersionsExtensionContext^ context
    )
F# __Копировать
     abstract BeforeRequest : 
            context : ICardGetFileVersionsExtensionContext -> Task 
    override BeforeRequest : 
            context : ICardGetFileVersionsExtensionContext -> Task 
#### Параметры
context
[ICardGetFileVersionsExtensionContext](T_Tessa_Cards_Extensions_ICardGetFileVersionsExtensionContext.htm)
    Контекст процесса получения версий файла.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardGetFileVersionsExtension.BeforeRequest(ICardGetFileVersionsExtensionContext)](M_Tessa_Cards_Extensions_ICardGetFileVersionsExtension_BeforeRequest.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardGetFileVersionsExtension -
](T_Tessa_Cards_Extensions_CardGetFileVersionsExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
