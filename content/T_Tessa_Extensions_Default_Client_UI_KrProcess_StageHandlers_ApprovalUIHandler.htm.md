# ApprovalUIHandler - класс
UI обработчик типа этапа
[ApprovalDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptors_ApprovalDescriptor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers](N_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ApprovalUIHandler : StageTypeUIHandlerBase
VB __Копировать
     Public NotInheritable Class ApprovalUIHandler
    	Inherits StageTypeUIHandlerBase
C++ __Копировать
     public ref class ApprovalUIHandler sealed : public StageTypeUIHandlerBase
F# __Копировать
     [<SealedAttribute>]
    type ApprovalUIHandler = 
        class
            inherit StageTypeUIHandlerBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StageTypeUIHandlerBase](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_StageTypeUIHandlerBase.htm) __ ApprovalUIHandler
##  __Конструкторы
[ApprovalUIHandler](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_ApprovalUIHandler__ctor.htm)|
Инициализирует новый экземпляр класса.  
---|---  
## __Методы
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
[Finalize(IKrStageTypeUIHandlerContext)](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_ApprovalUIHandler_Finalize.htm)|
Выполняется при закрытии строки с параметрами этапа. Вызывается как при
закрытии с сохранением строки, так и при отмене.  
(Переопределяет
[StageTypeUIHandlerBase.Finalize(IKrStageTypeUIHandlerContext)](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_StageTypeUIHandlerBase_Finalize.htm))  
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
[Initialize](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_ApprovalUIHandler_Initialize.htm)|
Выполняется при создании и открытии на редактирование существующей строки с
параметрами этапа.  
(Переопределяет
[StageTypeUIHandlerBase.Initialize(IKrStageTypeUIHandlerContext)](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_StageTypeUIHandlerBase_Initialize.htm))  
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
(Унаследован от
[StageTypeUIHandlerBase](T_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_StageTypeUIHandlerBase.htm))  
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
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers - пространство
имён](N_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers.htm)
