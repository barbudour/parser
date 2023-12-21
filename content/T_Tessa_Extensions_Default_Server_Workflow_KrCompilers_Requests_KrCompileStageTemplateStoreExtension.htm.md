# KrCompileStageTemplateStoreExtension - класс
Расширение на сохранение карточки KrStageTemplates Выполняет компиляцию при
наличии соответствующих флагов в Info При изменении исходных кодов
сбрасывается кэш компиляции и кэш этапов При изменении данных, не относящихся
к компиляции, сбрасывается кэш этапов
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.Requests](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrCompileStageTemplateStoreExtension : KrCompileSourceStoreExtension
VB __Копировать
     Public NotInheritable Class KrCompileStageTemplateStoreExtension
    	Inherits KrCompileSourceStoreExtension
C++ __Копировать
     public ref class KrCompileStageTemplateStoreExtension sealed : public KrCompileSourceStoreExtension
F# __Копировать
     [<SealedAttribute>]
    type KrCompileStageTemplateStoreExtension = 
        class
            inherit KrCompileSourceStoreExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm) __[KrCompileSourceStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileSourceStoreExtension.htm) __ KrCompileStageTemplateStoreExtension
##  __Конструкторы
[KrCompileStageTemplateStoreExtension](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileStageTemplateStoreExtension__ctor.htm)|
Инициализирует новый экземпляр класса KrCompileStageTemplateStoreExtension.  
---|---  
## __Свойства
[CompilationCache](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileSourceStoreExtension_CompilationCache.htm)|
Кэш с результатами компиляции объектов подсистемы маршрутов.  
(Унаследован от
[KrCompileSourceStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileSourceStoreExtension.htm))  
---|---  
[CompilationResultStorage](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileSourceStoreExtension_CompilationResultStorage.htm)|
Объект, предоставляющий доступ к результатам компиляции подсистемы маршрутов.  
(Унаследован от
[KrCompileSourceStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileSourceStoreExtension.htm))  
[ProcessCache](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileSourceStoreExtension_ProcessCache.htm)|
Кэш данных из карточек подсистемы маршрутов.  
(Унаследован от
[KrCompileSourceStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileSourceStoreExtension.htm))  
##  __Методы
[AfterBeginTransaction](M_Tessa_Cards_Extensions_CardStoreExtension_AfterBeginTransaction.htm)|
Действие, выполняемое после начала транзакции.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
---|---  
[AfterRequest](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileSourceStoreExtension_AfterRequest.htm)|
Действие, выполняемое после сохранения карточки как при успешном, так и при
неудачном результате.  
(Унаследован от
[KrCompileSourceStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileSourceStoreExtension.htm))  
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
[BeforeRequest](M_Tessa_Cards_Extensions_CardStoreExtension_BeforeRequest.htm)|
Действие, выполняемое перед сохранением карточки стандартными средствами.
Может установить ответ на запрос для того, чтобы сохранение карточки
стандартными средствами не выполнялось.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
[BuildAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileStageTemplateStoreExtension_BuildAsync.htm)|
Выполняет компиляцию сценариев.  
(Переопределяет
[KrCompileSourceStoreExtension.BuildAsync(ICardStoreExtensionContext)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileSourceStoreExtension_BuildAsync.htm))  
[CanBuild](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileSourceStoreExtension_CanBuild.htm)|
Возвращает значение, показывающее, возможна ли компиляция сценариев или нет.  
(Унаследован от
[KrCompileSourceStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileSourceStoreExtension.htm))  
[CardChanged](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileStageTemplateStoreExtension_CardChanged.htm)|
Возвращает значение, показывающее, наличие изменений в карточке.  
(Переопределяет
[KrCompileSourceStoreExtension.CardChanged(Card)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileSourceStoreExtension_CardChanged.htm))  
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
[SourceChanged](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileStageTemplateStoreExtension_SourceChanged.htm)|
Возвращает значение, показывающее, наличие изменений в сценариях.  
(Переопределяет
[KrCompileSourceStoreExtension.SourceChanged(Card)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrCompileSourceStoreExtension_SourceChanged.htm))  
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
