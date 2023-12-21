# KrExecutionUnit - класс
Единица выполнения объекта маршрута.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrExecutionUnit : IKrExecutionUnit
VB __Копировать
     Public NotInheritable Class KrExecutionUnit
    	Implements IKrExecutionUnit
C++ __Копировать
     public ref class KrExecutionUnit sealed : IKrExecutionUnit
F# __Копировать
     [<SealedAttribute>]
    type KrExecutionUnit = 
        class
            interface IKrExecutionUnit
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrExecutionUnit
Implements
    [IKrExecutionUnit](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_IKrExecutionUnit.htm)
##  __Заметки
Представляет собой агрегацию метаинформации о шаблоне этапа или группе этапов
(название, позиция, sql) и объекта, сгенерированного на основе карточки,
скомпилированного и инстанцированного.
## __Конструкторы
[KrExecutionUnit(IKrRuntimeStage,
IKrScript)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionUnit__ctor.htm)|
Инициализирует новый экземпляр класса.  
---|---  
[KrExecutionUnit(IKrStageGroup,
IKrScript)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionUnit__ctor_1.htm)|
Инициализирует новый экземпляр класса.  
[KrExecutionUnit(IKrStageTemplate,
IKrScript)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionUnit__ctor_2.htm)|
Инициализирует новый экземпляр класса.  
## __Свойства
[DesignTimeSources](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionUnit_DesignTimeSources.htm)|
Исходные коды для этапа перерасчета.  
---|---  
[ID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionUnit_ID.htm)|
Идентификатор единицы выполнения.  
[Instance](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionUnit_Instance.htm)|
Cгенерированный на основе карточки, скомпилированный и созданный объект.  
[Name](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionUnit_Name.htm)|
Название единицы выполнения.  
[RuntimeSources](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionUnit_RuntimeSources.htm)|
Исходные коды на момент выполнения процесса.  
[RuntimeStage](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionUnit_RuntimeStage.htm)|
Информация об этапе в процессе выполнения.  
[StageGroup](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionUnit_StageGroup.htm)|
Информация о группе этапов.  
[StageTemplate](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrExecutionUnit_StageTemplate.htm)|
Информация о шаблоне этапов.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Extensions.Default.Server.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers.htm)
