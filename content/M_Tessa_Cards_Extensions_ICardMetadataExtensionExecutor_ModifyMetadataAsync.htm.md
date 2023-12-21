# ICardMetadataExtensionExecutor.ModifyMetadataAsync - метод
Выполняет расширения, изменяющие метаинформацию по типам карточек после её
построения.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task ModifyMetadataAsync(
    	ICardMetadataExtensionContext context
    )
VB __Копировать
     Function ModifyMetadataAsync ( 
    	context As ICardMetadataExtensionContext
    ) As Task
C++ __Копировать
    Task^ ModifyMetadataAsync(
    	ICardMetadataExtensionContext^ context
    )
F# __Копировать
     abstract ModifyMetadataAsync : 
            context : ICardMetadataExtensionContext -> Task 
#### Параметры
context
[ICardMetadataExtensionContext](T_Tessa_Cards_Extensions_ICardMetadataExtensionContext.htm)
    Контекст расширения, содержащий изменяемую метаинформацию.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardMetadataExtensionExecutor -
](T_Tessa_Cards_Extensions_ICardMetadataExtensionExecutor.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
