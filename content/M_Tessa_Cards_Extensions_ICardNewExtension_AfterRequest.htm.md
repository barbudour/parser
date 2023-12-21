# ICardNewExtension.AfterRequest - метод
Действие, выполняемое после создания структуры карточки как при успешном, так
и при неудачном результате.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task AfterRequest(
    	ICardNewExtensionContext context
    )
VB __Копировать
     Function AfterRequest ( 
    	context As ICardNewExtensionContext
    ) As Task
C++ __Копировать
    Task^ AfterRequest(
    	ICardNewExtensionContext^ context
    )
F# __Копировать
     abstract AfterRequest : 
            context : ICardNewExtensionContext -> Task 
#### Параметры
context
[ICardNewExtensionContext](T_Tessa_Cards_Extensions_ICardNewExtensionContext.htm)
    Контекст процесса создания структуры карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardNewExtension - ](T_Tessa_Cards_Extensions_ICardNewExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
