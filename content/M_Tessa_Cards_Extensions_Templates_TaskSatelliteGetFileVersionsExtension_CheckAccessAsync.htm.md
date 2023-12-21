# TaskSatelliteGetFileVersionsExtension.CheckAccessAsync - метод
Возвращает признак того, что к основной карточке с заданным идентификатором
есть доступ. Это определяет, что есть доступ и к файлам сателлита.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract Task CheckAccessAsync(
    	ICardGetFileVersionsExtensionContext context,
    	Guid mainCardID
    )
VB __Копировать
     Protected MustOverride Function CheckAccessAsync ( 
    	context As ICardGetFileVersionsExtensionContext,
    	mainCardID As Guid
    ) As Task
C++ __Копировать
     protected:
    virtual Task^ CheckAccessAsync(
    	ICardGetFileVersionsExtensionContext^ context, 
    	Guid mainCardID
    ) abstract
F# __Копировать
     abstract CheckAccessAsync : 
            context : ICardGetFileVersionsExtensionContext * 
            mainCardID : Guid -> Task 
#### Параметры
context
[ICardGetFileVersionsExtensionContext](T_Tessa_Cards_Extensions_ICardGetFileVersionsExtensionContext.htm)
    Контекст расширения на получение версий файла.
mainCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор основной карточки, доступ к которой проверяется.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
true, если к основной карточке с заданным идентификатором есть доступ; false в
противном случае.
## __См. также
#### Ссылки
[TaskSatelliteGetFileVersionsExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetFileVersionsExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
