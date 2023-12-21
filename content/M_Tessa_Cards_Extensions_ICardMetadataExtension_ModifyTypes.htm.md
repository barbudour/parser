# ICardMetadataExtension.ModifyTypes - метод
Изменяет типы карточек, по которым затем будет строиться метаинформация.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task ModifyTypes(
    	ICardMetadataExtensionContext context
    )
VB __Копировать
     Function ModifyTypes ( 
    	context As ICardMetadataExtensionContext
    ) As Task
C++ __Копировать
    Task^ ModifyTypes(
    	ICardMetadataExtensionContext^ context
    )
F# __Копировать
     abstract ModifyTypes : 
            context : ICardMetadataExtensionContext -> Task 
#### Параметры
context
[ICardMetadataExtensionContext](T_Tessa_Cards_Extensions_ICardMetadataExtensionContext.htm)
    Контекст расширения, содержащий изменяемую коллекцию типов карточек.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardMetadataExtension -
](T_Tessa_Cards_Extensions_ICardMetadataExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
