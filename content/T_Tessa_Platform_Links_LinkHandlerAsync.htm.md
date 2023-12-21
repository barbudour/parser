# LinkHandlerAsync - делегат
Обработчик ссылок tessa:// на приложения Tessa. В случае успешной обработки он
должен установить значение
[Handled](P_Tessa_Platform_Links_ILinkContext_Handled.htm) равным true.
## __Definition
 **Пространство имён:** [Tessa.Platform.Links](N_Tessa_Platform_Links.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate Task LinkHandlerAsync(
    	ILinkContext context
    )
VB __Копировать
     Public Delegate Function LinkHandlerAsync ( 
    	context As ILinkContext
    ) As Task
C++ __Копировать
     public delegate Task^ LinkHandlerAsync(
    	ILinkContext^ context
    )
F# __Копировать
     type LinkHandlerAsync = 
        delegate of 
            context : ILinkContext -> Task
#### Параметры
context [ILinkContext](T_Tessa_Platform_Links_ILinkContext.htm)
    Контекст обработчика по открытию ссылок.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[Tessa.Platform.Links - пространство имён](N_Tessa_Platform_Links.htm)
