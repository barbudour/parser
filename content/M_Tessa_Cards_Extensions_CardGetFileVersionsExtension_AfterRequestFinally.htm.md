# CardGetFileVersionsExtension.AfterRequestFinally - метод
Действие, выполняемое при возникновении исключения или после получения версий
файла как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task AfterRequestFinally(
    	ICardGetFileVersionsExtensionContext context
    )
VB __Копировать
     Public Overridable Function AfterRequestFinally ( 
    	context As ICardGetFileVersionsExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequestFinally(
    	ICardGetFileVersionsExtensionContext^ context
    )
F# __Копировать
     abstract AfterRequestFinally : 
            context : ICardGetFileVersionsExtensionContext -> Task 
    override AfterRequestFinally : 
            context : ICardGetFileVersionsExtensionContext -> Task 
#### Параметры
context
[ICardGetFileVersionsExtensionContext](T_Tessa_Cards_Extensions_ICardGetFileVersionsExtensionContext.htm)
    Контекст процесса получения версий файла.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardGetFileVersionsExtension.AfterRequestFinally(ICardGetFileVersionsExtensionContext)](M_Tessa_Cards_Extensions_ICardGetFileVersionsExtension_AfterRequestFinally.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardGetFileVersionsExtension -
](T_Tessa_Cards_Extensions_CardGetFileVersionsExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
