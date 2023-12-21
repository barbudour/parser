# KrProcessUILauncher.SpecificParameters - класс
Предоставляет параметры запуска процесса с клиента.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Workflow.KrProcess](N_Tessa_Extensions_Default_Client_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SpecificParameters : KrProcessClientLauncherBaseSpecificParameters
VB __Копировать
     Public NotInheritable Class SpecificParameters
    	Inherits KrProcessClientLauncherBaseSpecificParameters
C++ __Копировать
     public ref class SpecificParameters sealed : public KrProcessClientLauncherBaseSpecificParameters
F# __Копировать
     [<SealedAttribute>]
    type SpecificParameters = 
        class
            inherit KrProcessClientLauncherBaseSpecificParameters
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[KrProcessLauncherSpecificParametersBase](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessLauncherSpecificParametersBase.htm) __[KrProcessClientLauncherBaseSpecificParameters](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientLauncherBaseSpecificParameters.htm) __ KrProcessUILauncher.SpecificParameters
##  __Конструкторы
[KrProcessUILauncher.SpecificParameters](M_Tessa_Extensions_Default_Client_Workflow_KrProcess_KrProcessUILauncher_SpecificParameters__ctor.htm)|
Инициализирует новый экземпляр класса KrProcessUILauncher.SpecificParameters  
---|---  
##  __Свойства
[CardEditor](P_Tessa_Extensions_Default_Client_Workflow_KrProcess_KrProcessUILauncher_SpecificParameters_CardEditor.htm)|
Возвращает или задаёт указанный
[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm) который следует
использовать. Приоритет ниже, чем у
[UseCurrentCardEditor](P_Tessa_Extensions_Default_Client_Workflow_KrProcess_KrProcessUILauncher_SpecificParameters_UseCurrentCardEditor.htm).  
---|---  
[RaiseErrorWhenExecutionIsForbidden](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessLauncherSpecificParametersBase_RaiseErrorWhenExecutionIsForbidden.htm)|
Возвращает или задаёт значение флага, показывающего, следует ли создавать
ошибку, если процесс не может быть выполнен из-за ограничений (параметр
вторичного процесса "Сообщение при невозможности выполнения процесса").  
(Унаследован от
[KrProcessLauncherSpecificParametersBase](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessLauncherSpecificParametersBase.htm))  
[RequestInfo](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientLauncherBaseSpecificParameters_RequestInfo.htm)|
Возвращает или задаёт дополнительную информацию, передаваемую в запросе на
сохранение карточки для расширений. Данные должны быть сериализуемых типов.
Может иметь значение по умолчанию для типа.  
(Унаследован от
[KrProcessClientLauncherBaseSpecificParameters](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientLauncherBaseSpecificParameters.htm))  
[UseCurrentCardEditor](P_Tessa_Extensions_Default_Client_Workflow_KrProcess_KrProcessUILauncher_SpecificParameters_UseCurrentCardEditor.htm)|
Возвращает или задаёт значение, показывающее, следует ли использовать текущий
[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm) или нет. Приоритет
выше, чем у свойства
[CardEditor](P_Tessa_Extensions_Default_Client_Workflow_KrProcess_KrProcessUILauncher_SpecificParameters_CardEditor.htm).  
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
[Tessa.Extensions.Default.Client.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Client_Workflow_KrProcess.htm)
