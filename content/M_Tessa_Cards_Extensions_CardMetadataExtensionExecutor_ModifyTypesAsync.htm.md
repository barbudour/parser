# CardMetadataExtensionExecutor.ModifyTypesAsync - метод
Выполняет расширения, изменяющие типы карточек, по которым затем будет
строиться метаинформация.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task ModifyTypesAsync(
    	ICardMetadataExtensionContext context
    )
VB __Копировать
     Public Function ModifyTypesAsync ( 
    	context As ICardMetadataExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ ModifyTypesAsync(
    	ICardMetadataExtensionContext^ context
    ) sealed
F# __Копировать
     abstract ModifyTypesAsync : 
            context : ICardMetadataExtensionContext -> Task 
    override ModifyTypesAsync : 
            context : ICardMetadataExtensionContext -> Task 
#### Параметры
context
[ICardMetadataExtensionContext](T_Tessa_Cards_Extensions_ICardMetadataExtensionContext.htm)
    Контекст расширения, содержащий изменяемую коллекцию типов карточек.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardMetadataExtensionExecutor.ModifyTypesAsync(ICardMetadataExtensionContext)](M_Tessa_Cards_Extensions_ICardMetadataExtensionExecutor_ModifyTypesAsync.htm)  
##  __См. также
#### Ссылки
[CardMetadataExtensionExecutor -
](T_Tessa_Cards_Extensions_CardMetadataExtensionExecutor.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
