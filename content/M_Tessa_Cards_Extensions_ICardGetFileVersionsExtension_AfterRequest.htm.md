# ICardGetFileVersionsExtension.AfterRequest - метод
Действие, выполняемое после получения версий файла как при успешном, так и при
неудачном результате.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task AfterRequest(
    	ICardGetFileVersionsExtensionContext context
    )
VB __Копировать
     Function AfterRequest ( 
    	context As ICardGetFileVersionsExtensionContext
    ) As Task
C++ __Копировать
    Task^ AfterRequest(
    	ICardGetFileVersionsExtensionContext^ context
    )
F# __Копировать
     abstract AfterRequest : 
            context : ICardGetFileVersionsExtensionContext -> Task 
#### Параметры
context
[ICardGetFileVersionsExtensionContext](T_Tessa_Cards_Extensions_ICardGetFileVersionsExtensionContext.htm)
    Контекст процесса получения версий файла.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardGetFileVersionsExtension -
](T_Tessa_Cards_Extensions_ICardGetFileVersionsExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
