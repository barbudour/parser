# KrTaskKindGetExtension - класс
Расширение, проставляющее информацию о виде задания из TaskCommonInfo.Kind в
task.Info. Это нужно для того, чтобы платформенное расширение
[TaskKindGetExtension](T_Tessa_Extensions_Platform_Server_Cards_TaskKindGetExtension.htm)
по этому Info проставило заголовок задания. По умолчанию заголовок ставится по
таск хистори, но если задание не пишется в историю, то это расширение
позволяет выставить заголовок.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Requests](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrTaskKindGetExtension : CardGetExtension
VB __Копировать
     Public NotInheritable Class KrTaskKindGetExtension
    	Inherits CardGetExtension
C++ __Копировать
     public ref class KrTaskKindGetExtension sealed : public CardGetExtension
F# __Копировать
     [<SealedAttribute>]
    type KrTaskKindGetExtension = 
        class
            inherit CardGetExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardGetExtension](T_Tessa_Cards_Extensions_CardGetExtension.htm) __ KrTaskKindGetExtension
##  __Конструкторы
[KrTaskKindGetExtension](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrTaskKindGetExtension__ctor.htm)|
Инициализирует новый экземпляр класса KrTaskKindGetExtension  
---|---  
##  __Методы
[AfterRequest](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrTaskKindGetExtension_AfterRequest.htm)|  
(Переопределяет
[CardGetExtension.AfterRequest(ICardGetExtensionContext)](M_Tessa_Cards_Extensions_CardGetExtension_AfterRequest.htm))  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardGetExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после получения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardGetExtension](T_Tessa_Cards_Extensions_CardGetExtension.htm))  
[BeforeRequest](M_Tessa_Cards_Extensions_CardGetExtension_BeforeRequest.htm)|
Действие, выполняемое перед получением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы получение карточки стандартными
средствами не выполнялось.  
(Унаследован от
[CardGetExtension](T_Tessa_Cards_Extensions_CardGetExtension.htm))  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Requests - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests.htm)
