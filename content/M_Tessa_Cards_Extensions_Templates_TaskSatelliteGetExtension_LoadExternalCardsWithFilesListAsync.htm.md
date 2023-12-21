# TaskSatelliteGetExtension.LoadExternalCardsWithFilesListAsync - метод
Возвращает идентификаторы карточек-сателлитов, которые содержат файлы и для
которых файлы требуется загрузить как виртуальные файлы для текущей карточки-
сателлита. Например, это идентификаторы сателлитов для заданий, которые
расположены выше по иерархии в истории заданий.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract Task<IEnumerable<Guid>> LoadExternalCardsWithFilesListAsync(
    	ICardGetExtensionContext context,
    	IDbScope dbScope,
    	Guid currentTaskRowID
    )
VB __Копировать
     Protected MustOverride Function LoadExternalCardsWithFilesListAsync ( 
    	context As ICardGetExtensionContext,
    	dbScope As IDbScope,
    	currentTaskRowID As Guid
    ) As Task(Of IEnumerable(Of Guid))
C++ __Копировать
     protected:
    virtual Task<IEnumerable<Guid>^>^ LoadExternalCardsWithFilesListAsync(
    	ICardGetExtensionContext^ context, 
    	IDbScope^ dbScope, 
    	Guid currentTaskRowID
    ) abstract
F# __Копировать
     abstract LoadExternalCardsWithFilesListAsync : 
            context : ICardGetExtensionContext * 
            dbScope : IDbScope * 
            currentTaskRowID : Guid -> Task<IEnumerable<Guid>> 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст расширения по загрузке карточки-сателлита.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, обеспечивающий взаимодействие с базой данных.
currentTaskRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор задания для текущей карточки-сателлита.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификаторы карточек-сателлитов, которые содержат файлы и для которых файлы
требуется загрузить как виртуальные файлы для текущей карточки-сателлита.
## __См. также
#### Ссылки
[TaskSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
