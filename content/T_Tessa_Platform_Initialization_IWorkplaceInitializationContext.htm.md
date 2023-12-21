# IWorkplaceInitializationContext - интерфейс
Контекст инициализации рабочих мест. Правило инициализации может скрыть
некоторые узлы рабочего места в зависимости от любых условий, например, от
того, в какие роли входит сотрудник.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkplaceInitializationContext
VB __Копировать
     Public Interface IWorkplaceInitializationContext
C++ __Копировать
     public interface class IWorkplaceInitializationContext
F# __Копировать
     type IWorkplaceInitializationContext = interface end
##  __Свойства
[AvailableWorkplaces](P_Tessa_Platform_Initialization_IWorkplaceInitializationContext_AvailableWorkplaces.htm)|
Все рабочие места, доступные пользователю.  
---|---  
[DbScope](P_Tessa_Platform_Initialization_IWorkplaceInitializationContext_DbScope.htm)|
Объект, обеспечивающий доступ к базе данных.  
[ExtensionContext](P_Tessa_Platform_Initialization_IWorkplaceInitializationContext_ExtensionContext.htm)|
Контекст расширений на инициализацию.  
[Info](P_Tessa_Platform_Initialization_IWorkplaceInitializationContext_Info.htm)|
Произвольная информация по обходу узлов, которая сохраняется только в пределах
обхода одного рабочего места. Например, здесь можно хранить информацию по
правам на просмотр узлов конкретного рабочего места.  
[Session](P_Tessa_Platform_Initialization_IWorkplaceInitializationContext_Session.htm)|
Сессия пользователя.  
[ValidationResult](P_Tessa_Platform_Initialization_IWorkplaceInitializationContext_ValidationResult.htm)|
Сообщения валидации, возникшие в процессе фильтрации узлов.  
[Workplace](P_Tessa_Platform_Initialization_IWorkplaceInitializationContext_Workplace.htm)|
Рабочее место, для которого выполняется обход узлов.  
[WorkplaceInfo](P_Tessa_Platform_Initialization_IWorkplaceInitializationContext_WorkplaceInfo.htm)|
Произвольная информация по обходу узлов, которая сохраняется при обходе всех
рабочих мест. Например, здесь можно хранить информацию по правам на просмотр
узлов конкретного рабочего места.  
## __См. также
#### Ссылки
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
