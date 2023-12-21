# ICardRepairExtension.BeforeRequest - метод
Действие, выполняемое перед исправлением структуры карточки.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task BeforeRequest(
    	ICardRepairExtensionContext context
    )
VB __Копировать
     Function BeforeRequest ( 
    	context As ICardRepairExtensionContext
    ) As Task
C++ __Копировать
    Task^ BeforeRequest(
    	ICardRepairExtensionContext^ context
    )
F# __Копировать
     abstract BeforeRequest : 
            context : ICardRepairExtensionContext -> Task 
#### Параметры
context
[ICardRepairExtensionContext](T_Tessa_Cards_Extensions_ICardRepairExtensionContext.htm)
    Контекст процесса исправления структуры карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardRepairExtension - ](T_Tessa_Cards_Extensions_ICardRepairExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
