# CardMetadataWithoutExtensionExecutor.ModifyMetadataAsync - метод
Выполняет расширения, изменяющие метаинформацию по типам карточек после её
построения.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task ModifyMetadataAsync(
    	ICardMetadataExtensionContext context
    )
VB __Копировать
     Public Function ModifyMetadataAsync ( 
    	context As ICardMetadataExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ ModifyMetadataAsync(
    	ICardMetadataExtensionContext^ context
    ) sealed
F# __Копировать
     abstract ModifyMetadataAsync : 
            context : ICardMetadataExtensionContext -> Task 
    override ModifyMetadataAsync : 
            context : ICardMetadataExtensionContext -> Task 
#### Параметры
context
[ICardMetadataExtensionContext](T_Tessa_Cards_Extensions_ICardMetadataExtensionContext.htm)
    Контекст расширения, содержащий изменяемую метаинформацию.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardMetadataExtensionExecutor.ModifyMetadataAsync(ICardMetadataExtensionContext)](M_Tessa_Cards_Extensions_ICardMetadataExtensionExecutor_ModifyMetadataAsync.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardMetadataWithoutExtensionExecutor -
](T_Tessa_Cards_Extensions_CardMetadataWithoutExtensionExecutor.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
