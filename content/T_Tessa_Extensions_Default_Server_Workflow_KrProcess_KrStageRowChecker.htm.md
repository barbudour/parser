# KrStageRowChecker - класс
Объект, определяющий наличие изменений в порядке и параметрах этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrStageRowChecker : IKrStageRowChecker
VB __Копировать
     Public NotInheritable Class KrStageRowChecker
    	Implements IKrStageRowChecker
C++ __Копировать
     public ref class KrStageRowChecker sealed : IKrStageRowChecker
F# __Копировать
     [<SealedAttribute>]
    type KrStageRowChecker = 
        class
            interface IKrStageRowChecker
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrStageRowChecker
Implements
    [IKrStageRowChecker](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_IKrStageRowChecker.htm)
##  __Конструкторы
[KrStageRowChecker](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrStageRowChecker__ctor.htm)|
Инициализирует новый экземпляр класса.  
---|---  
## __Свойства
[UntrackedFields](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrStageRowChecker_UntrackedFields.htm)|
Поля в строке этапа, игнорируемые при отслеживании изменений.  
---|---  
## __Методы
[AfterModifySatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrStageRowChecker_AfterModifySatelliteAsync.htm)|
Определяет наличие изменений в порядке и параметрах этапов после изменения
основного сателлита.  
---|---  
[BeforeModifySatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrStageRowChecker_BeforeModifySatelliteAsync.htm)|
Определяет наличие изменений в порядке и параметрах этапов перед изменением
основного сателлита.  
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
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HasAnySettingsSection](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrStageRowChecker_HasAnySettingsSection.htm)|
Проверяет, есть ли в карточке документа изменённые секции, содержащие
параметры этапов.  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)
