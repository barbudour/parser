# StageTypeUIHandlerBase - класс
UI обработчик типа этапа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers](N_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class StageTypeUIHandlerBase : IStageTypeUIHandler
VB __Копировать
     Public MustInherit Class StageTypeUIHandlerBase
    	Implements IStageTypeUIHandler
C++ __Копировать
     public ref class StageTypeUIHandlerBase abstract : IStageTypeUIHandler
F# __Копировать
     [<AbstractClassAttribute>]
    type StageTypeUIHandlerBase = 
        class
            interface IStageTypeUIHandler
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ StageTypeUIHandlerBase
Derived
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers.AddFromTemplateUIHandler](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_AddFromTemplateUIHandler.htm)
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers.ApprovalUIHandler](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_ApprovalUIHandler.htm)
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers.CreateCardUIHandler](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_CreateCardUIHandler.htm)
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers.DialogUIHandler](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_DialogUIHandler.htm)
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers.ProcessManagementUIHandler](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_ProcessManagementUIHandler.htm)
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers.ResolutionStageUIHandler](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_ResolutionStageUIHandler.htm)
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers.SigningUIHandler](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_SigningUIHandler.htm)
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers.TabCaptionUIHandler](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_TabCaptionUIHandler.htm)
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers.TypedTaskUIHandler](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_TypedTaskUIHandler.htm)
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers.UniversalTaskStageTypeUIHandler](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_UniversalTaskStageTypeUIHandler.htm)
Подробнее __Less __
Implements
    [IStageTypeUIHandler](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IStageTypeUIHandler.htm)
##  __Конструкторы
[StageTypeUIHandlerBase](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_StageTypeUIHandlerBase__ctor.htm)|
Инициализирует новый экземпляр класса StageTypeUIHandlerBase  
---|---  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize()](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize(IKrStageTypeUIHandlerContext)](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_StageTypeUIHandlerBase_Finalize.htm)|
Выполняется при закрытии строки с параметрами этапа. Вызывается как при
закрытии с сохранением строки, так и при отмене.  
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
[Initialize](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_StageTypeUIHandlerBase_Initialize.htm)|
Выполняется при создании и открытии на редактирование существующей строки с
параметрами этапа.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Validate](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_StageTypeUIHandlerBase_Validate.htm)|
Выполняется при валидации строки с параметрами этапа перед сохранением или
закрытием её окна редактирования.  
## __Методы расширения
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
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers - пространство
имён](N_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers.htm)
