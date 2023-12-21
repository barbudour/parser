# DisableRecalcPreparingGroupRecalcStrategy - класс
Стратегия подготавливающая данные для пересчёта маршрута. Возвращает этап
соответствующий текущему этапу, на момент применения стратегии, иначе значение
по умолчанию для типа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class DisableRecalcPreparingGroupRecalcStrategy : IPreparingGroupRecalcStrategy
VB __Копировать
     Public NotInheritable Class DisableRecalcPreparingGroupRecalcStrategy
    	Implements IPreparingGroupRecalcStrategy
C++ __Копировать
     public ref class DisableRecalcPreparingGroupRecalcStrategy sealed : IPreparingGroupRecalcStrategy
F# __Копировать
     [<SealedAttribute>]
    type DisableRecalcPreparingGroupRecalcStrategy = 
        class
            interface IPreparingGroupRecalcStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DisableRecalcPreparingGroupRecalcStrategy
Implements
    [IPreparingGroupRecalcStrategy](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IPreparingGroupRecalcStrategy.htm)
##  __Конструкторы
[DisableRecalcPreparingGroupRecalcStrategy](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_DisableRecalcPreparingGroupRecalcStrategy__ctor.htm)|
Инициализирует новый экземпляр класса
DisableRecalcPreparingGroupRecalcStrategy  
---|---  
##  __Свойства
[ExecutionUnits](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_DisableRecalcPreparingGroupRecalcStrategy_ExecutionUnits.htm)|
Возвращает коллекцию объектов выполнения.  
---|---  
[Used](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_DisableRecalcPreparingGroupRecalcStrategy_Used.htm)|
Возвращает признак, показывающий, что данная стратегия была применена.  
## __Методы
[ApplyAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_DisableRecalcPreparingGroupRecalcStrategy_ApplyAsync.htm)|
Применяет текущую стратегию.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetSuitableStage](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_DisableRecalcPreparingGroupRecalcStrategy_GetSuitableStage.htm)|
Возвращает первый этап удовлетворяющий стратегии.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
