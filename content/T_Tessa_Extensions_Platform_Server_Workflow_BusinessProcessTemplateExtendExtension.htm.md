# BusinessProcessTemplateExtendExtension - класс
Расширение, осуществляющее работу с карточкой шаблона процесса, связанную с
расширением прав доступа к тайлам.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Workflow](N_Tessa_Extensions_Platform_Server_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class BusinessProcessTemplateExtendExtension : CardStoreExtension, 
    	ICardGetExtension, ICardExtension, IExtension, ICardDeleteExtension
VB __Копировать
     Public NotInheritable Class BusinessProcessTemplateExtendExtension
    	Inherits CardStoreExtension
    	Implements ICardGetExtension, ICardExtension, IExtension, ICardDeleteExtension
C++ __Копировать
     public ref class BusinessProcessTemplateExtendExtension sealed : public CardStoreExtension, 
    	ICardGetExtension, ICardExtension, IExtension, ICardDeleteExtension
F# __Копировать
     [<SealedAttribute>]
    type BusinessProcessTemplateExtendExtension = 
        class
            inherit CardStoreExtension
            interface ICardGetExtension
            interface ICardExtension
            interface IExtension
            interface ICardDeleteExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm) __ BusinessProcessTemplateExtendExtension
Implements
    [ICardDeleteExtension](T_Tessa_Cards_Extensions_ICardDeleteExtension.htm), [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [ICardGetExtension](T_Tessa_Cards_Extensions_ICardGetExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Конструкторы
[BusinessProcessTemplateExtendExtension](M_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessTemplateExtendExtension__ctor.htm)|
Инициализирует новый экземпляр класса BusinessProcessTemplateExtendExtension  
---|---  
##  __Методы
[AfterBeginTransaction(ICardDeleteExtensionContext)](M_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessTemplateExtendExtension_AfterBeginTransaction.htm)|
Действие, выполняемое после начала транзакции.  
---|---  
[AfterBeginTransaction(ICardStoreExtensionContext)](M_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessTemplateExtendExtension_AfterBeginTransaction_1.htm)|
Действие, выполняемое после начала транзакции.  
(Переопределяет
[CardStoreExtension.AfterBeginTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_AfterBeginTransaction.htm))  
[AfterRequest(ICardDeleteExtensionContext)](M_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessTemplateExtendExtension_AfterRequest.htm)|
Действие, выполняемое после удаления карточки как при успешном, так и при
неудачном результате.  
[AfterRequest(ICardGetExtensionContext)](M_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessTemplateExtendExtension_AfterRequest_1.htm)|
Действие, выполняемое после получения карточки как при успешном, так и при
неудачном результате.  
[AfterRequest(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_AfterRequest.htm)|
Действие, выполняемое после сохранения карточки как при успешном, так и при
неудачном результате.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
[AfterRequestFinally(ICardDeleteExtensionContext)](M_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessTemplateExtendExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после удаления карточки
как при успешном, так и при неудачном результате. Необработанные исключения не
прерывают выполнение цепочки расширений.  
[AfterRequestFinally(ICardGetExtensionContext)](M_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessTemplateExtendExtension_AfterRequestFinally_1.htm)|
Действие, выполняемое при возникновении исключения или после получения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
[AfterRequestFinally(ICardStoreExtensionContext)](M_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessTemplateExtendExtension_AfterRequestFinally_2.htm)|  
(Переопределяет
[CardStoreExtension.AfterRequestFinally(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_AfterRequestFinally.htm))  
[BeforeCommitTransaction(ICardDeleteExtensionContext)](M_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessTemplateExtendExtension_BeforeCommitTransaction.htm)|
Действие, выполняемое перед коммитом транзакции.  
[BeforeCommitTransaction(ICardStoreExtensionContext)](M_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessTemplateExtendExtension_BeforeCommitTransaction_1.htm)|
Действие, выполняемое перед коммитом транзакции.  
(Переопределяет
[CardStoreExtension.BeforeCommitTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_BeforeCommitTransaction.htm))  
[BeforeRequest(ICardDeleteExtensionContext)](M_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessTemplateExtendExtension_BeforeRequest.htm)|
Действие, выполняемое перед удалением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы удаление карточки стандартными
средствами не выполнялось.  
[BeforeRequest(ICardGetExtensionContext)](M_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessTemplateExtendExtension_BeforeRequest_1.htm)|
Действие, выполняемое перед получением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы получение карточки стандартными
средствами не выполнялось.  
[BeforeRequest(ICardStoreExtensionContext)](M_Tessa_Extensions_Platform_Server_Workflow_BusinessProcessTemplateExtendExtension_BeforeRequest_2.htm)|
Действие, выполняемое перед сохранением карточки стандартными средствами.
Может установить ответ на запрос для того, чтобы сохранение карточки
стандартными средствами не выполнялось.  
(Переопределяет
[CardStoreExtension.BeforeRequest(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_BeforeRequest.htm))  
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
[Tessa.Extensions.Platform.Server.Workflow - пространство
имён](N_Tessa_Extensions_Platform_Server_Workflow.htm)
