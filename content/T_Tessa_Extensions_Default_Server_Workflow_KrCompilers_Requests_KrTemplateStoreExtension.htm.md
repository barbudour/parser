# KrTemplateStoreExtension - класс
Базовый класс расширений для процесса сохранения карточки содержащей шаблон
этапов маршрута документов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.Requests](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class KrTemplateStoreExtension : CardStoreExtension
VB __Копировать
     Public MustInherit Class KrTemplateStoreExtension
    	Inherits CardStoreExtension
C++ __Копировать
     public ref class KrTemplateStoreExtension abstract : public CardStoreExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type KrTemplateStoreExtension = 
        class
            inherit CardStoreExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm) __ KrTemplateStoreExtension
Derived
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.Requests.KrSecondaryProcessStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrSecondaryProcessStoreExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.Requests.KrStageTemplateStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrStageTemplateStoreExtension.htm)
##  __Конструкторы
[KrTemplateStoreExtension](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateStoreExtension__ctor.htm)|
Инициализирует новый экземпляр класса KrTemplateStoreExtension.  
---|---  
## __Методы
[AfterBeginTransaction](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateStoreExtension_AfterBeginTransaction.htm)|
Действие, выполняемое после начала транзакции.  
(Переопределяет
[CardStoreExtension.AfterBeginTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_AfterBeginTransaction.htm))  
---|---  
[AfterRequest](M_Tessa_Cards_Extensions_CardStoreExtension_AfterRequest.htm)|
Действие, выполняемое после сохранения карточки как при успешном, так и при
неудачном результате.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardStoreExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после сохранения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
[BeforeCommitTransaction](M_Tessa_Cards_Extensions_CardStoreExtension_BeforeCommitTransaction.htm)|
Действие, выполняемое перед коммитом транзакции.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
[BeforeRequest](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateStoreExtension_BeforeRequest.htm)|
Действие, выполняемое перед сохранением карточки стандартными средствами.
Может установить ответ на запрос для того, чтобы сохранение карточки
стандартными средствами не выполнялось.  
(Переопределяет
[CardStoreExtension.BeforeRequest(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_BeforeRequest.htm))  
[DoInsert](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateStoreExtension_DoInsert.htm)|
Возвращает значение, показывающее, что необходимо обновление карточки при её
создании ([Insert](T_Tessa_Cards_CardStoreMode.htm)).  
[DoUpdate](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateStoreExtension_DoUpdate.htm)|
Возвращает значение, показывающее, что необходимо принудительное обновление
карточки при её изменении ([Update](T_Tessa_Cards_CardStoreMode.htm)).  
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
[GetInnerCardAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateStoreExtension_GetInnerCardAsync.htm)|
Возвращает обновляемую карточку в которую должны быть сохранены изменения из
сохраняемой карточки.  
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
[OnInsert](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateStoreExtension_OnInsert.htm)|
Действие выполняемое перед обработкой карточки при её создании
([Insert](T_Tessa_Cards_CardStoreMode.htm)).  
[OnUpdate](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateStoreExtension_OnUpdate.htm)|
Действие выполняемое перед обновлением карточки содержащей данные из
сохраняемой карточки.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[CardMetadata](F_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateStoreExtension_CardMetadata.htm)|  
---|---  
[CardStoreStrategy](F_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateStoreExtension_CardStoreStrategy.htm)|  
[KrProcessCache](F_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateStoreExtension_KrProcessCache.htm)|  
[Serializer](F_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateStoreExtension_Serializer.htm)|  
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
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.Requests - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests.htm)
