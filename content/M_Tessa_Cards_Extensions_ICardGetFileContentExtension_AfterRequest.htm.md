# ICardGetFileContentExtension.AfterRequest - метод
Действие, выполняемое после получения контента файла как при успешном, так и
при неудачном результате.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task AfterRequest(
    	ICardGetFileContentExtensionContext context
    )
VB __Копировать
     Function AfterRequest ( 
    	context As ICardGetFileContentExtensionContext
    ) As Task
C++ __Копировать
    Task^ AfterRequest(
    	ICardGetFileContentExtensionContext^ context
    )
F# __Копировать
     abstract AfterRequest : 
            context : ICardGetFileContentExtensionContext -> Task 
#### Параметры
context
[ICardGetFileContentExtensionContext](T_Tessa_Cards_Extensions_ICardGetFileContentExtensionContext.htm)
    Контекст процесса получения контента файла.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardGetFileContentExtension -
](T_Tessa_Cards_Extensions_ICardGetFileContentExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
