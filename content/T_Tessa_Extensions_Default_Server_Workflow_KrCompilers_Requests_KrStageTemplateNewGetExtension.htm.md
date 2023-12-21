# KrStageTemplateNewGetExtension - класс
Расширение [ICardNewExtension](T_Tessa_Cards_Extensions_ICardNewExtension.htm)
для процесса создания и
[ICardGetExtension](T_Tessa_Cards_Extensions_ICardGetExtension.htm) для
процесса загрузки карточки шаблона этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.Requests](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrStageTemplateNewGetExtension : KrTemplateNewGetExtension
VB __Копировать
     Public NotInheritable Class KrStageTemplateNewGetExtension
    	Inherits KrTemplateNewGetExtension
C++ __Копировать
     public ref class KrStageTemplateNewGetExtension sealed : public KrTemplateNewGetExtension
F# __Копировать
     [<SealedAttribute>]
    type KrStageTemplateNewGetExtension = 
        class
            inherit KrTemplateNewGetExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardNewGetExtension](T_Tessa_Cards_Extensions_CardNewGetExtension.htm) __[KrTemplateNewGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateNewGetExtension.htm) __ KrStageTemplateNewGetExtension
##  __Конструкторы
[KrStageTemplateNewGetExtension](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrStageTemplateNewGetExtension__ctor.htm)|
Инициализирует новый экземпляр класса KrStageTemplateNewGetExtension.  
---|---  
## __Методы
[AfterRequest(ICardGetExtensionContext)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateNewGetExtension_AfterRequest.htm)|
Действие, выполняемое после получения карточки как при успешном, так и при
неудачном результате.  
(Унаследован от
[KrTemplateNewGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateNewGetExtension.htm))  
---|---  
[AfterRequest(ICardNewExtensionContext)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateNewGetExtension_AfterRequest_1.htm)|
Действие, выполняемое после создания структуры карточки как при успешном, так
и при неудачном результате.  
(Унаследован от
[KrTemplateNewGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateNewGetExtension.htm))  
[AfterRequestFinally(ICardGetExtensionContext)](M_Tessa_Cards_Extensions_CardNewGetExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после получения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardNewGetExtension](T_Tessa_Cards_Extensions_CardNewGetExtension.htm))  
[AfterRequestFinally(ICardNewExtensionContext)](M_Tessa_Cards_Extensions_CardNewGetExtension_AfterRequestFinally_1.htm)|
Действие, выполняемое при возникновении исключения или после создания
структуры карточки как при успешном, так и при неудачном результате.
Необработанные исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardNewGetExtension](T_Tessa_Cards_Extensions_CardNewGetExtension.htm))  
[BeforeRequest(ICardGetExtensionContext)](M_Tessa_Cards_Extensions_CardNewGetExtension_BeforeRequest.htm)|
Действие, выполняемое перед получением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы получение карточки стандартными
средствами не выполнялось.  
(Унаследован от
[CardNewGetExtension](T_Tessa_Cards_Extensions_CardNewGetExtension.htm))  
[BeforeRequest(ICardNewExtensionContext)](M_Tessa_Cards_Extensions_CardNewGetExtension_BeforeRequest_1.htm)|
Действие, выполняемое перед созданием структуры карточки стандартными
средствами. Может установить ответ на запрос для того, чтобы создание
структуры карточки стандартными средствами не выполнялось.  
(Унаследован от
[CardNewGetExtension](T_Tessa_Cards_Extensions_CardNewGetExtension.htm))  
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
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.Requests - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests.htm)
